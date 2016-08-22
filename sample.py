from bottle import Bottle, run
import os

app=Bottle()


@app.route('/')
def index():
    return "Hi there"

PORT = int(os.environ.get('D_PORT',  '80'))

app.run(host='0.0.0.0', port=PORT, debug=True)