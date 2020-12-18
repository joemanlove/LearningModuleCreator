# Module Maker
# Reads from a json file of modules and generates both latex and html code for copy pasting.
# Designed December 2020 by Joe Manlove
# Version 1.0 completed 12/11/2020, latex is properly generated in file.
# Version 1.1


import json
from module import Module

# JSON resources
# https://realpython.com/python-json/
# https://www.w3schools.com/js/js_json_syntax.asp
# https://stackoverflow.com/questions/28325994/how-are-multiple-objects-in-a-single-json-file-separated
# https://stackoverflow.com/questions/26068291/use-json-data-to-initialize-an-object-in-python


import os
PATH = os.path.dirname(__file__) + '/'


# collect module information from json file
with open(PATH + "topics.json", "r") as read_file:
    data = json.load(read_file)


with open(PATH + 'modules_by_json.tex', 'w') as file:
    print("% Start of code generated using module_maker.py\n", file=file)
    i = 1
    for datum in data:
        # print(datum)
        module = Module(**datum)
        module.latex(file, i)
        i += 1
