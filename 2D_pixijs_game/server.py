from gevent import monkey; monkey.patch_all()
from flask import Flask, Response, render_template, stream_with_context
from gevent.pywsgi import WSGIServer
import json
import time


app = Flask(__name__)


##############################
@app.route("/")
def render_index():
  return render_template("index.html")

##############################
@app.route("/listen")
def listen():

  def respond_to_client():
    while True:
      with open("color.txt", "r") as f:
        color = f.read()
        #print("server runs")
      if(color == "1"):
        _data = json.dumps({"color":color})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
      if(color == "2"):
        _data = json.dumps({"color":color})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
      if(color == "3"):
        _data = json.dumps({"color":color})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
      if(color == "4"):
        _data = json.dumps({"color":color})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"
      time.sleep(0.05)
  return Response(respond_to_client(), mimetype='text/event-stream')


@app.route("/right", methods=['POST','GET'])
def right():
  with open('color.txt', 'w') as f:
    f.truncate()
    f.write('1')
  return 'go right'

@app.route("/left", methods=['POST','GET'])
def left():
  with open('color.txt', 'w') as f:
    f.truncate()
    f.write('2')
  return 'go left'

@app.route("/krasit", methods=['POST','GET'])
def krasit():
  with open('color.txt', 'w') as f:
    f.truncate()
    f.write('3')
  return 'krasit'

@app.route("/stopkrasit", methods=['POST','GET'])
def stopkrasit():
  with open('color.txt', 'w') as f:
    f.truncate()
    f.write('4')
  return 'stopkrasit'

@app.route("/stop", methods=['POST','GET'])
def stop():
  with open('color.txt', 'w') as f:
    f.truncate()
  return 'stop'

@app.route("/joystick")
def joystick():
  return render_template("joystick.html")


##############################
if __name__ == "__main__":
  app.run()
  #app.run(port=80, debug=True)
  #http_server = WSGIServer(("localhost", 80), app)
  #http_server.serve_forever()










