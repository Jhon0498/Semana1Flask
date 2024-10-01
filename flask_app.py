from flask import Flask, request, jsonify, make_response, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextrequisition') 
def contexto():
    user_agent = request.headers.get('User-Agent') 
    return f'Your browser: {user_agent}</p>'  

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

@app.route('/abortar')
def abort():  # colocar para abort
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
