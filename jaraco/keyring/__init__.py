import requests
import keyring.backend

class RemoteAgent(keyring.backend.Backend):
	_url_tmpl = 'http://localhost:4273/{service}/{username}'

	@classmethod
	def priority(cls):
		return 3.1

	def get_password(self, service, username):
		url = self._url_tmpl.format(**locals())
		return requests.get(url).text

	def set_password(self, service, username, password):
		url = self._url_tmpl.format(**locals())
		requests.post(url, data=password)

	def delete_password(self, service, username):
		url = self._url_tmpl.format(**locals())
		requests.delete(url).raise_for_status()
