import webapp2
import grab
import json


class PatentHandler(webapp2.RequestHandler):

    def get(self):
        """Writes search results to endpoint"""
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        query = self.request.get('query', None)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(grab.patent_parse(query)))


handlers = webapp2.WSGIApplication([
    ('/api', PatentHandler)
], debug=True)
