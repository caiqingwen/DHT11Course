from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%M-%D  %H:%M")
    templateData = {
        'title':"Hello Page",
        'time': timeString
    }
    return render_template('main.html',**templateData)

if __name__ == '__main__':
    app.run(host="10.254.24.50",port=22,debug=True)