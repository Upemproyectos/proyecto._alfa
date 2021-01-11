"""empty message

Revision ID: 31104bd9c96d
Revises: 50cb1724b31f
Create Date: 2021-01-04 20:08:07.346213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31104bd9c96d'
down_revision = '50cb1724b31f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('frutas_id', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('cantidad', sa.String(length=255), nullable=True),
    sa.Column('costo', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['frutas_id'], ['frutas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('listado')
    # ### end Alembic commands ###