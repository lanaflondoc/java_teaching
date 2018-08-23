#!/usr/bin/env python3
import os
import yaml
import nbformat as nbf
from render_quiz import render_quiz

init_cell_template_folder="templates/init_cell"
quiz_template_folder="quiz"
nb = nbf.v4.new_notebook()


init_cell_template_lists=sorted([file  for path, subdirs, files in os.walk(init_cell_template_folder) for file in files])
nb['cells']=[]
for template in init_cell_template_lists:
    with open(os.path.join(init_cell_template_folder,template),"r") as f:
        code=f.read()
        cell=nbf.v4.new_code_cell(code)
        cell.metadata["init_cell"]=True
        nb['cells'].append(cell)
        

quiz_template_lists=sorted([file  for path, subdirs, files in os.walk(quiz_template_folder) for file in files])
for template in quiz_template_lists:
    with open(os.path.join(quiz_template_folder,template),"r") as f:
        data=yaml.load(f.read())
        for quiz_item in data:
            code=render_quiz(quiz_item)
            cell=nbf.v4.new_code_cell(code)
            nb['cells'].append(cell)



text = """\
# My first automatic Jupyter Notebook
This is an auto-generated notebook."""
code = """\
%pylab inline
hist(normal(size=2000), bins=50);"""
nb['cells'].append(               nbf.v4.new_markdown_cell(text))
nb['cells'].append(               nbf.v4.new_code_cell(code))


nbf.write(nb, 'test.ipynb')
