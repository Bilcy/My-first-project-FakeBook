#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello SmartNinja! <h1>Test </h1><h2>KONCNO </h2> ')

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),

], debug=True)
