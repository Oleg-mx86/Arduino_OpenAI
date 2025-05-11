from bottle import route, run, request, response
from arduinoControl_ollama import ask_model

@route('/')
def home():
    return "Hello from AI-powered Arduino Server!"

@route('/ask', method='POST')
def ask():
    user_input = request.forms.get('prompt')
    result = ask_model(user_input)
    response.content_type = 'text/plain'
    return result

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
