from flask import Flask, render_template, request
import tele

app = Flask(__name__)


@app.route('/')
def home():
    user_ip = request.remote_addr
    tele.send_message(str(user_ip))
    print(user_ip)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)