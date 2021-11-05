def dict_separator(a_dict):
    """dates, vals = dict_separator(a_dict)"""    
    dates = []
    vals = []
    for key, value in a_dict.items():
        dates.append(key)
        vals.append(value)
    return dates, vals