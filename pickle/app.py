from flask import Flask, request, make_response, redirect, render_template
import pickle
import base64
import codecs

app = Flask(__name__)

@app.route('/')
def index():
    notes = request.cookies.get('notes')
    if notes:
        all_notes = pickle.loads(base64.b64decode(notes))
        return render_template('index.html', notes=all_notes)
    else:
        all_notes = []
        return render_template('index.html')

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'GET':
        return redirect('/')
    else:
        notes = request.cookies.get('notes')
        if notes:
            all_notes = pickle.loads(base64.b64decode(notes))
        else:
            all_notes = []
        all_notes.append(request.form['note'])

        notes_str = base64.b64encode(pickle.dumps(all_notes)).decode('utf-8')
        
        resp = make_response(redirect('/'))
        resp.set_cookie('notes', notes_str)
        return resp

app.run(host="0.0.0.0")
