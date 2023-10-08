def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    current = obj

    try:
        for k in keys:
            current = current[k]
        return current
    except (KeyError, TypeError):
        return None

# Example usage:
nested_object = {
    "a": {
        "b": {
            "c": "d"
        }
    },
    "x": {
        "y": {
            "z": "a"
        }
    }
}

key1 = "a/b/c"
key2 = "x/y/z"

value1 = get_value_from_nested_object(nested_object, key1)
value2 = get_value_from_nested_object(nested_object, key2)

print(value1)  
print(value2) 
