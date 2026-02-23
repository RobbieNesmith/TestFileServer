import argparse

from flask import Flask, send_file

parser = argparse.ArgumentParser("TestFileServer", description="A server that serves the specified file at every route.")

parser.add_argument("filename")
parser.add_argument("--host", default="localhost")
parser.add_argument("--port", default="5000")
parser.add_argument("--code", default=200)

args = parser.parse_args()

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  resp = send_file(args.filename)
  resp.access_control_allow_origin = "*"
  resp.status_code=args.code
  return resp
if __name__ == '__main__':
  app.run(args.host, args.port)
