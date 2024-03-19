from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def homepage():
  resposta = {'teste': 30}
  return jsonify(resposta)


if __name__ == "__main__":
    app.run(debug=True)
    