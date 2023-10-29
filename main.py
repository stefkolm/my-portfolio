from flask import Flask, render_template, request, redirect, url_for
import tele

app = Flask(__name__)

@app.before_request
def before_request():
    if not request.is_secure:
        return redirect("https://www.stefkolm.com/", code=code)

@app.route('/')
def home():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)