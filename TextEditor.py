import os
from model.TextFileEditor import TextFileEditor

test = TextFileEditor("D:/new 2.txt")
test.replace_per_line(' ', '			', 1)
test.output("123.txt")
