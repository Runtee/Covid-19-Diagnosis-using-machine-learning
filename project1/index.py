# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, render_template, request, redirect
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datab.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# from werkzeug.security import generate_password_hash, check_password_hash

# class Profile(db.Model):
#     __tablename__ = 'profiles'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     firstName = db.Column(db.String(64), unique=False)
#     middleName = db.Column(db.String(64), unique=False)
#     surName = db.Column(db.String(64), unique=False)
#     email = db.Column(db.String(64), unique=False)
#     DOB = db.Column(db.Date, unique=False)
#     phone = db.Column(db.Integer, unique=False)
#     state = db.Column(db.String(64), unique=False)
#     LGA = db.Column(db.String(64), unique=False)
#     caddress = db.Column(db.String(64), unique=False)
#     bgroup = db.Column(db.String(64), unique=False)
#     gtype = db.Column(db.String(64), unique=False)
#     sex = db.Column(db.String(64), unique=False)

#     def __repr__(self):
#         return 'profile' % self.id


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128))
#     profiles = db.relationship('Profile', backref='role')

#     def __repr__(self):
#         return 'user is' % self.username
#     @property
#     def password(self):
#         raise AttributeError('password is not a readable attribute')

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)


# @app.route('/')
# @app.route('/home')
# def index():
#     return render_template('home.html')


# @app.route('/signup')
# def signup():
#     return render_template('Create.html')


# @app.route('/signup/post', methods=['POST'])
# def signup_post():
#     username = request.form['username']
#     password = request.form['password']
#     new_user = User(username=username, password=password)
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect('/login')


# @app.route('/login')
# def login_post():
#     return render_template('Login.html')


# @app.route('/login/post')
# def login():
#     return render_template('Login.html')


# @app.route('/dashboard')
# def dashboard():
#     return render_template('Dashboard.html')


# @app.route('/dashboard/test')
# def test():
#     return render_template('test.html')


# @app.route('/dashboard/profile', methods=['GET', 'POST'])
# def profile():
#     if request.method == 'POST':

#         firstName = request.form['firstName']
#         middleName = request.form['middleName']
#         surName = request.form['surName']
#         email = request.form['email']
#         DOB = request.form['DOB']
#         phone = request.form['phone']
#         state = request.form['state']
#         LGA = request.form['LGA']
#         caddress = request.form['caddress']
#         bgroup = request.form['bgroup']
#         gtype = request.form['gtype']
#         sex = request.form['sex']
#         new_profile = Profile(firstName=firstName, middleName=middleName, surName=surName,
#                               email=email, DOB=DOB, phone=phone, state=state, LGA=LGA,
#                               caddress=caddress, bgroup=bgroup, gtype=gtype, sex=sex)
#         db.session.add(new_profile)
#         db.session.commit()
#         return redirect('/dashboard/profile')
#     else:
#         return render_template('profile.html')


# # if __name__ == '__main__':
# #     app.run(debug=1)
