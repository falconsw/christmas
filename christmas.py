#  file : christmas.py
#  author :  Omer DOGAN <omer_dogan@outlook.com>
#  date : 15.12.2019 02:17

from random import randint
from time import sleep

rand2 = randint(1, 32)


def tree():
    print('\033c')
    for key in range(1, 32, 3):

        rand1 = randint(1, rand2)

        if key == 1:
            char = "$"
        elif rand1 % 4 == 0:
            char = "o"
        elif rand1 % 3 == 0:
            char = "i"
        else:
            char = "*"

        print("{:^33} ".format(char * key))
    print("{:^33} ".format("||||"))
    print("{:^33} ".format("||||"))

    sleep(.75)


while True:
    tree()
