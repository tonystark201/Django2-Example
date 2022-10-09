# * coding:utf-8 *


Definition = {
    "add_student": {
        "name": {"type": "string", "maxlength": 64, "required": True},
        "phone": {"type": "string", "maxlength": 15, "required": True},
        "teacher_id": {
            "type": "string",
            "regex": "^[0-9a-zA-Z]{22}$",
            "required": True,
        },
        "class_id": {"type": "string", "regex": "^[0-9a-zA-Z]{22}$", "required": True},
    }
}
