import os
import webapp2

from google.appengine.ext.webapp import template
import http2push as http2

class Handler(http2.PushHandler):

  @http2.push() # push_manifest.json is used by default.
  def get(self):
    # Resources in push_manifest.json will be server-pushed with index.html.
    path = os.path.join(os.path.dirname(__file__), 'build/unbundled/index.html')
    return self.response.write(template.render(path, {}))

app = webapp2.WSGIApplication([('/', Handler)])
