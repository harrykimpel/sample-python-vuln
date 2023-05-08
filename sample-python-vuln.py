# This script makes an API call to get a random word, 
# then checks that word against the password strength module (Passeo)
# version 1.0.4 has a CVE against it that was fixed in 1.0.5 and higher
# in order to generate meaningful load for New Relic's dashboard, it does this process multiple times

import newrelic.agent
newrelic.agent.initialize('newrelic.ini') #This is required!
import cairosvg
import requests
import json
import time

inputurl = "https://random-word-api.herokuapp.com/word"

@newrelic.agent.background_task(name="NameyMcNameyFace", group='GroupyMcGroupFace')
def execute_task():
    #for x in range(1000):
    cairosvg.svg2pdf(url='https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/USStates.svg', write_to='image.pdf')


counter = 0
while True:
    counter += 1
    print("counter is "+str(counter))
    execute_task()
    time.sleep(5)

newrelic.agent.shutdown_agent(timeout=100)