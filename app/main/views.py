from flask import render_template,request,redirect,url_for,abort,flash
from .forms import UpdateProfile,PitchForm,CommentForm
from flask_login import login_required,current_user
from . import main
from ..models import User,Pitch,Comment
from .. import db
from .. import db,photos

@main.route('/')
def index():

    return render_template('index.html')

#a dynamic route that will hold profile function
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# creating an update_profile function
#query db to pick a user with the same username we passed
#flask request checks if name photo has been passed into the request
# a path of where the file is stored
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
background-color:#FFCCFF; text-aligbackground-color:#FFCCFF; text-align: center;n: center;
        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# route that will process our form submission
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

#routing for viewing pitches only
@main.route('/pitch', methods=['GET','POST'])
@login_required
def pitch():
    pitch_form = PitchForm()
    pitchform1 = Pitch(name = pitch_form.title.data,description=pitch_form.title.data)
    pitchform1. save_pitch()
    print('wow')
    allpitches = Pitch.query.all()
    print(all)
    return render_template('pitch.html',pitch_form=pitch_form,Pitch=pitch,all=allpitches)


# #routing for pitches and categories
# @main.route('/pitch', methods=['GET','POST'])
# @login_required
# def category():
#     category_form = CategoryForm()
#     categoryform1 = Category(name = category_form.title.data,user=current_user)
#     categoryform1. save_category()
#     print('www')g


# routing for the business category /query the database to give us  a pitch
# if a pitch is found we render the template and pass the pitch as a variable

@main.route('/business', methods=['GET','POST'])
@login_required
def business():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        business = Pitch(category=pitch_form.category.data,title = pitch_form.title.data)
        db.session.add(business)
        db.session.commit()
    business = Pitch.query.all()
    return render_template('business.html',business=business,pitch_form=pitch_form)

#routing for different sales
@main.route('/sales', methods=['GET','POST'])
@login_required
def sales():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        sales = Pitch(category=pitch_form.category.data,title = pitch_form.title.data)
        db.session.add(sales)
        db.session.commit()
    sales = Pitch.query.all()
    return render_template('sales.html',sales=sales,pitch_form=pitch_form)

#routing for different interview
@main.route('/interview', methods=['GET','POST'])
@login_required
def interview():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        interview = Pitch(category=pitch_form.category.data,title = pitch_form.title.data)
        db.session.add(interview)
        db.session.commit()
    interview = Pitch.query.filter_by(category='interview').all()
    return render_template('interview.html',interview=interview,pitch_form=pitch_form)

#routing for comments
@main.route('/comments/<int:id>', methods=['GET','POST'])
@login_required
def comment(id):

    comment_form=CommentForm()
    if comment_form.validate_on_submit():

        new_comment = Comment(description=comment_form.description.data,pitch_id=id,user=current_user)
        db.session.add(new_comment)
        db.session.commit()
    comments = Comment.query.filter_by(pitch_id=id)

    return render_template('comment.html',comments=comments,comment_form=comment_form)
