from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Columbus,OH',
        'salary': '$100,000,00',
    },
    {
        'id':2,
        'title':'Hacker',
        'location': 'Seattle,WA',
        'salary': '$300,000,00',
    }
]


@app.route("/")
def hello_jovian():
    return render_template('home.html',
                           jobs=JOBS,
                           Company_Name='Yourway Express')


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)