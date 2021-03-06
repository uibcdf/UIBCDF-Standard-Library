"""
Test_UIBCDF_Library
This must be a short description of the project
"""

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

# Add imports here
from . import lists
from . import tuples
from . import lists_and_tuples
from . import input_arguments
from . import exceptions
from . import colors

