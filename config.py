from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:567234@postgres:5432/rest_app"

ALEMBIC_DATABASE_URL = f"postgresql+psycopg2://postgres:567234@localhost:5432/rest_app"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_overflow=5)
alembic_engine = create_engine(ALEMBIC_DATABASE_URL, echo=True, max_overflow=5)
