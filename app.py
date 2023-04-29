from flask import Flask, request, make_response, redirect, render_template
import json

app = Flask(__name__)

#todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor ']
app.debug = True

"""
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)
"""

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/home'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/home')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        #'todos': todos,
    }
    print(f'Going home')
    return render_template('index.html', **context)

@app.route("/buy")
def buy_tickets():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        #'todos': todos,
    }
    print(f'Compra iniciada')
    return render_template('buy.html', **context)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)