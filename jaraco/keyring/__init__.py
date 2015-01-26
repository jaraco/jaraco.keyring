import keyring.backend

class RemoteAgent(keyring.backend.Backend):
	@classmethod
	def priority(cls):
		return 3.1

	def get_password(self, service, username):
		return 'stubbed'

	def set_password(self, service, username, password):
		"stubbed"

	def delete_password(self, service, username):
		"stubbed"
