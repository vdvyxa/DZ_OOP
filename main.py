from functools import reduce
from winreg import REG_NOTIFY_CHANGE_ATTRIBUTES


# Функция получения среднего по всему списку/словарю
def avg(array):
    if isinstance(array, list):
        data = {'0': array}
    else:
        data = array
    sum = 0
    count = 0
    for marks in data.values():
        sum += reduce(lambda x, y: x + y, marks, 0)
        count += len(marks)
    res = sum / count if count > 0 else 0
    return res


# Функция подсчета средней оценки студентов за курс
def avg_dz(student_list, course):
    print(student_list)
    grades = []
    for student in student_list:
        grades += student.grades.get(course, [])
    print(grades)
    return avg(grades)


# Функция подсчета средней оценки лекторов за курс
def avg_lector(lector_list, course):
    grades = []
    for lector in lector_list:
        grades += lector.grades.get(course, [])
    return avg(grades)


#################################################
#################################################

# Класс студент STUDENT
class Student:
    def __init__(self, name, surname, gender):
        self.name = name  # имя
        self.surname = surname  # фамилия
        self.gender = gender  # пол
        self.finished_courses = []  # список завершенных курсов
        self.courses_in_progress = []  # список текущих курсов
        self.grades = {}  # словарь оценок {курс - [оценка1, оценка2, ...]}

    # Метод добавления курса, на котором обучается студент
    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    # Метод проставления оценки лектору
    # (только тому, на курс которого подписан)
    def rate_lection(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    # "Магический" метод преобразования класса в строку (для print)
    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания:{avg(self.grades)}\n'
        res += f'Курсы в процессе изучения: {self.courses_in_progress}\n'
        res += f'Завершенные курсы: {self.finished_courses}'
        return res

    # "Магический" метод сравнения (<) двух Student-ов
    # по среднему баллу из словарей grades
    def __lt__(self, other):
        return avg(self.grades) < avg(other.grades)


#################################################
#################################################

# Класс Учитель MENTOR (родительский)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # Вывод на экран информации об объекте
    def print(self):
        print('I\'m Mentor -  ', self.name, self.surname)

    # "Магический" метод преобразования класса в строку (для print)
    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}'
        return res


#################################################
#################################################

# Класс Лектор (наследник от MENTOR)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # словарь оценок {курс - [оценка1, оценка2,...]}
        self.courses_attached = []  # список курсов, которые он ведет

    # Вывод на экран информации об объекте
    def print(self):
        print('I\'m Lecturer -  ', self.name, self.surname)

    # "Магический" метод преобразования класса в строку (для print)
    def __str__(self):
        res = super().__str__()
        res += f'\nСредняя оценка за лекции: {avg(self.grades)}'
        return res

    # "Магический" метод сравнения (<) двух Student-ов
    # по среднему баллу из словарей grades
    def __lt__(self, other):
        return avg(self.grades) < avg(other.grades)


#################################################
#################################################

# Класс Проверяющий (наследник от MENTOR)
class Reviewer(Mentor):

    # Метод проверки ДЗ для студента student
    # по курсу course с выставлением оценки grade
    def rate_hw(self, student, course, grade):
        # проверка, что студент подписан на курс
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        # иначе ошибка
        else:
            return 'Ошибка'

    # Вывод на экран информации об объекте
    def print(self):
        print('I\'m Reviewer -  ', self.name, self.surname)

    # "Магический" метод преобразования класса в строку (для print)
    def __str__(self):
        res = f'I\'m Reviewer\n'
        res += super().__str__()
        return res


#################################################
#################################################

# ОСНОВНАЯ ФУНКЦИЯ - САМА ПРОГРАММА
def __main__():
    # Создание нескольких студентов
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    best_student.finished_courses += ['React']

    cool_student = Student('Funky', 'Tunes', 'your_gender')
    cool_student.courses_in_progress += ['React']

    print('Students')
    print(best_student)
    print(cool_student)

    # Создание нескольких учителей
    cool_mentor = Mentor('Some', 'Buddy')
    cool_mentor.print()
    print('\nMentors')
    print(cool_mentor)

    # Создание нескольких лекторов
    lecturer1 = Lecturer('Lec1', 'Backend')
    lecturer2 = Lecturer('Lec2', 'FrontEnd')
    lecturer1.courses_attached += ['Python']
    lecturer2.courses_attached += ['React']

    print('\nLecturers')
    lecturer1.print()
    print(lecturer1)
    print(lecturer2)

    # Создание нескольких проверяющих
    reviewer1 = Reviewer('Rev1', 'Backend')
    reviewer2 = Reviewer('Rev2', 'FrontEnd')

    reviewer1.rate_hw(best_student, 'Python', 10)
    reviewer1.rate_hw(best_student, 'Python', 9)
    reviewer2.rate_hw(best_student, 'React', 10)

    reviewer1.rate_hw(cool_student, 'Python', 10)
    reviewer2.rate_hw(cool_student, 'React', 9)
    reviewer2.rate_hw(cool_student, 'React', 8)

    print('\nReviewers')
    reviewer1.print()
    print(reviewer1)
    print(reviewer2)

    # оценивание лекторов
    cool_student.rate_lection(lecturer1, 'Python', 10)
    cool_student.rate_lection(lecturer2, 'React', 10)
    best_student.rate_lection(lecturer1, 'Python', 9)

    print('lecturer1 < lecturer2:', lecturer1 < lecturer2)

    print(lecturer1)
    print(lecturer2)

    course = 'Python'
    avg_st = avg_dz([best_student, cool_student], course)
    avg_lec = avg_lector([lecturer1, lecturer2], course)

    print(f'Средняя оценка по курсу {course}:')
    print(f'\tстуденты: {avg_st}')
    print(f'\tлекторы: {avg_lec}')


#################################################
#################################################


__main__()
