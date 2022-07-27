from random import randint


class Student:
   
    def __init__(self, name = "DefaultName", lastname = "DefaultLastname", grades=None):
        if grades is None:
            grades = []
        self.name = name
        self.lastname = lastname
        self.grades = grades
        
    def add_grade(self, grade):
        if isinstance(grade, list):
            self.grades += grade
        else:
            self.grades.append(grade)
        return self.grades

    def get_avr_grade(self):
        try:
            return sum(self.grades)/len(self.grades)
        except ZeroDivisionError:
            return None

    def display(self):
        print(
            f'Summary:\n   Name: {self.name}\n   Lastname: {self.lastname}\n   Grades: {self.grades}\n   '
            f'Average grade: {self.get_avr_grade()}')

    def __str__(self):
        if self.get_avr_grade() is not None:
            return f'{self.name} {self.lastname}, {self.grades}, {self.get_avr_grade():.2f}'
        else:                            # if-else вилку сделал для populate_group, чтобы ср.бал нормально отображался
            return f'{self.name} {self.lastname}, {self.grades}, {self.get_avr_grade()}'


"""--------------------------------------------------------------------------------"""
# #БЛОК ПРОВЕРОК
"""--------------------------------------------------------------------------------"""
# Разные способы задания объектов класса Student

stud0 = Student()
stud1 = Student('Stud1', "Stud1lastname")
stud1.name = 'Brandon'
stud1.lastname = 'Super'
stud2 = Student(name='Victor', lastname='Zaytsev')
# print(stud0.__dict__)
# print(stud1.__dict__)
# print(stud2.__dict__)

# Генератор оценок (grades). Разные способы передачи данных.


grades = [randint(60, 100) for i in range(randint(0,10))]

stud0.add_grade([75, 78, 85, 94, 77])
stud1.add_grade(grades)
stud2.add_grade(grades)
stud0.add_grade(80)
stud1.add_grade(grades[:3])
# print(stud0.__dict__)
# print(stud1.__dict__)
# print(stud2.__dict__)

# print('>>>>>>Проверка геттера среднего балла<<<<<<')
# print(stud0.get_avr_grade())
#
# print( '>>>>>>Проверка display<<<<<')
# stud0.display()
# stud1.display()
# stud2.display()

# Ещё генерим студентов для нужд отладки
stud3 = Student()
# stud3.display()
#
stud4 = Student('Foo', 'Bar', [80,94,99])
# stud4.display()

# Упаковываем всех студентов в список на импорт
studs = [stud0,stud1,stud2,stud3,stud4]

