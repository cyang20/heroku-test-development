from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  #return 'Hello, World!  Updated Flask from 0.11 to 1.0 to 1.1.1'
  print("Hello, world - printed!")
