from flask import render_template_string, request, render_template
import re
from . import app
import datetime

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/log')
def log():
    f = open("log.txt","r")
    daLog = f.read().split("\n")
    daLog = [x.split("$") for x in daLog]
    f.close()
    return render_template("log.html",log=daLog)

@app.route('/logme')
def logme():
    f = open("log.txt","w+")
    leNow = datetime.datetime.now().strftime("%d %b %Y %I:%M %p")
    leArgs = ["%s:%s"%(x,request.args[x]) for x in request.args.keys()]
    leArgs = ",".join(leArgs)
    f.write("%s$%s"%(leNow,leArgs))
    f.close()
    return ('', 204)
