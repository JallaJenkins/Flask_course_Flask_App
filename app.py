from flask import Flask, jsonify, request, url_for, redirect, session

app = Flask(__name__)

# app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "Thisisasecret"

@app.route("/")
def index():
  session.pop('name', None)
  return f"<h1>Hello!</h1>"

@app.route("/home", methods=['POST', 'GET'], defaults={'name' : "Default"})
@app.route("/home/<string:name>", methods=['POST', 'GET'])
def home(name):
  session['name'] = name
  return f"<h1>Hello {name}, you are on the home page</h1>"

@app.route("/json")
def json():
  # if 'name' in session:
  my_list = [1, 2, 3, 4]
  name = session['name']
  # else:
    # name = "NotInSession"
  return jsonify({'key' : 'value', 'key2' : [1, 2, 3], 'name' : name})

@app.route('/query')
def query():
  name = request.args.get('name')
  location = request.args.get('location')
  return f"<h1>Hi {name}! You are from {location} on the query page.</h1>"

@app.route('/theform', methods=['GET', 'POST'])
def theform():
  if request.method == "GET":
    return """<form method="POST" action="/theform">
              <input type="text" name="name">
              <input type="text" name="location">
              <input type="submit" value="Submit">
              </form>"""
  else:
    name = request.form["name"]
    location = request.form["location"]
  #   return f"Hello {name} from {location}! You have submitted the form successfully"
    return redirect(url_for('home', name=name, location=location))

@app.route("/processjson", methods=['POST'])
def processjson():
  data = request.get_json()
  name = data['name']
  location = data['location']
  randomlist = data['randomlist']
  return jsonify({'result' : 'Success!', 'name' : name, 'location' : location, "randomkeyinlist" : randomlist[1]})

if __name__ == '__main__':
  app.run()