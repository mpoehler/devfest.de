import webapp2

class LetsEncryptHandler(webapp2.RequestHandler):
    def get(self, challenge):
        self.response.headers['Content-Type'] = 'text/plain'
        responses = {
            'beguyUUE_XH8uCPHxKlB2Ts89Xdoc_Cp53EHf1iz7s4': 'beguyUUE_XH8uCPHxKlB2Ts89Xdoc_Cp53EHf1iz7s4.ONja4hoK8i3BGvn-QMf9BKbPyaNRQ3FkecClr-1On6g',
            '[challenge 2]': '[response 2]'
        }
        self.response.write(responses.get(challenge, ''))

app = webapp2.WSGIApplication([
    ('/.well-known/acme-challenge/([\w-]+)', LetsEncryptHandler),
])