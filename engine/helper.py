import os
import re
import time


def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None


def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string



# key events like receive call, stop call, go back
def keyEvent(key_code):
    command =  f'adb shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap event used to tap anywhere on screen
def tapEvents(x, y):
    command =  f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command =  f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)

# To replace space in string with %s for complete message send
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')



# import os
# import re
# import time

# def extract_yt_term(command):
#     pattern = r'play\s+(.+?)\s*(?:on\s+youtube)?$'
#     match = re.search(pattern, command, re.IGNORECASE)
#     return match.group(1) if match else None

# def remove_words(input_string, words_to_remove):
#     if not input_string:
#         return ""
#     words = input_string.split()
#     filtered_words = [word for word in words if word.lower() not in words_to_remove]
#     return ' '.join(filtered_words)

# def adb_command(command, delay=1):
#     os.system(command)
#     time.sleep(delay)

# def keyEvent(key_code):
#     adb_command(f'adb shell input keyevent {key_code}')

# def tapEvents(x, y):
#     adb_command(f'adb shell input tap {x} {y}')

# def adbInput(message):
#     adb_command(f'adb shell input text "{message}"')

# def goback(times=6, key_code=4):
#     for _ in range(times):
#         keyEvent(key_code)

# def replace_spaces_with_percent_s(input_string):
#     return input_string.replace(' ', '%s')
