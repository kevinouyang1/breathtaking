from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_route():
    return "hello daniel jiang"

if __name__ == '__main__':
    app.run()