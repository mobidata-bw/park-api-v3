"""photo url, duplicate id

Revision ID: 9ad8cd0f3b0d
Revises: c4f85305ddee
Create Date: 2024-05-14 06:46:51.653360

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9ad8cd0f3b0d'
down_revision = 'c4f85305ddee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_site', schema=None) as batch_op:
        batch_op.add_column(sa.Column('duplicate_of_parking_site_id', sa.BigInteger(), nullable=True))
        batch_op.add_column(sa.Column('photo_url', sa.String(length=4096), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f('fk_parking_site_duplicate_of_parking_site_id'), 'parking_site', ['duplicate_of_parking_site_id'], ['id']
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_site', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_parking_site_duplicate_of_parking_site_id'), type_='foreignkey')
        batch_op.drop_column('photo_url')
        batch_op.drop_column('duplicate_of_parking_site_id')

    # ### end Alembic commands ###
