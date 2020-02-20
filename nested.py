#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Evan Ochs"

import sys


def is_nested(line):
    """Validate a single input line for correct nesting"""
    openers = ("(", "(*", "[", "{", "<")
    closers = (")", "*)", "]", "}", ">")
    stack = []
    index = 0
    balance = True
    while line:
        current_char = line[0]
        if line.startswith("(*"):
            current_char = "(*"
        elif line.startswith("*)"):
            current_char = "*)"
        index += 1
        line = line[len(current_char):]
        if current_char in openers:
            stack.append(current_char)
        elif current_char in closers:
            if stack[-1] == openers[closers.index(current_char)]:
                stack.pop()
            else:
                balance = False
                break
    if balance and len(stack) == 0:
        return 'YES\n'
    else:
        return 'NO {}\n'.format(index)
    

def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open("input.txt", "r") as read_file:
        with open("output.txt", "w") as write_file:
            readible_line = read_file.readlines()
            for line in readible_line:
                final_output = is_nested(line)
                write_file.write(str(final_output))
                



if __name__ == '__main__':
    main(sys.argv[1:])
