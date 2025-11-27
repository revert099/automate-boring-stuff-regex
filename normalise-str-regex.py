"""
    Write a function that takes a string and does the same thing as the strip() method.
    If no other arguments are passed other than the string, then whitespace characters will be removed from the start and end of the string.
    If a second argument is provided, then it will be used as the set of characters to be removed from the start and end of the string.
"""
import re

def normalise_string_regex(arg_str: str, regex_args: str="") -> str:
    """
    Normalises a string regex determining on a regex argument.

    Args:
        input_string (str): The input string regex.
        regex_args (str, optional): The regex argument. Defaults to "".

    Returns:
        str: The normalised string regex.
    """
    if regex_args == "":
        # No arg given - remove leading and trailing whitespace characters
        updated_string = re.sub(r'^\s+|\s+$', '', arg_str)
    else:
        # regex_args were given, escape input string 
        pattern = re.compile(regex_args) # create pattern from regex_args
        updated_string = pattern.sub('', arg_str) # remove characters matching pattern from start and end

    return updated_string

print(normalise_string_regex(" Hello, Worlds! "))
print(normalise_string_regex(" ...Hello, Worlds!!!... ", r'[.!]'))
    
    