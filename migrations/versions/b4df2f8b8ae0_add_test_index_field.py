"""Add test index field

Revision ID: b4df2f8b8ae0
Revises: 383eac3634aa
Create Date: 2017-01-01 22:32:59.404644

"""

# revision identifiers, used by Alembic.
revision = 'b4df2f8b8ae0'
down_revision = '383eac3634aa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('test_index', sa.Integer(), nullable=True))

    ### The following isn't a part of this migration since it is a very long query to execute. It doesn't really have to block the installation, so it should be done manually after the installation

    #op.execute('update test set test_index = subquery.test_index from (select id, row_number() over (partition by session_id order by session_id asc, start_time asc) as test_index from test) as subquery where test.id = subquery.id and test.test_index is NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'test_index')
    # ### end Alembic commands ###
