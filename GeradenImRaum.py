#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Stützvektor der ersten Gleichung:")
a1 = float(input("a1: "))
a2 = float(input("a2: "))
a3 = float(input("a3: "))
print("Richtungsvektor der ersten Gleichung:")
b1 = float(input("b1: "))
b2 = float(input("b2: "))
b3 = float(input("b3: "))

print("Stützvektor der zweiten Gleichung:")
c1 = float(input("c1: "))
c2 = float(input("c2: "))
c3 = float(input("c3: "))
print("Richtungsvektor der zweiten Gleichung:")
d1 = float(input("d1: "))
d2 = float(input("d2: "))
d3 = float(input("d3: "))

if((b1/d1)==(b2/d2)==(b3/d3)):
    s=(c1-a1)/b1
    if(a2+s*b2==c2 and a3+s*b3==c3):
        print("s=" + str(s) + "\nin I:   " + "a1+s*b1=" + str(a1+s*b1) + "\nin II:  " + "a2+s*b2=" + str(a2+s*b2) + "\nin III: " + "a3+s*b3=" + str(a3+s*b3))
        print("Die Geraden sind identisch.")
    else:
        print("s=" + str(s) + "\nin I:   " + "a1+s*b1=" + str(a1+s*b1) + "\nin II:  " + "a2+s*b2=" + str(a2+s*b2) + "\nin III: " + "a3+s*b3=" + str(a3+s*b3))
        print("Die Geraden sind echt parallel.")
else:
    print("Die Geraden sind nicht parallel.")
