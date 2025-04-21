from bottle import route, run

@route('/')
def home():
    return "Hello, Bottle!"

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
