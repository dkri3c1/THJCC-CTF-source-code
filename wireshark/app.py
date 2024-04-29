from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_session import Session  
app = Flask(__name__)


app.secret_key = 'your_secret_key'


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'Frieren' and request.form['password'] == 'B3stan1me':
            session['logged_in'] = True
            flash('You were successfully logged in', 'success')
            return redirect(url_for('flag'))
        else:
            flash('Login Failed', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/secret-flag')
def flag():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return 'THJCC{Fake_Flag}'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=1234)