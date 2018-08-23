#!/usr/bin/env python3
import os
import yaml
import nbformat as nbf
from render_quiz import render_quiz

init_cell_template_folder="templates/init_cell"
quiz_template_folder="quiz"


quiz_template_lists=sorted([file  for path, subdirs, files in os.walk(quiz_template_folder) for file in files])
for template in quiz_template_lists:
    nb = nbf.v4.new_notebook()
    init_cell_template_lists=sorted([file  for path, subdirs, files in os.walk(init_cell_template_folder) for file in files])
    nb['cells']=[]
    for template_init_cell in init_cell_template_lists:
        with open(os.path.join(init_cell_template_folder,template_init_cell),"r") as f:
            code=f.read()
            cell=nbf.v4.new_code_cell(code)
            cell.metadata["init_cell"]=True
            nb['cells'].append(cell)
    with open(os.path.join(quiz_template_folder,template),"r") as f:
        data=yaml.load(f.read())
        for quiz_item in data:
            code=render_quiz(quiz_item)
            cell=nbf.v4.new_code_cell(code)
            cell.metadata["init_cell"]=True
            nb['cells'].append(cell)
    nbf.write(nb, os.path.join('output',template[:-5]+".ipynb"))
