import random
import pyperclip


def func():
    x = 4
    return 0


s = ""
for i in range(500):
    a = random.randint(-10, 10)
    s += str(a)
    s += " "
    s = ""


for i in range(499):
    l = ["+", "-", "*"]
    a = random.randint(0, 1)
    s += l[a]
    s += " "


pyperclip.copy(s)
