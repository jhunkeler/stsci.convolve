__version__ = '2.0'
from Convolve import *
import iraf_frame


def test(*args,**kwds):
    thisdir = os.path.dirname(os.path.abspath(__file__))
    pytools.tester.test(curdir=thisdir)

try:
    from svn_version import __svn_version__, __full_svn_info__
except:
    __svn_version__ = 'Unable to determine SVN revision'
    __full_svn_info__ = __svn_version__

