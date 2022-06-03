"""empty message

Revision ID: 96bda304fbae
Revises: a63e36c94b37
Create Date: 2022-06-02 23:06:48.664252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96bda304fbae'
down_revision = 'a63e36c94b37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venue_Id', sa.Integer(), nullable=False))
    op.drop_constraint('shows_venueId_fkey', 'shows', type_='foreignkey')
    op.drop_constraint('shows_artist_id_fkey', 'shows', type_='foreignkey')
    op.create_foreign_key(None, 'shows', 'Venues', ['venue_Id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'shows', 'Artists', ['artist_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('shows', 'venueId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venueId', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.create_foreign_key('shows_artist_id_fkey', 'shows', 'Artists', ['artist_id'], ['id'])
    op.create_foreign_key('shows_venueId_fkey', 'shows', 'Venues', ['venueId'], ['id'])
    op.drop_column('shows', 'venue_Id')
    # ### end Alembic commands ###