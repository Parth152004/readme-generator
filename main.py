from flask import Flask, render_template, redirect, request
import shutil

app = Flask(__name__)


@app.route('/')
def Home():

    return render_template('index.html')


@app.post('/add-element/<type>')
def AddElement(type):
    with open('README.md', 'a+') as f:
        if type == "title":
            text = request.form.get('title')
            f.write("# " + text + '\n\n')

        if type == "text":
            text = request.form.get("text")
            f.write(text + '\n\n')

        if type == "sub-title":
            text = request.form.get('sub-title')
            f.write("## " + text + '\n\n')

        if type == "bash":
            text = request.form.get('bash')
            f.write("```bash\n" + text + "\n```\n\n")

        if type == "code-snipate":
            text = request.form.get('code-snipate')
            language = request.form.get('language')
            f.write(f"```{language}\n" + text + "\n```\n\n")

        if type == "link":
            text = request.form.get('display-text')
            link = request.form.get('link')
            f.write(f"[{text}]({link})" + '\n\n')

        f.close()
    return redirect('/')

@app.route('/download-readme')
def DownloadReadMe():

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)