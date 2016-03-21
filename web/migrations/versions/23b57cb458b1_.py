"""empty message

Revision ID: 23b57cb458b1
Revises: e226c50ee645
Create Date: 2016-03-17 13:43:25.664213

"""

# revision identifiers, used by Alembic.
revision = '23b57cb458b1'
down_revision = 'e226c50ee645'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maintenance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('maintenance_name', sa.String(length=50), nullable=True),
    sa.Column('hostname', sa.String(length=50), nullable=True),
    sa.Column('maintenance_time', sa.Integer(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_maintenance_hostname'), 'maintenance', ['hostname'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_maintenance_hostname'), table_name='maintenance')
    op.drop_table('maintenance')
    ### end Alembic commands ###
