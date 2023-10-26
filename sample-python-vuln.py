# This script uses cairosvg to convert a SVG file to a PDF
# version 2.6.0 has a CVE against it that was fixed in 2.7.0 and higher
# in order to generate meaningful load for New Relic's dashboard, it does this process multiple times

import newrelic.agent
newrelic.agent.initialize('newrelic.ini') #This is required!
import cairosvg
import time
import langchain
import nltk

inputurl = "https://random-word-api.herokuapp.com/word"

@newrelic.agent.background_task(name="NameyMcNameyFace", group='GroupyMcGroupFace')
def execute_task():
    #for x in range(1000):
    cairosvg.svg2pdf(url='https://dev.w3.org/SVG/tools/svgweb/samples/svg-files/USStates.svg', write_to='image.pdf')


counter = 0
while True:
    try:
        counter += 1
        print("counter is "+str(counter))
        execute_task()
        time.sleep(5)
    except KeyboardInterrupt:
        print('Interrupted')
        break

print('Program ended')
newrelic.agent.shutdown_agent(timeout=2.5)