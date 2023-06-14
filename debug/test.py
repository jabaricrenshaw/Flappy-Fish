import re
import pygame
import os

string = '^F.*-.*g$'
dir = os.path.dirname(os.path.abspath(__file__))
r = re.compile(string)
list = list(filter(r.match, os.listdir(dir)))
print(dir + '\\' + list[0])
