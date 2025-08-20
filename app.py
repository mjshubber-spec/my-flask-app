from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Toilet Cleaning Log App Running!'

if __name__ == '__main__':
    app.run(debug=True)
