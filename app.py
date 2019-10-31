from flask import Flask,url_for,request,abort,redirect,render_template,flash,get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from models import db
app = Flask(__name__)


app.secret_key ="dsfjkshdhfusi8978"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    "mysql://root:123@127.0.0.1:3306/test_flask"
db.init_app(app)
# app.register_blueprint(user_bp,url_prefix='/user')

@app.route('/feed_back')
def feed_back():
    url_for('static', filename='style.css')
    return render_template('feed_back.html')

@app.route('/feed_back_manage')
def feed_back_manage():
    url_for('static', filename='style.css')
    return render_template('feed_back_manage.html')

@app.route('/front_login')
def front_login():
    url_for('static', filename='style.css')
    return render_template('front_login.html')

@app.route('/front_register')
def front_register():
    url_for('static', filename='style.css')
    return render_template('front_register.html')

@app.route('/groups_manage')
def groups_manage():
    url_for('static', filename='style.css')
    return render_template('groups_manage.html')

@app.route('/manager_login')
def manager_login():
    url_for('static', filename='style.css')
    return render_template('manager_login.html')

@app.route('/user_about')
def user_about():
    url_for('static', filename='style.css')
    return render_template('user_about.html')

@app.route('/user_center')
def user_center():
    url_for('static', filename='style.css')
    return render_template('user_center.html')

@app.route('/users_manage')
def users_manage():
    url_for('static', filename='style.css')
    return render_template('users_manage.html')

@app.route('/words_manage')
def words_manage():
    url_for('static', filename='style.css')
    return render_template('words_manage.html')



if __name__ == '__main__':
    app.run()
