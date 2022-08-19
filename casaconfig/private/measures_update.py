# Copyright 2020 AUI, Inc. Washington DC, USA
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
this module will be included in the api
"""

def measures_update(path=None, version=None, force=False, logger=None, extract_observatories=False):
    """
    Retrieve IERS data used for measures calculations from ASTRON FTP server
    
    Original data source is here: https://www.iers.org/IERS/EN/DataProducts/data.html

    By default, the Observatories table is not extracted from the ASTRON tarfile. CASA provides an Observatories
    file with the other data products (which can be retried using the pull_data function) and that Observatories table
    is recommended for CASA users. casaconfig module users who wish to use the ASTRON provided Observatories table
    can set the extract_observatories parameter to True to extract that from the tarball. 
    
    Parameters
       - path (str=None) - Folder path to place updated measures data. Default None places it in package installation directory
       - version (str=None) - Version of measures data to retrieve (usually in the form of yyyymmdd-160001.ztar, see measures_available()). Default None retrieves the latest
       - force (bool=False) - If True, always re-download the measures data. Default False will not download measures data if already updated today unless version parameter is specified and different from what was last downloaded.
       - logger (casatools.logsink=None) - Instance of the casalogger to use for writing messages. Default None writes messages to the terminal
       - extract_observatories (bool=False) - If True, also extract the Observatories table. Default do not extract the Observatories table.
        
    Returns
       None
    
    """
    from ftplib import FTP
    import tarfile
    import os
    import re
    from datetime import datetime
    import pkg_resources
    import sys
    
    if path is None: path = pkg_resources.resource_filename('casaconfig', '__data__/')
    path = os.path.expanduser(path)
    if not os.path.exists(path): os.mkdir(path)
    current = None
    updated = None

    # if measures are already preset, get their version
    if os.path.exists(os.path.join(path, 'geodetic/readme.txt')):
        try:
            with open(os.path.join(path,'geodetic/readme.txt'), 'r') as fid:
                readme = fid.readlines()
            current = readme[1].split(':')[-1].strip()
            updated = readme[2].split(':')[-1].strip()
        except:
            pass

    # don't re-download the same data
    if not force:
        if ((version is not None) and (version == current)) or ((version is None) and (updated == datetime.today().strftime('%Y-%m-%d'))):
            print('casaconfig current measures detected in %s, using version %s' % (path, current), file = sys.stderr )
            if logger is not None: logger.post('casaconfig current measures detected in %s, using version %s' % (path, current), 'INFO')
            return

    # path must be writable with execute bit set
    if (not os.access(path, os.W_OK | os.X_OK)) :
        print('No permission to write to the measures path, cannot update : %s' % path, file = sys.stderr )
        if logger is not None: logger.post('No permission to write to the measures path, cannot update : %s' % path, 'ERROR')
        return

    print('casaconfig connecting to ftp.astron.nl ...', file = sys.stderr )
    if logger is not None: logger.post('casconfig connecting to ftp.astron.nl ...', 'INFO')

    ftp = FTP('ftp.astron.nl')
    rc = ftp.login()
    rc = ftp.cwd('outgoing/Measures')
    files = sorted([ff for ff in ftp.nlst() if (len(ff) > 0) and (not ff.endswith('.dat')) and (ftp.size(ff) > 0)])

    # target filename to download
    target = files[-1] if version is None else version
    if target not in files:
        if logger is not None: logger.post('casaconfig cant find specified version %s' % target, 'ERROR')
        else: print('##### ERROR: cant find specified version %s #####' % target)
        return
    
    with open(os.path.join(path,'measures.ztar'), 'wb') as fid:
        print('casaconfig downloading %s from ASTRON server to %s ...' % (target, path), file = sys.stderr )
        if logger is not None: logger.post('casaconfig downloading %s from ASTRON server to %s ...' % (target, path), 'INFO')
        ftp.retrbinary('RETR ' + target, fid.write)

    ftp.close()
    
    # extract from the fetched tarfile
    with tarfile.open(os.path.join(path,'measures.ztar'),mode='r:gz') as ztar:
        # the list of members to extract
        x_list = []
        for m in ztar.getmembers() :
            # always exclude *.old names in geodetic and usually exclude Observatories
            do_skip = re.search('geodetic',m.name) and re.search('.old',m.name)
            if not extract_observatories:
                do_skip = do_skip or re.search('Observatories',m.name)
            if not do_skip:
                x_list.append(m)

        ztar.extractall(path=path,members=x_list)
        ztar.close()

    os.system("rm %s" % os.path.join(path, 'measures.ztar'))
    with open(os.path.join(path,'geodetic/readme.txt'), 'w') as fid:
       fid.write("# measures data populated by casaconfig\nversion : %s\ndate : %s" % (target, datetime.today().strftime('%Y-%m-%d')))

    return
