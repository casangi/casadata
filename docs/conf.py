# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = u'casaconfig'
copyright = u'2022, Associated Universities, Inc'
author = u'National Radio Astronomy Observatory'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'autoapi.extension',
    'recommonmark'
]

todo_include_todos = True
add_module_names = False
numpy_show_class_members = False
nbsphinx_codecell_lexer = 'python3'
nbsphinx_execute = 'never'

nbsphinx_prolog = """
Open in Colab: https://colab.research.google.com/github/casangi/casaconfig/blob/master/docs/{{ env.doc2path(env.docname, base=None) }}

----
"""

autoapi_dirs = ['../casaconfig']
autoapi_add_toctree_entry = False
autoapi_generate_api_docs = True
autoapi_root = '_api/autoapi'
autoapi_options = ['show-module-summary']
autoapi_template_dir = '_templates'
autoapi_keep_files = True

# Napoleon settings
#napoleon_google_docstring = True
#napoleon_numpy_docstring = True
#napoleon_include_private_with_doc = False
#napoleon_include_special_with_doc = False
#napoleon_use_admonition_for_examples = False
#napoleon_use_admonition_for_notes = False
#napoleon_use_admonition_for_references = False
#napoleon_use_ivar = True
#napoleon_use_param = True
#napoleon_use_rtype = True

#List of imports to mock (this ensures readthedocs works)
#autodoc_mock_imports = ['numcodecs','os','numpy','time','xarray', 'numba', 'itertools','zarr','dask']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_logo = 'casa_logo-small.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': True,
    'navigation_depth': 3,
    'style_nav_header_background': 'white',
    'logo_only': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'casaconfig_docs'


# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'pdflatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'extraclassoptions': 'openany,oneside'
    #'sphinxsetup': 'hmargin={0.5in,0.5in}, vmargin={0.7in,0.7in}'
}

latex_logo = 'casa_logo-small.png'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'casaconfig_docs.tex', u'casaconfig documentation',
     u'National Radio Astronomy Observatory', 'manual'),
]


# -- Extension configuration -------------------------------------------------

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

#autosummary_generate = True
#autodoc_default_flags = ['members', 'inherited-members']


def setup(app):
    app.add_css_file('customization.css')