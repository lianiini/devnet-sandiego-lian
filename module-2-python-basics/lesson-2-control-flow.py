"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: San Diego, Lian Nicole F.
Date: Spetember 29, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

if else is a condition in coding, it checks whether the condition is true and runs the code under that condition.
in simpler english it can be compared to "if the user says yes then do this, else, if the user says no then do that instead, else tell the user what they said is invalid"
it check if each condition, in this case, the user's response, is met, and if it is met, it does what is under that, if all conditions are not met, it proceeds to else

============================================
KEY VOCABULARY
============================================
- condition: the block of code added after if/elif/else
- if / elif / else: the words used for if else block before the condition
- comparison operator: has different kinds 
    ==  | equals
    !=  | not equals
    <   | less than
    <=  | less than or equal to
    >   | greater than
    >=  | greater than or equal to
- boolean expression: evaluates whether the expression is True or False
- elif: the expression used if you need to check more than 1 condition before else

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
user = "yes"

if user == "yes":
    print("do this")
elif user == "no":
    print("do that")
else:
    print("invalid response")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

the indention of the results to be ran when the codition is true, it can be confusing especially when if else conditions become nested

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]

its similar to match case expressions
"""
