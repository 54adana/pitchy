"""changes in password field

Revision ID: 2add9fadf7e2
Revises: 95f98d9a516d
Create Date: 2019-11-27 15:18:52.569157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2add9fadf7e2'
down_revision = '95f98d9a516d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
