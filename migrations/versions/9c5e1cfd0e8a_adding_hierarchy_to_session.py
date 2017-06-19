"""Adding hierarchy to session

Revision ID: 9c5e1cfd0e8a
Revises: ce7eef7a094c
Create Date: 2017-05-17 17:33:15.589024

"""

# revision identifiers, used by Alembic.
revision = '9c5e1cfd0e8a'
down_revision = 'ce7eef7a094c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('parent_logical_id', sa.String(length=256), nullable=True))
    op.create_index(op.f('ix_session_parent_logical_id'), 'session', ['parent_logical_id'], unique=False)
    op.drop_index('ix_session_logical_id', table_name='session')
    op.create_index(op.f('ix_session_logical_id'), 'session', ['logical_id'], unique=True)
    op.create_foreign_key(None, 'session', 'session', ['parent_logical_id'], ['logical_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'session', type_='foreignkey')
    op.drop_index(op.f('ix_session_logical_id'), table_name='session')
    op.create_index('ix_session_logical_id', 'session', ['logical_id'], unique=False)
    op.drop_index(op.f('ix_session_parent_logical_id'), table_name='session')
    op.drop_column('session', 'parent_logical_id')
    # ### end Alembic commands ###