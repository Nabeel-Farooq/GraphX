#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sphinx configuration for RTGraph documentation.
"""

from pathlib import Path
import sys

# -------------------------------------------------------------------
# Path setup
# -------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from rtgraph.core.constants import Constants  # noqa: E402

# -------------------------------------------------------------------
# Project information
# -------------------------------------------------------------------

project = "RTGraph"
author = "Sebastian Sepulveda"
copyright = "2016, Sebastian Sepulveda"

FULL_VERSION = Constants.app_version

try:
    major, minor, patch = FULL_VERSION.split(".")
    version = f"{major}.{minor}"
    release = patch
except ValueError:
    version = FULL_VERSION
    release = FULL_VERSION

# -------------------------------------------------------------------
# General configuration
# -------------------------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

source_suffix = ".rst"

master_doc = "index"

language = "en"

pygments_style = "sphinx"

todo_include_todos = False

# -------------------------------------------------------------------
# Autodoc configuration
# -------------------------------------------------------------------

autodoc_member_order = "bysource"

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}

# -------------------------------------------------------------------
# HTML output
# -------------------------------------------------------------------

html_theme = "alabaster"

html_title = f"{project} Documentation"

html_static_path = ["_static"]

html_theme_options = {
    "description": "RTGraph Documentation",
    "fixed_sidebar": True,
    "show_powered_by": False,
    "github_user": "sebastians",
    "github_repo": "rtgraph",
}

htmlhelp_basename = "RTGraphdoc"

# -------------------------------------------------------------------
# LaTeX output
# -------------------------------------------------------------------

latex_elements = {
    # "papersize": "letterpaper",
    # "pointsize": "10pt",
    # "preamble": "",
    # "figure_align": "htbp",
}

latex_documents = [
    (
        master_doc,
        "RTGraph.tex",
        "RTGraph Documentation",
        author,
        "manual",
    ),
]

# -------------------------------------------------------------------
# Manual page output
# -------------------------------------------------------------------

man_pages = [
    (
        master_doc,
        "rtgraph",
        "RTGraph Documentation",
        [author],
        1,
    ),
]

# -------------------------------------------------------------------
# Texinfo output
# -------------------------------------------------------------------

texinfo_documents = [
    (
        master_doc,
        "RTGraph",
        "RTGraph Documentation",
        author,
        "RTGraph",
        "Graph analysis and visualization toolkit.",
        "Miscellaneous",
    ),
]

# -------------------------------------------------------------------
# Doctest configuration
# -------------------------------------------------------------------

doctest_global_setup = """
import rtgraph
"""

# -------------------------------------------------------------------
# Napoleon settings
# -------------------------------------------------------------------

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
