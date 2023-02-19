from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        Number = request.form.get("Number")
        result = ""
        try:
            int(Number)
        except:
            result = "not a number "+request.form.get("Number")
            return render_template("result.html",result=result)
        if int(Number)%2 == 0:
            result = "even "+request.form.get("Number")
            return render_template("result.html",result=result)
        else:
            result = "odd "+request.form.get("Number")
            return render_template("result.html",result=result)
    return render_template("form.html")
        

if __name__ == "__main__":
    app.run(debug = True)