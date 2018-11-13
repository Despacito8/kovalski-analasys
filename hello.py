from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world</h1>'

@app.route('/animals/<name>')
def przywitajZwierze(name):
    return f'<h1>Witaj {name}</h1>'