"""max height

Revision ID: ccd3da2086d3
Revises: a951c44669b8
Create Date: 2023-12-11 09:26:47.894699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd3da2086d3'
down_revision = 'a951c44669b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_site', schema=None) as batch_op:
        batch_op.add_column(sa.Column('max_height', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_site', schema=None) as batch_op:
        batch_op.drop_column('max_height')

    # ### end Alembic commands ###