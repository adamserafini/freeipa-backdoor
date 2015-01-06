import subprocess
import sys
from bottle import run, request, post
import json

def call_freeipa(json_command):
  curl = 'curl -s -H referer:https://ds02.cs.dmc-int.net/ipa ' + \
         '-H "Content-Type:application/json" ' + \
         '-H "Accept:application/json" --negotiate -u : --cacert /etc/ipa/ca.crt ' + \
         '-d ' +  "'" + json_command + "'" \
         ' -X POST https://ds02.cs.dmc-int.net/ipa/json'

  return subprocess.check_output(curl, shell=True)

@post('/api')
def api():
  return json.loads(call_freeipa(json.dumps(request.json)))

run(host='0.0.0.0', port=8081)
