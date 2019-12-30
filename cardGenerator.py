#!/usr/bin/env python3

import datetime
import random

print("Введите ваши подпись:")
signature = input()
print("Cколько человек поздравляем? (введите число)")
quantity = input()
quantityPerson = ["Вас", "Вам"]
signaturePrefix = ["С уважением ", "Искренне Ваш ", "С любовью "]
wish = ["исключительно хорошим", "абсалютно выдающимся", "годом Ваших свершений"]

if int(quantity) == 1:
    print("Введите Имя (отчество и фамилия - опционально)")
    name = input()
    names = name
else:
    print("Поздравляем нескольких")
    for i in range(int(quantity)):
        print("Введите " + str(i + 1) + " Имя (отчество и фамилия - опционально)")
        name = input()
        try:
            names
        except NameError:
            names = name
        else:
            names = names + " и " + name

now = datetime.datetime.now()
newYear = str(now.year + 1)
message = names \
          + " поздравляю " \
          + quantityPerson[0] \
          + " с наступающим Новым " \
          + newYear \
          + " годом!\nЖелаю " \
          + quantityPerson[1] \
          + " всего самого наилучшего в наступающем году\nПусть Новый " \
          + newYear \
          + " Год будет " \
          + random.choice(wish) \
          + "!\n    " \
          + random.choice(signaturePrefix) \
          + signature

print(message)
