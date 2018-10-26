class Student(object):
    count: int = 0

    def __init__(self, name):
        self.name = name
        self.__score = 0
        Student.count += 1

    def get_score(self): return self.__score

    def set_score(self, value: float):

        if value <= 200 and value >= 0:
            self.__score = value

    score = property(get_score, set_score)


lolita = Student("lolita")
print(lolita.name)
print(lolita.get_score())
lolita.set_score(190)
print(lolita.get_score())
lolita.set_score(90)
lolita.score = 96.5
print(lolita.get_score())

if hasattr(lolita, 'sex'):
    lolita.sex = "female"
else:
    print("%s has no attribute of sex" % lolita.name)
    setattr(lolita, 'sex', "female")

print(getattr(lolita, 'sex', 404))

print(Student.count)

tom = Student("Tom")

if hasattr(tom, 'sex'):
    tom.sex = "male"
else:
    print("%s has no attribute of sex" %tom.name)
    setattr(tom, 'sex', "male")

print(tom.count)

print(getattr(tom, 'sex', 404))