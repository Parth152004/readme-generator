from flask import Flask, render_template, redirect, request
import shutil

app = Flask(__name__)


@app.route('/')
def Home():

    return render_template('index.html')


@app.post('/add-element/<type>')
def AddElement(type):
    if type == "title":
        text = request.form.get('title')
        with open('row_readme.txt', 'a+') as f:
            f.write("# " + text + '\n\n')
            f.close()

    if type == "sub-title":
        text = request.form.get('sub-title')
        with open('row_readme.txt', 'a+') as f:
            f.write("## " + text + '\n\n')
            f.close()

    return redirect('/')

@app.route('/generate-readme')
def GenerateReadMe():

    shutil.copy('row_readme.txt', 'yourreadme.md')
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)