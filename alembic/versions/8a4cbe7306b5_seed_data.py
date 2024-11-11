"""Seed data

Revision ID: 8a4cbe7306b5
Revises: c5972fcbaa30
Create Date: 2024-11-11 23:38:39.766249

"""
from typing import Sequence, Union
import seed

from alembic import op
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = '8a4cbe7306b5'
down_revision: Union[str, None] = 'c5972fcbaa30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()
    # Execute the query to check if the specific revision exists
    result = connection.execute(text("SELECT version_num FROM alembic_version WHERE version_num = :revision"),
                             {"revision": revision})

    # Check if result has a value
    if result.fetchone() is not None:
        print("Current revision is already executed:", revision)
        return

    # Apply the seed data if no existing row was found
    seed.seed_data()


def downgrade() -> None:
    pass
