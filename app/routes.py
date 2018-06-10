from app import app 
from flask import render_template
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user ={'username':'Shakir'}
    posts= [

        {
            'author':{'username':'john'},
            'body':'this is good idea'
        },
        {
            'author':{'username':'mary'},
            'body':'Great idea to aquire Github By Microsoft'
        }
    ]
    return render_template('index.html',user=user,posts=posts)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='sign In',form=form)



