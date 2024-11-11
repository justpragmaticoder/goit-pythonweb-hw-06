from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from config import alembic_engine
from models import Group, Student, Teacher, Subject, Grade

Session = sessionmaker(bind=alembic_engine)
session = Session()

fake = Faker()

def seed_data():
    groups = [Group(name=f"Group {i + 1}") for i in range(3)]
    session.add_all(groups)

    students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(30)]
    session.add_all(students)

    teachers = [Teacher(name=fake.name()) for _ in range(4)]
    session.add_all(teachers)

    subjects = [Subject(name=f"Subject {i + 1}", teacher=random.choice(teachers)) for i in range(5)]
    session.add_all(subjects)

    for student in students:
        for subject in subjects:
            grades = [
                Grade(
                    student=student,
                    subject=subject,
                    grade=random.uniform(2, 5),
                    date_received=fake.date_between(start_date="-1y", end_date="today")
                ) 
                for _ in range(random.randint(10, 20))
            ]
            session.add_all(grades)

    session.commit()
