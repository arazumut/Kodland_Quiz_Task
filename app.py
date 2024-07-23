from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(100), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    questions = Question.query.all()
    highscore_user = User.query.order_by(User.score.desc()).first()
    highscore = highscore_user.score if highscore_user else 0
    return render_template('index.html', questions=questions, highscore=highscore)

@app.route('/submit', methods=['POST'])
def submit():
    answers = request.form
    score = 0
    total_questions = Question.query.count()
    
    for question_id, user_answer in answers.items():
        if question_id != "username":
            question = Question.query.filter_by(id=int(question_id)).first()
            if question.answer == user_answer:
                score += 1

    username = answers.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        if score > user.score:
            user.score = score
    else:
        new_user = User(username=username, score=score)
        db.session.add(new_user)
    db.session.commit()

    highscore_user = User.query.order_by(User.score.desc()).first()
    highscore = highscore_user.score if highscore_user else 0

    return render_template('result.html', score=score, total_questions=total_questions, highscore=highscore)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
