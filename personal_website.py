from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return "<h1>Welcome to My Personal Website</h1><p>This is the home page.</p>"

# About Me page
@app.route("/about")
def about():
    return "<h1>About Me</h1><p>Here is some information about me.</p>"

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)  # Use port 8081 for the second app
