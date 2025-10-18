from flask import Flask, render_template, request
from vercel_wsgi import handle_wsgi

app = Flask(__name__, template_folder="../templates", static_folder="../static")

USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return f"<h1>Welcome, {username}!</h1>"
    else:
        return render_template('login.html', message="Invalid username or password")

# This is for Vercel serverless
def handler(request, context):
    return handle_wsgi(app, request, context)
