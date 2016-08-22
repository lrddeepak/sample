from bottle import Bottle, run
app =Bottle()


@app.route('/')
def index():
    return "Hi there"

run(app, host='0.0.0.0', port='5000',debug = True)