"""privaan tool to be notifyed when someone access to an apache server.

Usage: __init__.py [HOST] PORT

Arguments:
    HOST  host where to expose the service [default: 0.0.0.0]
    PORT  port to expose the service

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from managepivpn_app import ManagePIVPNApp
from docopt import docopt

__all__ = ['managepivpnapi_run', '__version__']

__version__ = "0.0.1"


def managepivpnapi_run():
    args = docopt(__doc__, version=__version__)
    print args
    app = ManagePIVPNApp(args["HOST"], args["PORT"])
    app.run()



if __name__ == '__main__':
    managepivpnapi_run()