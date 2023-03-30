from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()


class Participant(db.Model):
    __tablename__ = "participant_table"


    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, unique=True, nullable=False)
    wish = sa.Column(sa.String, nullable=False)
    group_id = sa.Column(sa.ForeignKey("group_table.id"), nullable=True)
    
    recipient_id = sa.Column(sa.ForeignKey("participant_table.id"), nullable=True)
    recipient = db.relationship(
        'Participant',
        uselist=False,
        remote_side=[id],
        post_update=True
    )

class Group(db.Model):
    __tablename__ = "group_table"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, unique=True, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    participants = db.relationship(Participant)

