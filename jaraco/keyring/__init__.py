import urllib.parse

import keyring.backend
import requests_unixsocket

session = requests_unixsocket.Session()


class RemoteAgent(keyring.backend.KeyringBackend):
    """
    >>> agent = RemoteAgent()
    """

    path = '/tmp/keyring.sock'
    path_enc = urllib.parse.quote(path, safe='')
    _url_tmpl = 'http+unix://%(path_enc)s/{service}/{username}' % locals()

    priority = 0

    def get_password(self, service, username):
        url = self._url_tmpl.format(**locals())
        return session.get(url).text

    def set_password(self, service, username, password):
        url = self._url_tmpl.format(**locals())
        session.post(url, data=password)

    def delete_password(self, service, username):
        url = self._url_tmpl.format(**locals())
        session.delete(url).raise_for_status()
