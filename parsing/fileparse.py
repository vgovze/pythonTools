import chardet
from itertools import islice

def GetFileLen(file):
    """Count the number of lines in a file.

    Args:
        file (str): path to file.

    Returns:
        int: line count.
    """
    count = 0
    for i in open(file, "rb"):
        count += 1
    return count

def ParseFile(file, lparsefunc, *args, start=1, end=-1, **kwargs):
    """Parse file and return a list of outputs produced by lparsefunc.
        *args and **kwargs are used by lparsefunc.

    Args:
        file (str): path to file.
        lparsefunc (function): function that parses a string and generates
            desired output from data in a line. If output of lparsefunc is
            None, the line is omitted. If errors occur while parsing the
            line, the line is omitted and the line number is stored.
        start (int, optional): Start line. Defaults to first line.
        end (int, optional): End line. Defaults to last line.

    Returns:
        tuple: tuple of objects returned by lparsefunc.
        tuple: tuple of faulty line line numbers.
    """

    # figure out encoding.
    with open(file, "rb") as f:
        encoding = chardet.detect(f.read(10000000)).get("encoding")

    if end == -1:
        end = GetFileLen(file)
    
    data = ()
    faulty = ()
    with open(file, "r", encoding=encoding) as f:
        for i, line in enumerate(islice(f, start-1, end), start=start):
            try:
                object = lparsefunc(line, *args, **kwargs)
                if object is not None:
                    data += (object,)
            except Exception as error:
                print("Error parsing line", i, "in file", file)
                print(f"Error message: {error}")
                faulty += (i,)
    return data, faulty