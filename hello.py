from bottle import route, run

@route('/hello')
def hello():
    return "Hello World! Bacl to terminal windoes and CTRL+C"

run(host='localhost', port=8585, debug=True)

