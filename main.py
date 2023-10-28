from flask import Flask, render_template, request
import tele

app = Flask(__name__)


@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    tele.send_message(str(user_ip))
    tele.send_message(str(user_agent))
    print(user_ip)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)