from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Feedback
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/account')
@login_required
def account():
    return render_template('account.html', user=current_user)

@views.route('/feedback', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        question1 = request.form.get('question1')
        question2 = request.form.get('question2')
        question3 = request.form.get('question3')
        question4 = request.form.get('question4')
        
        
        new_feedback = Feedback(
            question1=question1,
            question2=question2,
            question3=question3,
            question4=question4,
            user_id=current_user.id 
        )
        
   
        
        db.session.add(new_feedback)
        db.session.flush() 
        db.session.commit()
        
        
        flash('Feedback submitted successfully!', category='success')
        
    return render_template('home.html', user=current_user)
