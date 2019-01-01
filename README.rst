.. image:: https://img.shields.io/pypi/v/skeleton.svg
   :target: https://pypi.org/project/skeleton

.. image:: https://img.shields.io/pypi/pyversions/skeleton.svg

.. image:: https://img.shields.io/travis/jaraco/skeleton/master.svg
   :target: https://travis-ci.org/jaraco/skeleton

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/skeleton/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/skeleton/branch/master

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

Remote Agent Keyring
--------------------

Implements a remote agent keyring for use over SSH connections.

Requires OpenSSH 6.7.

To use, on the host machine, install jaraco.keyring and invoke
the server::

    python -m jaraco.keyring.server

That starts a server listening only on localhost:4273.

Then, connect to the remote host and forward the traffic back to
the keyring server::

    ssh -R /tmp/keyring.sock:localhost:4273 remote_host

This command creates a unix domain socket at /tmp/keyring.sock
which only that user can access.

Then, on that host, configure keyring to use the remote agent
backend. For example,

    keyring -b jaraco.keyring.RemoteAgent get SERVICE USERNAME

The remote agent backend will request the password over the
tunnel, where the server will request the password using the
default configuration.
