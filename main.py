from flask import Flask, render_template, request, url_for

app = Flask(__name__)           # initialise the Flask application

@app.route('/', methods=["GET"])                 # define a route for the root URL
def index():
   if request.method == "GET":
     title = "Any Page"
     name = "Keano"
     message = "This is my first flask app!"
     return render_template ("index.html",  title=title, name=name, message=message)   # response sent when the route is accessed

@app.route("/about", methods=["POST"]) # Sends information from the FORM to the URL
def about():
    if request.method == "POST":
        username = request.form.get("username")
        age = request.form.get("age")
        title = "About Me"
        name = username
        message =  "Welcome to my first Flask app"
        return render_template("about.html", username=username, age=age, title=title, name=name, message=message)

@app.route('/hello') # Defaults to a GET request
def hello():
    name = "Keano"
    title = "New Page"
    message = "Hello world"
    return render_template("hello.html", name=name, message=message, title=title)

# running the application
if __name__ == '__main__':
    app.run(debug=True)