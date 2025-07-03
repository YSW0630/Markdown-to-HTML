# Author: Pacfrog

import sys
import os
import time
import markdown
import pyperclip

import conf
from debug import clip_debug

def basic_check():
    if len(sys.argv) <= 1:
        print("error: Please give me a argument!")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("error: The program only support one argument now, qaq")
        sys.exit(1)

def interact(html):
    print("Copy the converted html file into your clipboard? (default: yes)\n>> ", end='')

    user_input = input().lower()

    if user_input == "yes" or user_input == "":
        # clip_debug()
        pyperclip.copy(html)
        print("Success! the html text is now in your clipboard")
        time.sleep(1)
        print("===============================================")
        print(html)

    elif user_input == "no":
        print(html)

    else:
        print("error: Invalid user input! Please try again")

def main():
    basic_check()

    file_path = sys.argv[1]
    file_path = os.path.abspath(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
    except FileNotFoundError:
        print(f"error: File not found: {file_path}")
        sys.exit(1)

    # Parse
    html = markdown.markdown(md_text)

    interact(html)

main()
