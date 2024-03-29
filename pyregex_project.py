'''
This program attempts to match lines of input against a list of regular expressions for each line
the name of the first matching pattern is printed, or unknown if no matching pattern is matched.

when run without any arguments, line will be read from standard input. 
If given a filename, lines will be read from that file.

Patterns - Integers, Real numbers, Addresses, Prices, Phone no, Email add, C identifiers, 
Course Identifiers.
'''

import re,sys

def print_match(string, patterns):
    """
    Iterates over the provided patterns, and prints the name of the first
    pattern that matches the provided string. If no pattern matches, 'unknown'
    is printed.

    Parameters:
      string - the string to match
      patterns - an iterable of tuples, where each tuple contains a regular
                 expression pattern and a name
    """

    for pattern, name in patterns:
        if re.match(pattern, string):
            print(name)
            return

    print('unknown')


def match_strings_from_file(file, patterns):
    """
    Reads each line from the provided file object, strips off the trailing
    newline, and passes the line to print_match() along with the provided
    list of patterns.

    Parameters:
      file - an open file-like object
      patterns - a list of tuples, where each tuple contains a regular
                 expression pattern and a name
    """

    for line in file:
        string = line.rstrip('\n')
        print_match(string, patterns)


def main():
    # TODO - add patterns to this list
    patterns = [
        # (r'^\d+$', 'Integer'),
        (r'^\d+\.\d+$', 'Real number'),
        (r'^\d{1,5}\s?[a-zA-z]+\.?(\s+[A-Za-z]*\.?)*$', 'Address'),
        (r'^\$\d{1,3}(,{1}\d{3})*\.\d{2}', 'Price'),
        (r'^((\+?234)\s?|0)(((7)0)|((8|9)(0|1)))\d{8}', 'Phone Number'),
        (r'^\w+(\.|_|-)?\w*@\w+(\.|-)?(\w*\.?)*(edu|wheeeee)$', 'Email Address'),
        (r'^[A-za-z_][A-za-z0-9]*$', 'C identifier'),
        (r'^[A-Z]{4}-[0-9]{5}-[0-9]{2}', 'Course Identifier')
    ]

    # if a filename is supplied on the command line, read strings from that file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            match_strings_from_file(f, patterns)
    # if no arguments are given, read lines from standard input
    elif len(sys.argv) == 1:
        print('Reading from standard input.')
        print('Enter lines to match, press ctrl+d to exit')
        match_strings_from_file(sys.stdin, patterns)
    # more than 2 arguments is an error
    else:
        usage = 'Usage: {} [<input filename>]'.format(sys.argv[0])
        sys.exit(usage)


main()