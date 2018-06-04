from app import app 

@app.route('/')
@app.route('/index')
def index():
    return "I thought I wanted a career, turns out I just wanted pay checks"
