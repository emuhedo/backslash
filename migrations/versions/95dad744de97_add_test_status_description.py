"""Add test.status_description

Revision ID: 95dad744de97
Revises: 7de4c23aaddd
Create Date: 2017-10-09 13:03:19.677995

"""

# revision identifiers, used by Alembic.
revision = '95dad744de97'
down_revision = '7de4c23aaddd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('status_description', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'status_description')
    # ### end Alembic commands ###
