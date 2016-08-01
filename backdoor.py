import subprocess
import sys
from bottle import run, request, post
import json

from os import environ

freeipa_url = environ['FREEIPA_URL']
krb_principal = environ['KRB_PRINCIPAL']
krb_password = environ['KRB_PASSWORD']

def call_freeipa(json_req):

    kinit = 'echo %s | kinit %s >/dev/null' % (krb_password, krb_principal)

    curl = 'curl -s -H referer:%sipa ' % freeipa_url + \
        '-H "Content-Type:application/json" ' + \
        '-H "Accept:application/json" --negotiate -u : --cacert /etc/ipa/ca.crt ' + \
        '-d ' +  "'" + json_req + "'" \
        ' -X POST %sipa/json' % freeipa_url

    return subprocess.check_output('%s; %s' % (kinit, curl), shell=True)


@post('/api')
def api():
    return json.loads(call_freeipa(json.dumps(request.json)))

run(host='0.0.0.0', port=sys.argv[1])
