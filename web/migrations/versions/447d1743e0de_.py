"""empty message

Revision ID: 447d1743e0de
Revises: 3f20a8a72d0a
Create Date: 2016-01-28 10:12:43.616668

"""

# revision identifiers, used by Alembic.
revision = '447d1743e0de'
down_revision = '3f20a8a72d0a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('uuid', sa.String(length=100), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('server', 'uuid')
    ### end Alembic commands ###
