from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import RegistrationForm, LoginForm, BugForm
from app.models import User
from app.models import Bug
from app.extensions import db

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index')) 

    form = RegistrationForm()
    if form.validate_on_submit():  
        hashed_password = generate_password_hash(form.password.data)  
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)    
        db.session.commit()
        flash('Konto zostało utworzone. Możesz się teraz zalogować.', 'success')
        return redirect(url_for('main.login'))  

    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index')) 

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Zalogowano pomyślnie!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło.', 'danger')

    return render_template('login.html', form=form)

@main.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('Wylogowano.', 'info')
    return redirect(url_for('main.index'))

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/report', methods=['GET', 'POST'])
@login_required
def report():
    form = BugForm()
    if form.validate_on_submit():
        bug = Bug(
            title=form.title.data,
            description=form.description.data,
            author=current_user)
        db.session.add(bug)      
        db.session.commit()
        flash('Zgłoszenie zostało wysłane!!!.', 'success')
        return redirect(url_for('main.index'))
    return render_template('report_bug.html', form=form)
@main.route('/admin_bugs')
@login_required
def admin_bugs():
    if not current_user.is_admin:
        abort(403)
    bugs = Bug.query.all()
    return render_template('reports.html', bugs=bugs)
@main.route('/admin', methods=['POST'])
@login_required
def admin():
    if not current_user.is_admin:
        abort(403)
    return redirect(url_for('main.admin_bugs'))
@main.route('/delete_bug', methods=['POST'])
def delete_bug():
    bug_id = request.form.get('bug_id')
    bug = Bug.query.get_or_404(bug_id)
    db.session.delete(bug)
    db.session.commit()
    return redirect(url_for('main.admin_bugs'))
@main.route('/zmien_status', methods=['POST'])
def zmien_status():
    bug_id = request.form.get('bug_id')
    new_status = request.form.get('status')
    bug = Bug.query.get_or_404(bug_id)
    bug.status = new_status 
    db.session.commit() 
    return redirect(url_for('main.admin_bugs'))