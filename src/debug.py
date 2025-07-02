import pyperclip

def clip_debug():
    try:
        pyperclip.copy("Hello clipboard")
        print("pyperclip debug Success!")
    except pyperclip.PyperclipException as e:
        print("pyperclip debug Failure, qq", e)
