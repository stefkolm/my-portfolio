from flask import Flask, render_template, request
import tele

app = Flask(__name__)


@app.route('/')
def home():
    user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    tele.send_message(str(f"User from: {user_ip}"))
    print(user_ip)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)