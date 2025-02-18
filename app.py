from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, URLField, StringField
from wtforms.validators import DataRequired, Email, Length, URL

app = Flask(__name__)
app.secret_key = "sdf44"


class SignUpForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    remember_me = BooleanField(label="Remember me")
    submit = SubmitField(label="Sign Up")


class PasswordForm(FlaskForm):
    url = URLField(label="Website URL", validators=[DataRequired(), URL()])
    username = StringField(label="Username")
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    save = SubmitField(label="Save")


@app.route("/", methods=["GET", "POST"])
def home():
    form = PasswordForm()
    if form.validate_on_submit():
        pass
    return render_template("pages/index.html", active_page='home', form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("pages/signup.html", form=form)


@app.route("/passwords")
def passwords():
    return render_template("pages/passwords.html", active_page='passwords')


if __name__ == '__main__':
    app.run(debug=True)
