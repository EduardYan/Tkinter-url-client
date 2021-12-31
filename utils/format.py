"""
This module have somes
funtions for format
the url.

"""

from errors.requests import DataInvalid

def format_data_post(data:str) -> dict:
    """
    Format the url for
    make a post request valid. Return
    a dict for make the request
    """

    if '&' not in data:
        raise DataInvalid('The data not is valid. Try again.')

    # gettings partsa for add to dict
    parts = data.split('&')

    data = {}
    for part in parts:
        parts = part.split('=')
        data[f'{parts[0]}'] = parts[1]

    return data
