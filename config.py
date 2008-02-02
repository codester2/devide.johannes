# FIXME: we could do more in this module to abstract OS differences
# for example, we could have a build command that varies per platform
# WIN32: 'devenv %s /project ALL_BUILD /projectconfig \
# "RelWithDebInfo|Win32" /build RelWithDebInfo'
# IX: make

# FIXME: each installpackage should be able to register its own
# library and python paths.  At the moment, devide.py is taking care
# of creating the script containing all these... (not optimal!)

import os
import sys

# for binaries not on your PATH, you should specify the complete path here,
# e.g. SVN = '/usr/bin/svn'.  For binaries ON your path, only the binary name
# e.g. SVN = 'svn'
SVN = 'svn'
CVS = 'cvs -z3'
PATCH = 'patch'

# FIXME: this should move to the platform dependent part of init()
# UNTIL THEN: change the 1 to 0 if you don't use distcc
if 1:
    MAKE = 'make -j6' # if you have more CPUS, up the -j parameter!
    CMAKE_PRE_VARS = 'CC="distcc cc" CXX="distcc c++"'
else:
    MAKE = 'make'
    CMAKE_PRE_VARS = ''

# nothing for you to edit below this line
#######################################################################

# currently, this is only being used by the devide InstallPackage to
# modify the devide version to include the johannes version used to
# build it, so it is important that you change this file (config.py)
# when you prepare a johannes-based release.

JOHANNES_REV = "$Revision$"
JOHANNES_REL = JOHANNES_REV.split()[1]

#DEVIDE_REL = "2482" # check svn log devide for this...
# same repo, current johannes should be able to build current devide
DEVIDE_REL = JOHANNES_REL
TUDVIS_REL = "203"

# the following variables are written by various InstallPackages
CMAKE = '' # this one will be completed by the cmake install package 
CMAKE_DEFAULT_PARAMS = '' # this will be set by init()

DCMTK_INCLUDE = ''
DCMTK_LIB = ''

VTK_DIR = ''
VTK_LIB = ''
VTK_PYTHON = ''

WX_LIB_PATH = ''
WXP_PYTHONPATH = ''

ITK_DIR = ''
WRAPITK_LIB = ''
WRAPITK_PYTHON = ''

DEVIDE_PY = ''

#######################################################################

def init(wd, the_profile):
    global working_dir, archive_dir, build_dir, inst_dir
    working_dir = os.path.abspath(wd)
    archive_dir = os.path.join(working_dir, 'archive')
    build_dir = os.path.join(working_dir, 'build')
    inst_dir = os.path.join(working_dir, 'inst')

    global profile
    profile = the_profile

    global python_library_path, python_binary_path
    #python_include_path = os.path.join(inst_dir, 'python/include/python2.5')
    python_library_path = os.path.join(inst_dir, 'python/lib')
    #python_library = os.path.join(python_library_path, 'libpython2.5.so')
    python_binary_path = os.path.join(inst_dir, 'python/bin')

    # platform dependent stuff =========================================
    # use conditionals based on os.name (posix, nt) and sys.platform (linux2,
    # win32)

    global CMAKE_DEFAULT_PARAMS

    if os.name == 'posix':
        CMAKE_DEFAULT_PARAMS = '-G "Unix Makefiles"'

    elif os.name == 'nt':
        CMAKE_DEFAULT_PARAMS = '-G "Visual Studio 7 .NET 2003"'

