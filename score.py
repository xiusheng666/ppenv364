#!/usr/bin/env python
# -*- coding:utf8 -*-

score = int(input("please input your score:"))

if score >= 90:
    print("A")
    print("very good")
elif score >= 80:
    print("B")
    print("good")
elif score >= 70:
    print("C")
    print("pass")
else:
    print("D")