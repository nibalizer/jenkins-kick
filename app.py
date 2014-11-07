from flask import Flask
app = Flask(__name__)

import os

import jenkinsapi
from jenkinsapi.jenkins import Jenkins

@app.route("/")
def docs_mainpage():
    docstext = ""
    with open("doc.html") as f:
        docstext = f.read()
    f.closed
    return docstext

@app.route("/list")
def list_nodes():
    ret = "<html><head><title>List of Nodes</title></head>"
    ret += "<body><h1>Nodes in Jenkins</h1>"
    for node in J.get_nodes().keys():
        ret += "<p>{0}".format(node)

    ret += "<p></body></html>"
    return ret

@app.route("/offline/<nodename>")
def make_node_offline(nodename):
    J.get_nodes()[str(nodename)].set_offline()
    return "Success!"

@app.route("/online/<nodename>")
def make_node_offline(nodename):
    J.get_nodes()[str(nodename)].set_online()
    return "Success!"



if __name__ == "__main__":
    try: 
        os.environ['JENKINS_KICK_DEBUG'] == 'True'
    except KeyError:
        debug = False
    else:
        debug = True

    J = Jenkins('http://localhost:8080')
    app.run(
        host='0.0.0.0',
        debug = debug,
        )
