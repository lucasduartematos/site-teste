from fk import Flask
app = Flask(__name__)
@app.route('/')
def hello_word():
  return "Olá, mundo! Esse é meu site. (Lucas Duarte)"
