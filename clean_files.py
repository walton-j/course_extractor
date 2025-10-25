# Regex File
import re
import pandas as pd
import numpy as np

filename = 'EngMgt.txt'

def clean_text(filename)
    with open(filename, 'r') as f:
        lines = f.readlines()

    nonempty = [line for line in lines if line.strip() != '']

    with open(filename, 'w') as f:
        f.writelines(nonempty)
