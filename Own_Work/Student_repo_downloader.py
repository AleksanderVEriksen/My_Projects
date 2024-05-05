# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:06:50 2024

@author: eriks
"""
# In[0]: 
import git # pip install gitpython
text_file = open("students.txt", "r").read().split("\n")

working_dir = "text"
github_link = "text"

for student in text_file:   
    try:
        git.Repo.clone_from(f'{github_link}labs-{student}.git', f'{working_dir}labs-{student}')
    except git.exc.GitCommandError as expection:
            print(f"Error occured for {student} as {expection}")
    SET = True
    if SET:
        current_lab = 15  # Lab to be graded
    import os
    import shutil
    for x in range(1, current_lab):
        dirpath = os.path.join(f'C:{working_dir}labs-{student}', f'lab{x}')
        if os.path.exists(dirpath) and os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
