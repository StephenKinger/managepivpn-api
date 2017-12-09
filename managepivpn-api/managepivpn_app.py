import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class ManagePIVPNApp():
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        app = tornado.web.Application(
            [(r'/', IndexHandler)],
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static')
        )
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(self.port, self.host)
        tornado.ioloop.IOLoop.instance().start()