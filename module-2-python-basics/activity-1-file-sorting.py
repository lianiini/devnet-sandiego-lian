"""
Module 2 — Activity: File Sorting with os and shutil
Student: San Diego, Lian Nicole F.
Date: Spetember 29, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

We built a system that automatically sorts files according to their extensions to their respective folders.
This system was built during our laboratory few weeks ago and it isn't fully working as of now. 
It can only make the needed directory as listed in folder list.
Supposedly, the code should sort the files on their respective folder by looping to each file in the path listed but im having errors on that part of my code.


============================================
KEY VOCABULARY
============================================
- os module: an os module is a library that is used to allow python code to interact with the operating system 
- shutil module: shutil module is another library that is used for high level operations on files
- file path: file path is the address of a file inside a computer
- directory: another term for folder

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

imageCount = 0
documentCount = 0
videosCount = 0
othersCount = 0

path_list = []

folder = ["Image", "Document", "Videos", "Others"]

user_path = input("Type a path: ")

if os.path.exists(user_path) is True:
    path_list.append(os.listdir(user_path))
    for list in path_list:
        print(list)

    for i in folder:
        if not os.path.exists(i):
            os.mkdir(os.path.join(user_path, i))

            for file in path_list:
                if os.path.isdir(file) is True:
                    continue
                if file.endswith(".jpg", ".jpeg", ".png", ".gif"):
                    shutil.move(file, i[0])
                    print("hi")
                elif file.endswith(".pdf", ".docx", ".txt", ".pptx"):
                    pass
                elif file.endswith(".mp4", ".mov", ".avi"):
                    pass
                else:
                    pass


        else:
            continue

    # if not os.path.exists(user_path):
    #     print("hi")
    #     # os.path.join(base_dir, "Images")

else:
    print("Path does not exist")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

the specific part i didnt manage to run was checking for the files inside the directory and sorting them.
i think i made a mistake on the if else part as well as on the closing parenthesis used for the list of extensions.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]

something like this could definitely save time, im part of an organization that deals with papers so having an automatic sorter would help me.
also, this concept would be helpful if it can be applied with not just extension but file names.
"""
