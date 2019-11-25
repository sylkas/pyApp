from flask import render_template
from hello_world import app
 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posty')
def posts():
    return render_template('posts.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post_id = post_id)
 
@app.route('/omnie')
def about():
    return render_template('about.html')
 
@app.route('/kontakt')
def contact():
    return render_template('contact.html')
 
@app.context_processor
def inject_variables():
    return dict(
        user = {'name': 'SSS'},
        posts = [
        {
            'post_id': 0,
            'title': 'Post numer 0'
        },
        {
            'post_id': 1,
            'title': 'Post numer 1'
        },
        {
            'post_id': 2,
            'title': 'Post numer 2'
        }]
        )