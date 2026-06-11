import json
from pathlib import Path



def save_natas():
    PATH = Path("natas_progress.json")
    file_name = PATH.name

    level = input("Please enter the level: ")
    password = input("Please enter the password for next level: ")
    Lesson = input("Tell us th econcept you leanrt today: ")
    commands = input("Commands used to pass through: ")
    
    if PATH.exists() and PATH.stat().st_size > 0:
        print("Yes")
        with open(file_name, 'r') as f:
            dict = json.load(f)
    else:
        PATH = Path.touch(file_name)
        dict = {}

    dict[level] = {"password_to_next_level": password,
                   "lesson": Lesson,
                   "commands": commands
        } 
    
    with open(file_name, 'w') as f:
            json.dump(dict, f, indent=4)
    return dict


save_natas()
