from flask import Flask, render_template, request

app = Flask(__name__)

USER_ID = 'admin'
USER_PW = '1234'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    result = ''
    if request.method == 'POST':
        user_id = request.form['username']
        user_pw = request.form['password']
        if user_id == USER_ID and user_pw == USER_PW:
            result = '로그인 성공!'
        else:
            result = '로그인 실패...'
    return render_template('login.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
