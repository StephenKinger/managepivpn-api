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

    @classmethod
    def setUpClass(cls):
        print "starting server"
        cls.api = ManagePIVPNApp('0.0.0.0', '8082')
        cls.backgroundserver = BackgroundServer(cls.api)
        cls.backgroundserver.start()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        print "stopping server"
        cls.api.stop()
        cls.backgroundserver.join()

    def test_RootAnswer(self):
        print "http://127.0.0.1/"
        http_client = httpclient.HTTPClient()
        no_exception = True
        try:
            response = http_client.fetch("http://127.0.0.1:8082")
            print(response.body)
            self.assertIn('<body>', response.body, '<body> not present in response')
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print("Error: " + str(e))
            no_exception = False
        except Exception as e:
            # Other errors are possible, such as IOError.
            print("Error: " + str(e))
            no_exception = False
        self.assertEqual(no_exception, True, 'Exception during request')
        http_client.close()

    def test_UsersAnswer(self):
        print "http://127.0.0.1/"
        http_client = httpclient.HTTPClient()
        no_exception = True
        try:
            response = http_client.fetch("http://127.0.0.1:8082/user")
            print(response.body)
            self.assertEqual('{\"me\": \"me\"}', response.body, 'Not expected answer for user')
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print("Error: " + str(e))
            no_exception = False
        except Exception as e:
            # Other errors are possible, such as IOError.
            print("Error: " + str(e))
            no_exception = False
        self.assertEqual(no_exception, True, 'Exception during request')
        http_client.close()
