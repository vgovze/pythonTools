def SplitStrip(str, delim="\t", tofloat=False):
    """Split string at given delimiter and clear the whitespace of each result.
        If tofloat is True, try to convert strings to float.

    Args:
        str (str): the string to parse.
        delim (str, optional): line item delimiter. Defaults to "/t".
        tofloat (bool, optional): convert numeric values to float.
            Defaults to False.

    Returns:
        list : containing strings with floats.
    """
    lst = str.split(delim)
    for i, s in enumerate(lst):
        lst[i] = s.strip()
    if tofloat:
        for i, s in enumerate(lst):
            try:
                lst[i] = float(lst[i])
            except:
                continue
    return lst