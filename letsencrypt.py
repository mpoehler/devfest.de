import webapp2

class LetsEncryptHandler(webapp2.RequestHandler):
    def get(self, challenge):
        self.response.headers['Content-Type'] = 'text/plain'
        responses = {
            'rQdM6WAmon1pH-YRI-mbyfPIND6hqcNwCH8q_nzxqwI': 'rQdM6WAmon1pH-YRI-mbyfPIND6hqcNwCH8q_nzxqwI.DlYoCObwrBzgQU4uXQdkPNEsRrNNNHlHxzzD_ZYYRZk',
            'BJK3wReUL97dkNYOlHN2L-9yzZv3czXj7Ck2oQ_1z84': 'BJK3wReUL97dkNYOlHN2L-9yzZv3czXj7Ck2oQ_1z84.DlYoCObwrBzgQU4uXQdkPNEsRrNNNHlHxzzD_ZYYRZk'
        }
        self.response.write(responses.get(challenge, ''))

app = webapp2.WSGIApplication([
    ('/.well-known/acme-challenge/([\w-]+)', LetsEncryptHandler),
])
