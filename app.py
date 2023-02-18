from flask import Flask

app = Flask(__name__)

world = "Minh"


@app.route("/")
def Hello_world():
  return f"<h1>Hello_{world}!<h1/>"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
