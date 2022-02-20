"""add a content column

Revision ID: 88cb75a59cc2
Revises: 8cc0cd5a5017
Create Date: 2022-02-20 05:50:25.384861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88cb75a59cc2'
down_revision = '8cc0cd5a5017'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
