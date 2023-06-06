from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return f"hi {name}"

if __name__ == "__main__":
    app.debug = True
    app.run(port=8001)
