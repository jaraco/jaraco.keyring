import os

import keyring
import cherrypy


class Keyring:
    exposed = True

    def GET(self, service, username):
        return keyring.get_password(service, username)

    def PUT(self, service, username):
        password = cherrypy.request.body
        keyring.set_password(service, username, password)
        return 'OK'

    def DELETE(self, service, username):
        keyring.delete_password(service, username)
        return 'OK'

    @classmethod
    def run(cls):
        config = {
            'global': {
                'server.socket_host': '::1',
                'server.socket_port': int(os.environ.get('PORT', 4273)),
            },
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            },
        }
        cherrypy.quickstart(cls(), config=config)


if __name__ == '__main__':
    Keyring.run()
