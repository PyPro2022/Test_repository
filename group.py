from faker import Faker

from random import randint

from student import Student, studs, grades


class Group:

    def __init__(self, name, st_list=None):
        if st_list is None:
            st_list = []
        self.group_name = name
        self.st_list = st_list

    def add_student(self, student):
        if isinstance(student, Student):
            return self.st_list.append(student)
        else:
            raise TypeError('Only Student class objects allowed!!')

    def display_group(self):
        print(f'Group: {self.group_name}')
        for i in range(len(self.st_list)):
            print(f'    {i+1}. {self.st_list[i]}')

    def get_student(self, st_name):
        return [f'{self.st_list.index(student)+1}. {student}' for student in self.st_list
                if st_name in student.__dict__.values()]

    def populate_group(self, num_of_studs):
        for i in range(num_of_studs):
            self.add_student(Student(Faker().first_name(),
                                     Faker().last_name(),
                                     [randint(60, 100) for _ in range(randint(0,10))]))

"""--------------------------------------------------------------------------------"""
# #БЛОК ПРОВЕРОК
"""--------------------------------------------------------------------------------"""
#

g1 = Group('Brython Advanced')

# Добавляем студентов
for student in studs:
    g1.add_student(student)
#
# Создадим парочку с похожими именами:
g1.add_student(Student('Foo', 'Far', grades=grades))


# print( '>>>>>>Проверка display<<<<<')
g1.display_group()

# Получаем инфо по нужному студенту
print(g1.get_student("Foo"))
print(g1.get_student("Bar"))


#Проверка if-else "заглушки" в методе add_student():

# g2 = Group('TestGroup')
# g2.add_student('Ivan')
# g2.add_student(g1)

# Проверка метода populate_group
# g2.populate_group(10)
# g2.display_group()
