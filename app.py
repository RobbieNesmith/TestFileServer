from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  resp = send_file("Trollface.png")
  resp.access_control_allow_origin = "*"
  return resp
if __name__ == '__main__':
  app.run()
