#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import datetime

import os
import urllib

from google.appengine.ext import ndb
from google.appengine.api import users

import jinja2
import webapp2

import csv2json


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {'title':'city-widgets'}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class DataPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(csv2json.get_json())

class BootstrapPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('bootstrap.html')
        self.response.write(template.render({}))

class DynamicMapPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('dynamic-map.html')
        self.response.write(template.render({}))

class PlayerPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('player.html')
        self.response.write(template.render({}))

class TrafficPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('traffic.html')
        self.response.write(template.render({}))

class VictimsPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('victims.html')
        self.response.write(template.render({}))

print "a"
app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/get-data', DataPage),
  ('/bootstrap', BootstrapPage),
  ('/dynamic-map', DynamicMapPage),
  ('/player', PlayerPage),
  ('/traffic', TrafficPage),
  ('/victims', VictimsPage),
], debug=True)
