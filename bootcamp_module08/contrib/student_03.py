def reverse_string(string):
    """Reverses a string

    Parameters
    ----------
    string : str
        The string to reverse

    Returns
    -------
    reversed_string: str
        the 'string' with all characters in reversed order

    """
    reversed_string = ""
    for ii in range(len(string)-1, -1, -1):
        reversed_string += string[ii]
    return reversed_string
