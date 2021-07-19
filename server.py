from flask import Flask, session, redirect, render_template, request

from users import User

app = Flask(__name__)
app.secret_key = "What even is a secret key tho"

@app.route('/')
def index():
    users = User.get_all_users()
    return render_template('index.html', users = users)

@app.route('/add_user')
def display_add_user():
    return render_template('new_user.html')


@app.route('/add_user/create', methods = ['POST'])
def add_user():
    User.create_user(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)