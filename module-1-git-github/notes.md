# Module 1 — Git & GitHub

**Student:** San Diego, Lian Nicole F.
**Date:** September 27, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]

Git is inside my computer, i installed it. it acts like the permission my mom gives me when i wanna do something.
Github is the cloud storage for codes. Its web based but also have an app. its the thing i wanna do and because i have permission, i was able to do it

---

## Key vocabulary (in your own words)

- repository: a folder in github 
- commit: saving changes
- branch: a separate area to work on but in the same repository
- push / pull: pushing is to give the code to github, pulling is getting the code from github
- pull request: a request to add the work done in a separate branch to the main branch
- merge conflict: when 2 editors changes the same line of code in one project, this error is given

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]

for this activity, i first cloned the repository to my folder in my pc
then i made and switched to a new branch to avoid conflicts with my other works
after making changes on my first file, i added the file to git
i then saved it by using commit and added a descriptive message to identify what i changed
after the commit i pushed to my new branch for the file changes to go to the repository

```
# paste your actual commands here
git clone https://github.com/lianiini/devnet-sandiego-lian.git
git switch -c module-1/notes
git add module-1-git-github\notes.md
git commit -m "answered all required questions"
git push -u origin module-1/notes

```
---

## A mistake I made (or one I want to avoid)

adding way too many remote repository inside my working file, it confuses and messes on pushing

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
