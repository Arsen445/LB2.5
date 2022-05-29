#!/usr/bin/env python3
# -- coding: utf-8 --

import math


if __name__ == '__main__':
    t = []
    n = int(input('Введите длину кортежа: '))
    for i in range(n):
        t.append(int(input()))
    t = tuple(t)
    k = 0
    for i in range(len(t)-2):
        print(t[i])
        if t[i+1] > t[i] and t[i+1] > t[i+2]:
            k += 1
            print('Есть, его номер(начинается с 1) = ', i+1, i+2, i+3)
            break
    if k == 0:
        print('Нету')
