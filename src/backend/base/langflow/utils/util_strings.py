from langflow.utils import constants


def truncate_long_strings(data, max_length=None):
    """
    Recursively traverse the dictionary or list and truncate strings longer than max_length.
    """

    if max_length is None:
        max_length = constants.MAX_TEXT_LENGTH

    if max_length < 0 or not isinstance(data, dict | list):
        return data

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str) and len(value) > max_length:
                data[key] = value[:max_length] + "..."
            elif isinstance(value, (dict | list)):
                truncate_long_strings(value, max_length)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, str) and len(item) > max_length:
                data[index] = item[:max_length] + "..."
            elif isinstance(item, (dict | list)):
                truncate_long_strings(item, max_length)

    return data