# -*- coding: utf-8 -*-

from extraction import *
from preprocess import *
from BART_model import *
import sys


if len(sys.argv) < 2:
    print("Usage: python script.py <text>")
    sys.exit(1)

text = ' '.join(sys.argv[1:])  # Concaténer tous les arguments après le nom du script

txt=clean_text(text)
txt=supp_phrases(txt)
x=generate_summary(txt)
print("  ",x.encode('utf-8').decode(sys.stdout.encoding))
