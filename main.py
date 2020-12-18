# Module Maker
# Reads from a json file of modules and generates both latex and html code for copy pasting.
# Designed December 2020 by Joe Manlove
# Version 1.0 completed 12/11/2020, latex is properly generated in file.
# Version 1.0.1 12/18/2020 better filepaths in preparation for html


import json
from module import Module

# JSON resources
# https://realpython.com/python-json/
# https://www.w3schools.com/js/js_json_syntax.asp
# https://stackoverflow.com/questions/28325994/how-are-multiple-objects-in-a-single-json-file-separated
# https://stackoverflow.com/questions/26068291/use-json-data-to-initialize-an-object-in-python

import os
# path to directory containing script
PATH = os.path.dirname(__file__) + '/'

INPUT_FILE_NAME = "linear_algebra.json"
INPUT_FILE_PATH = PATH + INPUT_FILE_NAME
OUTPUT_NAME = INPUT_FILE_NAME.replace(".json", '')
HTML_OUTPUT_PATH = PATH + OUTPUT_NAME + '.html'
TEX_OUTPUT_PATH = PATH + OUTPUT_NAME + '.tex'


# collect module information from json file
with open(INPUT_FILE_PATH, "r") as read_file:
    data = json.load(read_file)


with open(TEX_OUTPUT_PATH, 'w') as file:
    print("% Start of code generated using module_maker.py\n", file=file)
    i = 1
    for datum in data:
        # print(datum)
        module = Module(**datum)
        module.latex(file, i)
        i += 1
