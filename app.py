from json import load

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    with open("data/groups.json") as group_file:
        groups = load(group_file)
    return render_template('index.html', groups=groups)

if __name__ == '__main__':
    app.run(debug=True)
