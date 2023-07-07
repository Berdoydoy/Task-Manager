from flask import Flask,render_template, request,Markup,url_for,redirect

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('summarize.html')
