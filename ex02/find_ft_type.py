def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if obj_type == list:
        print(f"List : {obj_type}")
    elif obj_type == tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type == set:
        print(f"Set : {obj_type}")
    elif obj_type == dict:
        print(f"Dict : {obj_type}")
    elif obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    elif obj_type == int:
        print("Type not found")
    else:
        print(f"{obj_type.__name__.capitalize()} : {obj_type}")
    return 42
