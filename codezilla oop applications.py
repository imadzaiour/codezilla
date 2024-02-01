from datetime import date
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"my name is {self.name} and my age is {self.age}")

    @classmethod 
    def initFromBirthYear(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)


cat_1 = cat("deddoum", 7)
cat_1.describe()
cat_2 = cat.initFromBirthYear("Macha", 2019)
cat_2.describe()