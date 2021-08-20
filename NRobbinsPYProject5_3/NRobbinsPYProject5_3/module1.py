# Import Flask class (render allows creation of html files)
from flask import Flask, render_template

# Create variable
app=Flask(__name__)

# Route app to home page
@app.route('/')
def home():
    return render_template("home.html")

# Route app to about page
@app.route('/about/')
def about():
    return render_template("about.html")

# Route app to hobbies page
@app.route('/hobbies/')
def hobbies():
    return render_template("hobbies.html")

# Run
if __name__=="__main__":
    app.run(debug=True)