
from functools import reduce
from winreg import REG_NOTIFY_CHANGE_ATTRIBUTES


def avg(array):
    if isinstance(array, list):
        data = {'0': array}
    else:
        data = array
    sum = 0
    count = 0
    for marks in data.values():
        sum += reduce(lambda x,y: x + y, marks, 0)
        count += len(marks)   
    res = sum / count if count > 0 else 0
    return res


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   

    def rate_lection(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res =  f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания:{avg(self.grades)}\n'
        res += f'Курсы в процессе изучения: {self.courses_in_progress}\n'
        res += f'Завершенные курсы: {self.finished_courses}'
        return res
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def print(self):
        print('I\'m Mentor -  ',self.name,self.surname)
        
    def __str__(self):
        res =  f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}'
        return res
 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}
        self.courses_attached = []
 
    def print(self):
        print('I\'m Lecturer -  ',self.name,self.surname)
    
    def __str__(self):
        res =  super().__str__()
        res += f'\nСредняя оценка за лекции: {avg(self.grades)}'
        return res
 
class Reviewer(Mentor):
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def print(self):
         print('I\'m Reviewer -  ',self.name,self.surname)
    
 
 
def __main__():
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    best_student.finished_courses += ['React']
    
    cool_student =  Student('Funky', 'Tunes', 'your_gender')
    cool_student.courses_in_progress += ['React']
    
    cool_mentor = Mentor('Some', 'Buddy')
    
    cool_mentor.print()
    print(cool_mentor)
    
    lecturer1 = Lecturer('Lec1', 'Backend')
    lecturer2 = Lecturer('Lec2', 'FrontEnd')
    
  
    lecturer1.courses_attached += ['Python']
    lecturer2.courses_attached += ['React']
   
    reviewer1 = Reviewer('Rev1', 'Backend')
    reviewer2 = Reviewer('Rev2', 'FrontEnd')
    
    reviewer1.rate_hw(best_student, 'Python', 10)
    reviewer1.rate_hw(best_student, 'Python', 9)
    reviewer2.rate_hw(best_student, 'React', 10)
  
    reviewer1.rate_hw(cool_student, 'Python', 10)
    reviewer2.rate_hw(cool_student, 'React', 9)
    reviewer2.rate_hw(cool_student, 'React', 8)
  
    cool_student.rate_lection(lecturer1, 'Python', 10)
    cool_student.rate_lection(lecturer2, 'React', 10)
    
  
    print(best_student)
    print(cool_student)
    
    
     
    lecturer1.print()
    print(lecturer2)
    reviewer1.print()
    print(reviewer2)
    



__main__()
