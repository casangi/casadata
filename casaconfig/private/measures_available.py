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


def measures_available():
    """
    List available measures versions on the ASTRON server

    This returns a list of the measures files available on the ASTRON
    server. The version parameter of measures_update must be one
    of the values in that list if set (otherwise the most recent version
    in this list is used).

    Parameters
       None
    
    Returns
       version names returned as list of strings

    Raises:
       - casaconfig.RemoteError - raised when when a socket.gaierror is seen, likely due to no network connection
       - Exception: raised when any unexpected exception happens

    """
    from ftplib import FTP_TLS
    import socket

    from casaconfig import RemoteError

    files = []
    try:
        ftps = FTP_TLS('ftp.astron.nl')
        # this doesn't work
        # rc = ftps.login()
        # but this does, go figure
        rc = ftps.sendcmd('USER anonymous')
        rc = ftps.sendcmd('PASS anonymous')
        rc = ftps.cwd('outgoing/Measures')
        files = ftps.nlst()
        ftps.quit()
        #files = [ff.replace('WSRT_Measures','').replace('.ztar','').replace('_','') for ff in files]
        files = [ff for ff in files if (len(ff) > 0) and (not ff.endswith('.dat'))]
    except socket.gaierror as gaierr:
        raise RemoteError("Unable to retrieve list of available measures versions : " + str(gaierr)) from None
    except Exception as exc:
        msg = "Unexpected exception while getting list of available measures versions : " + str(exc)
        raise Exception(msg)
        
    return files
