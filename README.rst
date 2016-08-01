================
FreeIPA-BackDoor
================

A Python script that can be installed on a
FreeIPA server to facilitate API access by external clients, without mucking
around with Kerberos certificates for the external client.
A typical use case might be that you are prototyping against the excellent,
but poorly documented FreeIPA JSON API.

Instructions
------------

1. Install the dependencies:

    $ pip install -r requirements.txt

2. Environment variables must be set on the target box, eg:

    $ export FREEIPA_URL=https://your.freeipa.net/

    $ export KRB_PRINCIPAL=admin

    $ export KRB_PASSWORD=password

3. Run the software:

    $ python backdoor.py

Congratulations. Your external client can now access the FreeIPA JSON API
on port 8081.
