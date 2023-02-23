from flask import Flask

app = Flask(__name__)

@app.route('/check', methods=['GET'])
def get():
    return 'ok'