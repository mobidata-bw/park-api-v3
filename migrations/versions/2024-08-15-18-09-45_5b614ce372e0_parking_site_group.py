"""parking site group

Revision ID: 5b614ce372e0
Revises: 0c34a8561ddb
Create Date: 2024-08-15 18:09:45.727361

"""

import sqlalchemy as sa
import sqlalchemy_utc
from alembic import op

# revision identifiers, used by Alembic.
revision = '5b614ce372e0'
down_revision = '0c34a8561ddb'
branch_labels = None
depends_on = None

old_parking_site_types: list[str] = [
    'ON_STREET',
    'OFF_STREET_PARKING_GROUND',
    'UNDERGROUND',
    'CAR_PARK',
    'GENERIC_BIKE',
    'WALL_LOOPS',
    'SAFE_WALL_LOOPS',
    'STANDS',
    'LOCKERS',
    'SHED',
    'TWO_TIER',
    'BUILDING',
    'FLOOR',
    'OTHER',
]

new_parking_site_types: list[str] = [
    'ON_STREET',
    'OFF_STREET_PARKING_GROUND',
    'UNDERGROUND',
    'CAR_PARK',
    'GENERIC_BIKE',
    'WALL_LOOPS',
    'SAFE_WALL_LOOPS',
    'STANDS',
    'LOCKERS',
    'SHED',
    'TWO_TIER',
    'BUILDING',
    'FLOOR',
    'LOCKBOX',
    'OTHER',
]


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'parking_site_group',
        sa.Column('source_id', sa.BigInteger(), nullable=False),
        sa.Column('original_uid', sa.String(length=256), nullable=False),
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('created_at', sqlalchemy_utc.sqltypes.UtcDateTime(timezone=True), nullable=False),
        sa.Column('modified_at', sqlalchemy_utc.sqltypes.UtcDateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['source_id'], ['source.id'], name=op.f('fk_parking_site_group_source_id')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_parking_site_group')),
    )
    with op.batch_alter_table('parking_site_group', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_parking_site_group_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_parking_site_group_modified_at'), ['modified_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_parking_site_group_original_uid'), ['original_uid'], unique=False)
        batch_op.create_index('ix_parking_site_group_source_original_uid', ['source_id', 'original_uid'], unique=True)

    # Prepare enums for Postgresql
    engine_name = op.get_bind().engine.name
    if engine_name == 'postgresql':
        op.execute('ALTER TYPE parkingsitetype RENAME TO _parkingsitetype')
        sa.Enum(
            *new_parking_site_types,
            name='parkingsitetype',
        ).create(op.get_bind())
        op.execute('ALTER TABLE parking_site ALTER COLUMN type type parkingsitetype using type::text::parkingsitetype;')
        sa.Enum(*old_parking_site_types, name='_parkingsitetype').drop(op.get_bind())

    with op.batch_alter_table('parking_site', schema=None) as batch_op:
        batch_op.alter_column(
            'type',
            existing_type=sa.Enum(*old_parking_site_types, name='parkingsitetype'),
            type_=sa.Enum(*new_parking_site_types, name='parkingsitetype'),
            existing_nullable=True,
        )
        batch_op.add_column(sa.Column('parking_site_group_id', sa.BigInteger(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f('fk_parking_site_parking_site_group_id'), 'parking_site_group', ['parking_site_group_id'], ['id']
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TYPE parkingsitetype RENAME TO _parkingsitetype')
    sa.Enum(*old_parking_site_types, name='parkingsitetype').create(op.get_bind())
    op.execute('ALTER TABLE parking_site ALTER COLUMN type type parkingsitetype using type::text::parkingsitetype;')
    sa.Enum(*new_parking_site_types, name='_parkingsitetype').drop(op.get_bind())

    with op.batch_alter_table('parking_site', schema=None) as batch_op:
        batch_op.alter_column(
            'type',
            existing_type=sa.Enum(*new_parking_site_types, name='parkingsitetype'),
            type_=sa.Enum(*old_parking_site_types, name='parkingsitetype'),
            existing_nullable=True,
        )
        batch_op.drop_constraint(batch_op.f('fk_parking_site_parking_site_group_id'), type_='foreignkey')
        batch_op.drop_column('parking_site_group_id')

    with op.batch_alter_table('parking_site_group', schema=None) as batch_op:
        batch_op.drop_index('ix_parking_site_group_source_original_uid')
        batch_op.drop_index(batch_op.f('ix_parking_site_group_original_uid'))
        batch_op.drop_index(batch_op.f('ix_parking_site_group_modified_at'))
        batch_op.drop_index(batch_op.f('ix_parking_site_group_created_at'))

    op.drop_table('parking_site_group')
    # ### end Alembic commands ###