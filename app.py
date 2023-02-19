from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    d = datetime.now()    
    return render_template('index.html', 
    date = d.strftime("%A"), 
    month=d.strftime("%B"), 
    day=d.strftime("%d"), 
    year=d.year, 
    time=d.strftime("%X")) 

if __name__ == "__main__":
    app.run(debug = True)