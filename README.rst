.. image:: https://img.shields.io/pypi/v/PROJECT.svg
   :target: https://pypi.org/project/PROJECT

.. image:: https://img.shields.io/pypi/pyversions/PROJECT.svg

.. image:: https://github.com/PROJECT_PATH/actions/workflows/main.yml/badge.svg
   :target: https://github.com/PROJECT_PATH/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2023-informational
   :target: https://blog.jaraco.com/skeleton

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
