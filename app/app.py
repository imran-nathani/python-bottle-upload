from bottle import Bottle, run, response, request, redirect, template, get, post, error, route
from bottle import TEMPLATE_PATH, static_file

app = Bottle()

TEMPLATE_PATH.insert(0, './app/views')

@error(404)
def error404(error):
    return template('header') + template('404') + template('footer')



@app.get('/')
def index():
    return template('header') + template('upload') + template('footer')

@app.post('/')
def do_upload(): 
    redirect("/done")

@app.get('/done')
def done():
    return template('header') + template('done') + template('footer')
    
run(app, host='0.0.0.0', port=8080, reloader=True, debug=True)