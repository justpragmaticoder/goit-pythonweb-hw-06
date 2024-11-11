# Import the Config and Engine from the app's config file
from config import ALEMBIC_DATABASE_URL
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import models  # Import models so Alembic can find them

# this is the Alembic Config object, which provides access to values within the .ini file
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Replace the sqlalchemy.url value with the one from config.py
config.set_main_option("sqlalchemy.url", ALEMBIC_DATABASE_URL)

target_metadata = models.Base.metadata  # Use your Base metadata for Alembic

def run_migrations_offline():
    context.configure(
        url=ALEMBIC_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()