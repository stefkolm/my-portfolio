from flask import Flask, render_template, request
import tele

app = Flask(__name__)

@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route('/')
def home():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)