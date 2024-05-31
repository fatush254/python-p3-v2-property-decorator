#!/usr/bin/env python3

from dog import Dog
import ipdb

ipdb.set_trace()


dog = Dog("Fido", "Corgi")


try:
    dog.name = 7  
except ValueError as e:
    print("Caught ValueError:", e)

try:
    dog.breed = "Poodle"  
except ValueError as e:
    print("Caught ValueError:", e)
