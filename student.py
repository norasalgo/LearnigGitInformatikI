from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}


    def add_module(self,title):
        self.modules.append(title)
        grade = title.get_grade()
        self.grades[title] = grade

    def get_list_modules(self):
        print("Modules of Student {0:s}".format(self.name))
        for module in self.modules:
            print("\t" + module.title)

    def get_grades(self):
        print("Grades of Student {0:s}".format(self.name))
        for module in self.grades:
           print("\t" + module.title + ": " + str(self.grades[module]))


### test cases ###

me = Student("FirstName LastName")

me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
