"""parking site history

Revision ID: 0c34a8561ddb
Revises: 9ad8cd0f3b0d
Create Date: 2024-07-28 11:38:03.246492

"""

import sqlalchemy as sa
import sqlalchemy_utc
from alembic import op

# revision identifiers, used by Alembic.
revision = '0c34a8561ddb'
down_revision = '9ad8cd0f3b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'parking_site_history',
        sa.Column('parking_site_id', sa.BigInteger(), nullable=False),
        sa.Column('static_data_updated_at', sqlalchemy_utc.sqltypes.UtcDateTime(timezone=True), nullable=True),
        sa.Column('realtime_data_updated_at', sqlalchemy_utc.sqltypes.UtcDateTime(timezone=True), nullable=True),
        sa.Column(
            'realtime_opening_status',
            sa.Enum('OPEN', 'CLOSED', 'UNKNOWN', name='history_openingstatus'),
            nullable=False,
        ),
        sa.Column('capacity', sa.Integer(), nullable=True),
        sa.Column('capacity_disabled', sa.Integer(), nullable=True),
        sa.Column('capacity_woman', sa.Integer(), nullable=True),
        sa.Column('capacity_family', sa.Integer(), nullable=True),
        sa.Column('capacity_charging', sa.Integer(), nullable=True),
        sa.Column('capacity_carsharing', sa.Integer(), nullable=True),
        sa.Column('capacity_truck', sa.Integer(), nullable=True),
        sa.Column('capacity_bus', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity_disabled', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity_woman', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity_family', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity_charging', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity_carsharing', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity_truck', sa.Integer(), nullable=True),
        sa.Column('realtime_capacity_bus', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity_disabled', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity_woman', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity_family', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity_charging', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity_carsharing', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity_truck', sa.Integer(), nullable=True),
        sa.Column('realtime_free_capacity_bus', sa.Integer(), nullable=True),
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('created_at', sqlalchemy_utc.sqltypes.UtcDateTime(timezone=True), nullable=False),
        sa.Column('modified_at', sqlalchemy_utc.sqltypes.UtcDateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['parking_site_id'],
            ['parking_site.id'],
            name=op.f('fk_parking_site_history_parking_site_id'),
        ),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_parking_site_history')),
        mysql_charset='utf8mb4',
        mysql_collate='utf8mb4_unicode_ci',
    )
    with op.batch_alter_table('parking_site_history', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_parking_site_history_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_parking_site_history_modified_at'), ['modified_at'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parking_site_history', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_parking_site_history_modified_at'))
        batch_op.drop_index(batch_op.f('ix_parking_site_history_created_at'))

    op.drop_table('parking_site_history')
    # ### end Alembic commands ###