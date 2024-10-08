from flask import Flask, render_template, request, session, redirect, url_for
from config import Config
from middle_secure import auth
import bcrypt
import os
from models import db, User, Book
from data_loader import load_sample_data

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/logout')
@auth
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            session['user_id'] = user.id
            session['username'] = user.username
            session['email'] = user.email
            return redirect(url_for('home'))
        
        return render_template('login.html', error="Invalid email or password")
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('register.html', error="Email is already in use.")
        
        new_user = User(username=username, email=email, password=password, name=name)
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id
        session['username'] = new_user.username
        session['email'] = new_user.email
        return redirect(url_for('home'))
    
    return render_template('register.html')

#Quản trị account
@app.route('/sitemanager', methods=['GET', 'POST'])
def sitemanager():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['admin'] = True
            return redirect(url_for('manage_users'))
        else:
            return render_template('sitemanager.html', error="Invalid credentials")
    return render_template('sitemanager.html')

@app.route('/sitemanage_users')
def manage_users():
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    users = User.query.all()
    return render_template('sitemanage_users.html', users=users)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('manage_users'))

@app.route('/add_user', methods=['POST'])
def add_user():
    if 'admin' not in session:
        return redirect(url_for('sitemanager'))
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    new_user = User(username=username, email=email, password=password, name=username)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('manage_users'))

@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    books = Book.query.paginate(page=page, per_page=20)
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html', book=book)

@app.route('/profile')
@auth
def profile():
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

def init_db():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        load_sample_data()
    
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
