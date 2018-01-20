import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web
import json
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor   # `pip install futures` for python2
import time


MAX_WORKERS=5

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class UserHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    @run_on_executor
    def retrieveUserList(self):
        time.sleep(5)
        return {'me':'me'}

    @tornado.gen.coroutine
    def get(self):
        result = yield self.retrieveUserList()
        self.write(json.dumps(result))

class Hello():
    def __init__(self, host, port):
        print host + " " + port

    def coucou(self):
        print 'coucou'

class ManagePIVPNApp(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        app = tornado.web.Application(
            [(r'/', IndexHandler), (r'/user', UserHandler)],
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static')
        )
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(self.port, self.host)
        tornado.ioloop.IOLoop.instance().start()

    def stop(self):
        tornado.ioloop.IOLoop.instance().stop()