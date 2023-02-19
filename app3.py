from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        register = {
            "name": request.form.get("Name"),
            "organization": request.form.get("Organization")
        }
        registered = []
        registered.append(register)
        return render_template("Registered.html",registered=registered)
    return render_template("Register.html")
        

if __name__ == "__main__":
    app.run(debug = True)