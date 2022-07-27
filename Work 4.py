class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_of_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        for unpacking in list(best_student.grades.values()):
            average_mark = sum(unpacking)/len(unpacking)

        in_progress = ', '.join(best_student.courses_in_progress)
        finished_courses = ', '.join(best_student.finished_courses)
        students = (f'Студенты:\nИмя: {self.name}\nФамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {round(average_mark, 2)}\n'
                    f'Курсы в процессе изучения: {in_progress}\nЗавершенные курсы: {best_student.finished_courses}')
        return students


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):
        for unpacking in list(cool_lecturer.grades.values()):
            average_mark = sum(unpacking)/len(unpacking)

        lecturers = (f'Лекторы:\nИмя: {self.name}\n'
                     f'Фамилия: {self.surname}\nСредняя оценка за лекции: {round(average_mark, 2)}')
        return lecturers


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        rewiewers = f'Ревьюеры:\nИмя: {self.name}\nФамилия: {self.surname}'
        return rewiewers


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student = Student('111', '222', '333')

best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']


cool_lecturer = Lecturer('Ivan', 'Ivanov')
cool_lecturer.courses_attached += ['Python']


cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'JS', 10)
cool_reviewer.rate_hw(best_student, 'JS', 8)
cool_reviewer.rate_hw(best_student, 'JS', 10)


best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 9)
best_student.rate_of_lecturer(cool_lecturer,'Python', 10)
best_student.rate_of_lecturer(cool_lecturer,'Python', 8)
best_student.rate_of_lecturer(cool_lecturer,'JS', 7)


def student():
    for key in cool_lecturer.grades.keys():
        for unpacking in list(cool_lecturer.grades.values()):
            average_mark_lecturer = sum(unpacking) / len(unpacking)
            average_mark_lecturer = round(average_mark_lecturer, 2)
    print(f'Средняя оценка у студентов по курсу {key}: {average_mark_lecturer}')


def lecturer():
    for key in best_student.grades.keys():
        for unpacking in list(best_student.grades.values()):
            average_mark_student = sum(unpacking) / len(unpacking)
            average_mark_student = round(average_mark_student, 2)
    print(f'Средняя оценка лекторов по курсу {key}: {average_mark_student}')


student()
lecturer()