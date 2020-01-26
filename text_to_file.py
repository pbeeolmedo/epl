#!/usr/bin/env python

def text_to_file(txt,mode="a"):
    with open("Output.txt", mode) as text_file:
        print(txt, file=text_file)
        print("writing text to file")