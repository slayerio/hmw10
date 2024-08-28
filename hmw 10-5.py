def remove_key_from_dict(dictionary: dict):
    """
    Removes the last key-value,
    """
    dictionary.popitem()


def clear_all(dictionary: dict):
    """
    clears all the items in the dict
    """
    dictionary.clear()


# both func changes the outside dict within them
a = {'x': 1, 'y': 2, 'c': 3}
remove_key_from_dict(a)
print(a)
clear_all(a)
print(a)