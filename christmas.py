#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:13:39 2017

@author: jil20
"""

import sys

def get_names_from_user():
    print("Please enter names seperated by comma")
    name = sys.stdin.readline()
    names = name.strip().split(",")
    return names
    
def create_a_personalised_greetings_message(person_name):
    return "Hello "+person_name+", happy Christmas!"

def write_message_to_file(filename, message):
    with open(filename,'w') as f:
        if f.write(message):
            return True
        else:
            return False
        
if __name__ == "__main__":
    
    names = get_names_from_user()
    messages = []
    for name in names:
        message = create_a_personalised_greetings_message(name)
        messages.append(message+"\n")
    messages = ''.join(messages)
    if write_message_to_file("a.txt", messages):
        print("Successfully wrote into file!")
    else:
        print("Failed to write file")