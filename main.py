# Module Maker
# Reads from a json file of modules and generates both latex and html code for copy pasting.
# Designed December 2020 by Joe Manlove
# Version 1.0 completed 12/11/2020, latex is properly generated in file.
# Version 1.0.2 completed 12/18/2020, html is properly generated in file


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

# change the input file name variable to the json you'd like to generate from
INPUT_FILE_NAME = "differential_equations/differential_equations_sp20.json"
# INPUT_FILE_NAME = "linear_algebra/linear_algebra_sp20.json"
INPUT_FILE_PATH = os.path.join(PATH, INPUT_FILE_NAME)

# removes the json extension
OUTPUT_NAME = INPUT_FILE_NAME.replace(".json", '')

HTML_OUTPUT_PATH = PATH + OUTPUT_NAME + '.html'
TEX_OUTPUT_PATH = PATH + OUTPUT_NAME + '.tex'


# collect module information from json file
with open(INPUT_FILE_PATH, "r") as read_file:
    data = json.load(read_file)


with open(TEX_OUTPUT_PATH, 'w') as file:
    print("% Start of code generated using Learning Module Creator\n", file=file)
    i = 1
    for datum in data:
        # print(datum)
        module = Module(**datum)
        module.latex(file, i)
        i += 1
    print("% End of code generated using Learning Module Creator\n", file=file)


# single file generation
with open(HTML_OUTPUT_PATH, 'w') as file:
    # this is an HTML comment.
    print("<!-- Start of code generated using Learning Module Creator -->\n", file=file)
    i = 1
    for datum in data:
        # print(datum)
        module = Module(**datum)
        module.html(file, i)
        i += 1
    print("<!-- End of code generated using Learning Module Creator -->\n", file=file)
