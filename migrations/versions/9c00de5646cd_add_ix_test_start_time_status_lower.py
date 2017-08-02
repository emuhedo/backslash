"""Add ix_test_start_time_status_lower

Revision ID: 9c00de5646cd
Revises: d5e936a5835e
Create Date: 2017-08-01 14:25:16.846453

"""

# revision identifiers, used by Alembic.
revision = '9c00de5646cd'
down_revision = 'd5e936a5835e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_test_start_time_status_lower', 'test', [sa.text('start_time DESC'), sa.text('lower(status::text)')], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_test_start_time_status_lower')
    # ### end Alembic commands ###