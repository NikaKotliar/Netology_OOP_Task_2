course_python = 'Python'
course_android = 'Android'

class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_list.append(self)

    def avrg_grades(self):
        avrg_grades = 0
        for course in self.grades:
            avrg_grades += sum(self.grades[course]) / len(self.grades)
        return round(avrg_grades)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.avrg_grades()} \n' \
              f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
              f'Завершенные курсы: {self.finished_courses} \n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.avrg_grades() < other.avrg_grades()

    def rate_lecturer(self, lecturer_name, course, lecturer_grade):
        if isinstance(lecturer_name, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturer_name.courses_attached:
            if course in lecturer_name.evaluation:
                lecturer_name.evaluation[course] += [lecturer_grade]
            else:
                lecturer_name.evaluation[course] = [lecturer_grade]
        else:
            return 'Mistake'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.evaluation = {}
        self.lecturer_list.append(self)

    def avrg_grades(self):
        avrg_grades = 0
        for course in self.evaluation:
            avrg_grades += sum(self.evaluation[course]) / len(self.evaluation)
        return round(avrg_grades)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self.avrg_grades()} \n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.avrg_grades() < other.avrg_grades()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}\n'\
              f'Оценивает курсы: {self.courses_attached}'
        return res


kirill_neiman = Reviewer('Kirill', 'Neiman')
kirill_neiman.courses_attached += [course_android, course_python, 'C++']


nika_kotlyar = Student('Nika', 'Kotlyar', 'female')
nika_kotlyar.courses_in_progress += [course_python, 'C++']

petr_petrov = Student('Petr', 'Petrov', 'male')
petr_petrov.courses_in_progress += [course_android , 'C++', course_python]
petr_petrov.finished_courses += [course_python]

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += [course_python]

ivan_petrov = Lecturer('Ivan', 'Petrov')
ivan_petrov.courses_attached += ['C++', course_android, course_python]

ivan_sidorov = Lecturer('Ivan', 'Sidorov')
ivan_sidorov.courses_attached += ['C++', course_android, course_python]

kirill_neiman.rate_hw(nika_kotlyar, course_python, 6)
kirill_neiman.rate_hw(nika_kotlyar, 'C++', 8)
kirill_neiman.rate_hw(petr_petrov, course_android, 2)
kirill_neiman.rate_hw(petr_petrov, course_python, 8)
nika_kotlyar.rate_lecturer(ivan_petrov,'C++',10)
petr_petrov.rate_lecturer(ivan_petrov, course_android, 8)
petr_petrov.rate_lecturer(ivan_sidorov, course_android, 4)


def avg_global_hw(students,course):
    global_hw = 0
    counter = 0
    for student in students:
        if course in student.grades:
            global_hw += sum(student.grades[course])
            counter += 1
    return global_hw / counter


def avg_global_rate(lectors,course):
    global_lc_rate = 0
    counter = 0
    for lecturer in lectors:
        if course in lecturer.evaluation:
            global_lc_rate += sum(lecturer.evaluation[course])
            counter += 1
    return global_lc_rate / counter

result_avg_hw = avg_global_hw (Student.student_list, course_python)
print(f'Средняя оценка за домашние задания по курсу {course_python} равна {result_avg_hw}')
print()

result_avg_rate = avg_global_rate (Lecturer.lecturer_list, course_android)
print(f'Средняя оценка за лекции всех лекторов по курсу {course_android} равна {result_avg_rate}')
print()

print(ivan_petrov.evaluation)
print(ivan_petrov)
print(nika_kotlyar.grades)
print(nika_kotlyar)
print(petr_petrov.grades)
print(petr_petrov)
print(nika_kotlyar > petr_petrov)
