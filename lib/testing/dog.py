#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    
    # Getter and setter for name
    def get_attr(self):
        print("This is the dog name")
        return self._name

    def set_attr(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}")
            return self._name
        else:
            print("Name must be string between 1 and 25 characters.")

    
    name = property(get_attr, set_attr)

    # Getter and setter for name
    def getb_attr(self):
        print("This is the dog breed")
        return self._breed

    def setb_attr(self, breed):
        if breed != APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            print(f"The dog is of breed {breed}")
            return self._breed

    breed = property(getb_attr, setb_attr)

Gith = Dog("Gith", "tiff")
print(Gith.name)
# print(pluto.breed)

Gith.name = "Moh"
print(Gith.set_attr)
Gith.breed = "bosco"
print(Gith.breed)

    