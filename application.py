from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from math2code import LaTeX2Python

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def tasks():
    if "latex_formulas" not in session:
        session["latex_formulas"] = []
        session["python_formulas"] = []
    return render_template("formulas.html", latex_formulas=session["latex_formulas"], 
            python_formulas=session["python_formulas"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        latex_formula = request.form.get("latex_formula")
        session["latex_formulas"].append(latex_formula)
        l2p = LaTeX2Python(latex_formula)
        session["python_formulas"].append(l2p.latex_to_python(latex_formula))
        return redirect("/")