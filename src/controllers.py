from flask import Blueprint, request, abort
from .models import Group, Participant, db
from sqlalchemy import and_

import random

bp = Blueprint("group", __name__)

@bp.post("/group")
def add_group():
    request.get_json(force=True)
    data = request.json

    if data.get("name") in [None, ""]:
        abort(400)
    
    group = Group(name=data["name"], description=data.get("description"))
    db.session.add(group)
    db.session.commit()

    return {"id": group.id}, 200    

@bp.get("/group")
def get_all_groups_short_info():
    groups = db.session.execute(db.select(Group)).scalars()

    return [
        {
            "id": group.id,
            "name": group.name,
            "description": group.description
        } for group in groups
    ]

@bp.get("/group/<id>")
def get_group_info(id):
    group = db.session.execute(db.select(Group).where(Group.id == id)).scalar()
    res = {
        "id": group.id,
        "name": group.name,
        "description": group.description,
        "participants": [
            {
                "id": participant.id,
                "name": participant.name,
                "wish": participant.wish,
                "recipient": {
                    "id": participant.recipient.id,
                    "name": participant.recipient.name,
                    "wish": participant.recipient.wish
                } if participant.recipient else None
            } for participant in group.participants 
        ] 
    } 

    return res
    
@bp.put("/group/<id>")
def edit_group(id):
    request.get_json(force=True)
    data = request.json

    if data.get("name") in [None, ""]:
        abort(400)
    
    group = db.session.execute(db.select(Group).where(Group.id == id)).scalar()
    group.name = data["name"]
    group.description = data.get("description")
    db.session.commit()

    return {"id": group.id}, 200   

@bp.delete("/group/<id>")
def delete_group(id):
    db.session.execute(db.delete(Group).where(Group.id == id))

    return {}, 200

@bp.post("/group/<id>/participant")
def add_participant_to_group(id):
    request.get_json(force=True)
    data = request.json

    if data.get("name") in [None, ""]:
        abort(400)
    
    group = db.session.execute(db.select(Group).where(Group.id == id)).scalar()
    participant = Participant(name=data.get("name"), wish=data.get("wish"))
    group.participants.append(participant)
    db.session.commit()

    return {"id": participant.id}, 200   


@bp.delete("/group/<group_id>/participant/<participant_id>")
def delete_participant_from_group(group_id, participant_id):    
    group = db.session.execute(db.select(Group).where(Group.id == group_id)).scalar()
    participant = db.session.execute(db.select(Participant).where(Participant.id == participant_id)).scalar()
    group.participants.remove(participant)
    db.session.commit()

    return {}, 200   

@bp.post("/group/<id>/toss")
def make_toss(id):
    group = db.session.execute(db.select(Group).where(Group.id == id)).scalar()
    n_participants = len(group.participants)

    if n_participants < 3:
        abort(409)

    random.shuffle(group.participants)

    for index in range(n_participants):
        if index == n_participants - 1:
            group.participants[index].recipient = group.participants[0]
        else:
            group.participants[index].recipient = group.participants[index + 1]

    for part in group.participants:
        print(part.recipient.id, part.id)

    db.session.commit()

    return {}, 200


@bp.get("/group/<group_id>/participant/<participant_id>/recipient")
def get_participant_recipient(group_id, participant_id):
    participant = db.session.execute(db.select(Participant).where(and_(Participant.id == participant_id, Participant.group_id == group_id))).scalar()
    recipient = participant.recipient

    return {
        "id": recipient.id,
        "name": recipient.name,
        "wish": recipient.wish
    }

@bp.errorhandler(Exception)
def handle_common_exception():
    return {"message": "Неизвестная ошибка."}, 500