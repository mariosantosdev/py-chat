from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.get('/')
def render_frontend():
    return render_template('/index.html')


@socketio.on('message')
def receive_message(payload):
    emit('message', payload, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
