from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,PitchingForm,CommentForm
from .. import db,photos


@main.route('/', methods = ['GET','POST'])
def index():
    religion = Pitch.query.filter_by(category='Religion').all()
    sports = Pitch.query.filter_by(category='Sports').all()
    tech = Pitch.query.filter_by(category='Technology').all()

    return render_template('index.html', tech = tech,sports = sports,religion= religion)



@main.route('/sports', methods = ['GET','POST'])
def sports():
    sports = Pitch.query.filter_by(category = 'Sports').all()
    print(sports)


    return render_template('sports.html',sports = sports)

@main.route('/religion')
def religion():
    religion = Pitch.query.filter_by(category = 'Religion').all()
    print(religion)

    return render_template('religion.html',religion= religion)

@main.route('/post', methods = ['GET','POST'])
@login_required
def new_post():
   form = PitchingForm()
   if form.validate_on_submit():
       description = form.description.data
       category = form.category.data
       user = current_user


       new_pitch = Pitch(description = description,category = category,user = user)

       # save pitch
       db.session.add(new_pitch)
       db.session.commit()

       return redirect(url_for('main.index',uname = user.username))

   return render_template('post.html',form = form)

@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form_comment = CommentForm()

    comment = Comment.query.filter_by(pitch_id=id).all()

    if form_comment.validate_on_submit():
        details = form_comment.details.data
        user = current_user
        print(comment)
        new_comment = Comment(details = details,user =user,pitch_id=id)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()



        return redirect(url_for('main.index', uname = user.username))
    return render_template('comments.html',form_comment = form_comment,comment=comment)

# @main.route('/post/up_vote/<int:id>')
# @login_required
# def up_vote(id):
#         post = Pitch.query.filter_by(id=id).first()
#         post.up_vote = post.up_vote +1
#         db.session.add(post)
#         db.session.commit()
#
#         return redirect(url_for('main.index'))


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html',form =form)




@main.route('/user/<uname>/update/pic',methods =['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))