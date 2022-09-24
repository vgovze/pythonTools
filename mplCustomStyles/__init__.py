# Functions for accessing the matplotlib style files in the 
# custom mpl_styles folder.
import os

# The matplotlib style extension string.
__FILEEXTENSION__ = ".mplstyle"

# Get this module's absolute path.
__STYLESPATH__ = os.path.abspath(os.path.join(__file__, os.pardir))

# Get the style names.
__STYLES__ = []
for file in os.listdir(__STYLESPATH__):
    if file[-len(__FILEEXTENSION__):] == __FILEEXTENSION__:
        __STYLES__.append(file[:-len(__FILEEXTENSION__)])

def Show():
    """Print available custom styles to the console.
    """
    print(f"Available custom {__FILEEXTENSION__} styles are:")
    for name in __STYLES__:
        print(f"|--> {name}")

def Get(s):
    """Get the absoulte path the custom style file to use.

    Args:
        s (str): the name the custom style. The extension name can be included
            or omitted.

    Raises:
        Exception: if input argument is not a str.
        Exception: if style does not exist.

    Returns:
        str|None: the absolute path to the custom style file if style exists.
    """
    try:
        # Sanity check.
        if not isinstance(s, str):
            raise Exception("Expected a string as an argument "
                            "to the Select() function.")

        if s in __STYLES__:
            return __STYLESPATH__ + f"/{s}" + __FILEEXTENSION__
        elif s[:-len(__FILEEXTENSION__)] in __STYLES__:
            return __STYLESPATH__ + f"/{s}"
        else:
            raise Exception(f"style '{s}' does not exist.\n"
                "For a full list of available styles use the Show() function.")

    except Exception as error:
        print(f"An error occured when searching for styles.")
        print(f"Full error message: {error}")
        return None