"""empty message

Revision ID: 32a97401b350
Revises: 2b4ab7eefbb9
Create Date: 2022-02-06 00:59:52.707259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32a97401b350'
down_revision = '2b4ab7eefbb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
