from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pages/index.html", active_page='home')


@app.route("/signin")
def signin():
    return render_template("pages/signin.html")


@app.route("/passwords")
def passwords():
    return render_template("pages/passwords.html", active_page='passwords')


if __name__ == '__main__':
    app.run(debug=True)
