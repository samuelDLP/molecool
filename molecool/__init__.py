"""
molecool
A Python package for analyzing and visualizing xyz files.
"""

# Add imports here
from .functions import canvas
from .measure import calculate_distance, calculate_angle
from .visualize import draw_molecule, bond_histogram
from .molecule import build_bond_list

from . import io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
