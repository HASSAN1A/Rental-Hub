from flask import render_template,abort,request,redirect,url_for,flash
from . import rental_hub
from flask_login import login_required,current_user
from ..models import User,Article,Comment
from .forms import UpdateProfile,CommentForm
from .. import db,photos
from ..requests import get_quotes


@rental_hub.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes=get_quotes()
    articles=Article.get_all_articles()
    popular=Article.query.order_by(Article.article_upvotes.desc()).limit(3).all()
    return render_template('index.html',quotes=quotes,articles=articles,popular=popular)


@rental_hub.route('/profile/<username>')
@login_required
def profile(username):

    '''
    View profile page function that returns the profile details of the current user logged in
    '''
    user = User.query.filter_by(username = username).first()
    
    if user is None:
        abort(404)
 
    return render_template("profile/profile.html", user = user)



@rental_hub.route('/profile/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        flash('User bio updated')

        return redirect(url_for('rental_hub.profile',username=user.username))


    return render_template('profile/update.html',user=user,form =form)



@rental_hub.route('/profile/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

        flash('User pic updated')
        
    return redirect(url_for('rental_hub.update_profile',username=username))  