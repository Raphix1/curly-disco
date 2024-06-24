class Animal:
    def make_sound(self, s):
        return s

class Horse(Animal):
    pass

pony = Horse()
print(pony.make_sound("igo-go"))