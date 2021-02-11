.. image:: https://img.shields.io/pypi/v/skeleton.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/skeleton.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/skeleton

.. image:: https://github.com/jaraco/skeleton/workflows/tests/badge.svg
   :target: https://github.com/jaraco/skeleton/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

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
