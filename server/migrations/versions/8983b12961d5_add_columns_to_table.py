"""add columns to table

Revision ID: 8983b12961d5
Revises: 67f5d67aea55
Create Date: 2024-01-25 23:21:06.885505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8983b12961d5'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###