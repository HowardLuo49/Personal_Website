from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/coursework")
def coursework():
    return render_template("coursework.html")

@app.route("/teaching")
def teaching():
    return render_template("teaching.html")

@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)