from app import app 
from flask import render_template
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
            'body':'Great idea to aquire Github'
        }
    ]
    return render_template('index.html',user=user,posts=posts)