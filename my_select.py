from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models import Student, Grade, Subject, Group, Teacher
from config import alembic_engine

# Set up session factory
Session = sessionmaker(bind=alembic_engine)


# Helper function for executing queries with error handling
def execute_query(query_func, *args, **kwargs):
    """
    Executes a query function with provided arguments and catches any exceptions.

    :param query_func: The query function to execute.
    :param args: Positional arguments to pass to the query function.
    :param kwargs: Keyword arguments to pass to the query function.
    :return: The result of the query if successful; None if an exception occurs.
    """
    session = Session()
    try:
        result = query_func(session, *args, **kwargs)  # Pass session explicitly
        return result
    except Exception as e:
        print(f"Error in {query_func.__name__}: {e}")
        session.rollback()
    finally:
        session.close()


# Query functions with session passed as a parameter
def select_1(session):
    return session.query(Student.name, func.avg(Grade.grade).label('average_grade')) \
        .join(Grade) \
        .group_by(Student.id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .limit(5).all()


def select_2(session, subject_id):
    return session.query(Student.name, func.avg(Grade.grade).label('average_grade')) \
        .join(Grade) \
        .filter(Grade.subject_id == subject_id) \
        .group_by(Student.id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .first()


def select_3(session, group_id, subject_id):
    return session.query(func.avg(Grade.grade).label('average_grade')) \
        .join(Student) \
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id) \
        .scalar()


def select_4(session):
    return session.query(func.avg(Grade.grade).label('average_grade')).scalar()


def select_5(session, teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()


def select_6(session, group_id):
    return session.query(Student.name).filter(Student.group_id == group_id).all()


def select_7(session, group_id, subject_id):
    return session.query(Student.name, Grade.grade) \
        .join(Student) \
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id) \
        .all()


def select_8(session, teacher_id):
    return session.query(func.avg(Grade.grade).label('average_grade')) \
        .join(Subject) \
        .filter(Subject.teacher_id == teacher_id) \
        .scalar()


def select_9(session, student_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).distinct().all()


def select_10(session, student_id, teacher_id):
    return session.query(Subject.name) \
        .join(Grade) \
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id) \
        .distinct().all()


# Execute all selects and log their results
if __name__ == "__main__":
    print("Result of select_1:", execute_query(select_1), '\n')
    print("Result of select_2:", execute_query(select_2, subject_id=1), '\n')
    print("Result of select_3:", execute_query(select_3, group_id=1, subject_id=1), '\n')
    print("Result of select_4:", execute_query(select_4), '\n')
    print("Result of select_5:", execute_query(select_5, teacher_id=1), '\n')
    print("Result of select_6:", execute_query(select_6, group_id=1), '\n')
    print("Result of select_7:", execute_query(select_7, group_id=1, subject_id=1), '\n')
    print("Result of select_8:", execute_query(select_8, teacher_id=1), '\n')
    print("Result of select_9:", execute_query(select_9, student_id=1), '\n')
    print("Result of select_10:", execute_query(select_10, student_id=1, teacher_id=1), '\n')