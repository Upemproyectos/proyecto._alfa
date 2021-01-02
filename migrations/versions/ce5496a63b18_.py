"""empty message

Revision ID: ce5496a63b18
Revises: 977564b82cb7
Create Date: 2021-01-01 22:27:52.954571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce5496a63b18'
down_revision = '977564b82cb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('frutas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.Column('nombre', sa.String(length=255), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('costo', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('frutas')
    # ### end Alembic commands ###
