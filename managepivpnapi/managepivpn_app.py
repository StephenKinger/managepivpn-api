import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web
import json

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class UserHandler(tornado.web.RequestHandler):
    def getUserList(self):
        return {'me':'me'}
    def get(self):
        self.write(json.dumps(self.getUserList()))

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