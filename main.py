from flask import Flask, render_template
from data import db_session
from data.users import Department
from data.users import Jobs
from data.users import User
from data.db_session import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    global_init('db/blogs1.db')
    db_sess = create_session()
    ids = []
    leaders = []
    for job in db_sess.query(Jobs).all():
        ids.append(job.team_leader)
    jobs = db_sess.query(Jobs).filter()
    for i in ids:
        for user in db_sess.query(User).all():
            if user.id == i:
                leaders.append(f"{user.surname} {user.name}")
    print(leaders)
    return render_template("base.html", jobs=jobs, leaders=leaders)


if __name__ == '__main__':
    app.run(debug=True)
