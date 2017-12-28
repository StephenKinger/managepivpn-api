import unittest
from managepivpnapi.managepivpn_app import ManagePIVPNApp
import threading
import time
from tornado import httpclient


class BackgroundServer(threading.Thread):
    def __init__(self, api):
        threading.Thread.__init__(self)
        self.api = api

    def run(self):
        print 'running'
        self.api.run()

class RootTest(unittest.TestCase):

    def setUp(self):
        print "starting server"
        self.api = ManagePIVPNApp('0.0.0.0', '8082')
        self.backgroundserver = BackgroundServer(self.api)
        self.backgroundserver.start()
        time.sleep(10)

    def tearDown(self):
        print "stopping server"
        self.api.stop()
        self.backgroundserver.join()

    def test_RootAnswer(self):
        print "http://127.0.0.1/"
        http_client = httpclient.HTTPClient()
        try:
            response = http_client.fetch("http://127.0.0.1:8082")
            print(response.body)
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print("Error: " + str(e))
        except Exception as e:
            # Other errors are possible, such as IOError.
            print("Error: " + str(e))
        http_client.close()


