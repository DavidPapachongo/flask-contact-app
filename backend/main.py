
from flask import render_template, request, url_for, redirect, flash, Blueprint
from sqlalchemy.exc import DataError
from flask_login import login_required, current_user
from models import Contacts
from __init__ import create_app
from __init__ import db

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    data = Contacts.query.filter(Contacts.user_id == current_user.id).all()
    return render_template('index.html', contacts=data)


@main.route('/add_contact', methods=['POST'])
@login_required
def add_contact():
    try:
        if request.method == 'POST':
            fullname = request.form['fullname']
            phone = request.form['phone']
            email = request.form['email']
            user_id = current_user.id
            data = Contacts(fullname, phone, email, user_id)
            db.session.add(data)
            db.session.commit()
            flash('Contact Added successfully')

            return redirect(url_for('main.index'))
    except DataError:

        flash('Fill The Form')
        return redirect(url_for('main.index'))


@main.route('/edit/<id>')
@login_required
def edit_contact(id):
    data = Contacts.query.filter(Contacts.id == id).one()
    return render_template('edit_contact.html', contact=data)


@main.route('/update/<id>', methods=['POST'])
@login_required
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        up_data = Contacts.query.filter(Contacts.id == id).one()
        up_data.fullname = fullname
        up_data.phone = phone
        up_data.email = email
        db.session.commit()
        flash('Contact Updated successfully')
        return redirect(url_for('main.index'))


@main.route('/delete/<id>')
@login_required
def delete_contact(id):
    Contacts.query.filter(Contacts.id == id).delete()
    db.session.commit()
    flash('Contact Removed successfully')
    return redirect(url_for('main.index'))


