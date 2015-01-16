import subprocess
import sys
from bottle import run, request, post
import json

from os import environ

freeipa_url = environ['FREEIPA_URL']


def call_freeipa(json_command):
    curl = 'curl -s -H referer:%sipa ' % freeipa_url + \
        '-H "Content-Type:application/json" ' + \
        '-H "Accept:application/json" --negotiate -u : --cacert /etc/ipa/ca.crt ' + \
        '-d ' +  "'" + json_command + "'" \
        ' -X POST %sipa/json' % freeipa_url

    return subprocess.check_output(curl, shell=True)


@post('/api')
def api():
    return json.loads(call_freeipa(json.dumps(request.json)))

run(host='0.0.0.0', port=8081)
