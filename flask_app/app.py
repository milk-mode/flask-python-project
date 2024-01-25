import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route("/")
def hello():
    return "Welcome"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/error")
def error():
    return render_template("custom_error.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            return redirect(url_for('success', name=name, email=email))
        else:
            return redirect("/error")
    else:
        return render_template("form.html")


@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')

    return render_template("success.html", name=name, email=email)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # post
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect('/list_files')
    # get
    return render_template('upload.html')


@app.route('/list_files')
def list_files():
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('list_files.html', files=uploaded_files)


if __name__ == '__main__':
    app.run(debug=True)
