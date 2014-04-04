import tornado.ioloop
import tornado.web
import tornado.escape
import handlers as hd




settings = {
    "cookie_secret": "跪舔高端大气上档次低调奢华有内涵狂拽酷炫叼炸天的伯克利博导大飞神",
    "login_url": "/login",
}


application = tornado.web.Application([
    (r"/", hd.MainHandler),
    (r"/login", hd.LoginHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()