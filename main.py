import requests
from flask import *
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')
def home():
    return {'status':True}

@app.route('/cors',methods=['GET','POST'])
def coe():
    url = request.args.get('url')
    req = requests.get(url).content
    return req

if __name__ == '__main__':
    app.run()
