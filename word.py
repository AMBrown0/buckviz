# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:47:22 2020

@author: andy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import median, mean
import json, urllib.request
import sys
from pathlib import Path


from docx import Document


dataFolder=Path(r"C:\\Users\\Andy.JIVEDIVE\\OneDrive - University of Buckingham\\Notes\\2020-05-22")

filename="test.docx"
dataFile= dataFolder / filename

document = Document(dataFile)
all_paras = document.paragraphs
for para in all_paras:
    print(para.text)
    print("-------")