# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, jsonify, make_response, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')  # Captura o User-Agent
    return f'<h1>Hello, {name} Mendes!</h1><p>Your browser: {user_agent}</p>'

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

@app.route('/setcookie/<username>')
def set_cookie(username):
    resp = make_response('<h1>This document carries a cookie!</h1>')
    resp.set_cookie('username', username)
    return resp

@app.route('/redirect')
def redirecionar():
    return redirect('https://ptb.ifsp.edu.br/')

@app.errorhandler(404)
def not_found(error):
    return '<h1>404 Not Found</h1><p>A URL solicitada não foi encontrada no servidor.</p>', 404

if __name__ == '__main__':
    app.run(debug=True)
