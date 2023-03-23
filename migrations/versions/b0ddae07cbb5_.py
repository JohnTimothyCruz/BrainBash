"""empty message

Revision ID: b0ddae07cbb5
Revises:
Create Date: 2023-03-22 15:59:36.114222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0638339b5ba7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('mix_type', sa.String(), nullable=False),
    sa.Column('visibility', sa.Boolean(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('headline', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('decks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('objective', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('learners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('mastery', sa.Integer(), nullable=True),
    sa.Column('days_studied', sa.Integer(), nullable=True),
    sa.Column('time_studied', sa.Integer(), nullable=True),
    sa.Column('cards_studied', sa.Integer(), nullable=True),
    sa.Column('permission', sa.String(length=11), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flashcards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deck_id', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(length=250), nullable=False),
    sa.Column('answer', sa.String(length=250), nullable=False),
    sa.Column('question_image', sa.String(), nullable=True),
    sa.Column('answer_image', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['deck_id'], ['decks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flashcards')
    op.drop_table('learners')
    op.drop_table('decks')
    op.drop_table('classes')
    op.drop_table('users')
    # ### end Alembic commands ###
