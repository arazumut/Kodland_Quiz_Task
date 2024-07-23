# populate_db.py
from app import app
from models import db, Exam

with app.app_context():
    db.create_all()
    question1 = Exam(
        question="What is AI?", 
        option1="Artificial Intelligence", 
        option2="Artificial Invention", 
        option3="Applied Intelligence", 
        option4="None", 
        answer="Artificial Intelligence"
    )
    db.session.add(question1)
    db.session.commit()
