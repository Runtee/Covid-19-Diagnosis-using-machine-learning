from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from datetime import datetime
from .models import Profile, User

from . import db 
import pickle
import numpy as np

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def index():
    return render_template('home.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('Dashboard.html', current_user = current_user)


@main.route('/dashboard/test')
@login_required
def test():
    return render_template('test.html', current_user = current_user)


@main.route('/dashboard/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        profile = Profile.query.filter_by(user_id=current_user.id).first()
    
        if profile:
            profile.user_id = current_user.id
            profile.firstName = request.form['firstName']
            profile.middleName = request.form['middleName']
            profile.surName = request.form['surName']
            profile.email = request.form['email']
            profile.DOB = datetime.strptime(request.form['DOB'],'%Y-%m-%d')
            profile.phone = request.form['phone']
            profile.state = request.form['state']
            profile.LGA = request.form['LGA']
            profile.caddress = request.form['caddress']
            profile.bgroup = request.form['bgroup']
            profile.gtype = request.form['gtype']
            profile.sex = request.form['sex']
            db.session.commit()

        user_id = current_user.id
        firstName = request.form['firstName']
        middleName = request.form['middleName']
        surName = request.form['surName']
        email = request.form['email']
        DOB = datetime.strptime(request.form['DOB'],'%Y-%m-%d')
        phone = request.form['phone']
        state = request.form['state']
        LGA = request.form['LGA']
        caddress = request.form['caddress']
        bgroup = request.form['bgroup']
        gtype = request.form['gtype']
        sex = request.form['sex']
        new_profile = Profile(user_id = user_id,firstName=firstName, middleName=middleName, surName=surName,
                              email=email, DOB=DOB, phone=phone, state=state, LGA=LGA,
                              caddress=caddress, bgroup=bgroup, gtype=gtype, sex=sex)
        db.session.add(new_profile)
        db.session.commit()
        return redirect('/dashboard/profile')
    else:
        profile = Profile.query.filter_by(user_id=current_user.id).first()

        return render_template('profile.html',profile= profile)

model = pickle.load(open('model.pkl','rb'))


@main.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output =  prediction[0]
    if output == 1:
        result =  'Postive'
    else:
        result = 'Negative'
    return render_template('result.html', output = result)


@main.route('/dashboard/changePassword', methods=['GET','POST'])
def changePassword():
    if request.method == 'POST':
        password = request.form['password']        
        npassword = request.form['npassword']
        cpassword = request.form['cpassword']
        
        user = User.query.filter_by(username=current_user.username).first()


        if not user.verify_password(password):
            flash('The current password you entered is incorrect.')
            return redirect('/dashboard/changePassword')
        else:
            user.password = npassword
            db.session.commit()
            return render_template('successfulP.html') 
    else:
        return render_template('changePassword.html')



