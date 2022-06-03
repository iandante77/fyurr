"""empty message

Revision ID: 3da75d28f995
Revises: aa387e8802a1
Create Date: 2022-06-02 09:09:25.151917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3da75d28f995'
down_revision = 'aa387e8802a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artists', sa.Column('web', sa.String(length=120), nullable=True))
    op.add_column('Artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artists', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venues', sa.Column('web', sa.String(length=120), nullable=True))
    op.add_column('Venues', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venues', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venues', 'seeking_description')
    op.drop_column('Venues', 'seeking_talent')
    op.drop_column('Venues', 'web')
    op.drop_column('Artists', 'seeking_description')
    op.drop_column('Artists', 'seeking_venue')
    op.drop_column('Artists', 'web')
    # ### end Alembic commands ###
