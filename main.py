import requests
from flask import *
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')
def home():
    return {'status':True}

def stream_with_context(generator_function):
  for chunk in generator_function:
      yield chunk

@app.route('/cors',methods=['GET','POST'])
def coe():
    url = request.args.get('url')
    req = requests.get(url).content
    return req


@app.route('/ibomma',methods=['GET','POST'])
def download_file():
    url = request.args.get('url')
    resp = requests.get(url,headers = {"Referer" : "https://seucre-otp-ymflg-h002giy-ig-india.ibc.wf/"}, stream=True)
    return Response(stream_with_context(resp.iter_content(chunk_size=1024)),
                    content_type=resp.headers['Content-Type'])


if __name__ == '__main__':
    app.run()
