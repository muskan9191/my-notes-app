from datetime import datetime
from uuid import uuid4

from database.mongodb import db


def add_notes_method(notes, user):
    try:
        data = {
            "id": str(uuid4()),
            "createdDate": datetime.now(),
            "createdBy": user["sub"],
            **notes
        }
        id = data.get("id")
        db.notes.insert_one(data)
        return {
            "status": True,
            "data": {"id": id},
            "message":"Notes data added successfully",
            "status_code": 201
        }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }


def get_notes_method(id, user):
    try:
        notes = db.notes.find_one({"id":id, "createdBy": user["sub"]}, {"_id": 0})
        if notes:
            return {
                "status": True,
                "data": notes,
                "message":"Notes details fetched successfully",
                "status_code": 200
            }
        else:
            return {
                "status": False,
                "data": None,
                "message":"Notes data not found",
                "status_code": 404
            }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }


def get_all_notes_method(user):
    try:
        notes = list(db.notes.find({"createdBy": user["sub"]}, {"_id": 0}))
        if notes:
            return {
                "status": True,
                "data": notes,
                "message":"Notes fetched successfully",
                "status_code": 200
            }
        else:
            return {
                "status": False,
                "data": [],
                "message":"No Notes found",
                "status_code": 404
            }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }


def update_notes_method(id, notes, user):
    try:
        notes_response = db.notes.find_one({"id":id, "createdBy": user["sub"]}, {"_id": 0})
        if not notes_response:
            return {
                "status": False,
                "data": None,
                "message":"Notes not found",
                "status_code": 404
            }
        notes["modifiedDate"] = datetime.now()
        notes["modifiedBy"] = user["sub"]
        update_response = db.notes.update_one(
            {"id":id},
            {"$set": notes}
        )
        if update_response and update_response.modified_count > 0:
            notes = db.notes.find_one({"id":id}, {"_id": 0})
            return {
                "status": True,
                "data": notes,
                "message":"Notes data updated successfully",
                "status_code": 200
            }
        else:
            return {
                "status": False,
                "data": None,
                "message":"Failed to update notes data",
                "status_code": 200
            }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }
    

def delete_notes_method(id, user):
    try:
        notes = db.notes.find_one({"id":id, "createdBy": user["sub"]}, {"_id": 0})
        if not notes:
            return {
                "status": False,
                "data": None,
                "message":"Notes not found",
                "status_code": 404
            }
        delete_response = db.notes.delete_one(
            {"id":id}
        )
        if delete_response and delete_response.deleted_count:
            return {
                "status": True,
                "data": None,
                "message":"Notes data deleted successfully",
                "status_code": 200
            }
        else:
            return {
                "status": False,
                "data": None,
                "message": "Failed to delete notes data",
                "status_code": 200
            }
    except Exception as e:
        return {
            "status": False,
            "data": None,
            "message": str(e),
            "status_code": 500
        }