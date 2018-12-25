"""new fields in user model

Revision ID: 94c17bed6c46
Revises: c3358bbef969
Create Date: 2018-12-25 21:47:35.441635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94c17bed6c46'
down_revision = 'c3358bbef969'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
