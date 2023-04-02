class Student:
  
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

  
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

  
    def rate_lecturer(self, lecturer, course, rate):
          if isinstance(lecturer,
                      Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
              if course in lecturer.rates:
                  lecturer.rates[course] += [rate]
              else:
                  lecturer.rates[course] = [rate]
          else:
              return 'Ошибка'
              
      
    def mid_grade(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return f"{mid_sum / len(self.grades.values()):.2f}"

          
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания: {self.mid_grade()}\n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

      
    def __lt__(self, student):
        return self.mid_grade() < student.mid_grade()

      
class Mentor:
  
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):

    def mid_grade(self):
        mid_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return f"{mid_sum / len(self.rates.values()):.2f}"

  
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.mid_grade()}\n'
        return res

  
    def __lt__(self, lecturer):
        return self.mid_grade() < lecturer.mid_grade()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

def st_grades(st_list, course):
    mid_sum = 0
    counter = 0
    for st in st_list:
        if course in st.grades.keys():
            st_sum = 0
            for grades in st.grades[course]:
                st_sum += grades
            st_mid = st_sum / len(st.grades[course])   
            mid_sum += st_mid  
            counter += 1
    if mid_sum == 0:
        return 'Нет оценок!'
    else:
        return f'{mid_sum / counter:.2f}'
        
      
def lect_rates(lect_list, course):
    mid_sum = 0
    counter = 0
    for lect in lect_list:
        if course in lect.rates.keys():
            lect_sum = 0
            for rates in lect.rates[course]:
                lect_sum += rates
            lect_mid = lect_sum / len(lect.rates[course])
            mid_sum += lect_mid
            counter += 1
    if mid_sum == 0:
        return 'Нет оценок!'
    else:
        return f'{mid_sum / counter:.2f}' 
                 
  
first_student = Student('Rick', 'Eman', 'Male')
first_student.courses_in_progress += ['Enter course']
first_student.courses_in_progress += ['GIT']
first_student.courses_in_progress += ['Python']

second_student = Student('Donna', 'Morrow', 'Female')
second_student.courses_in_progress += ['Enter course']
second_student.courses_in_progress += ['GIT']
second_student.courses_in_progress += ['Python']

 
first_reviewer = Reviewer('Tomas', 'Rurk')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Max', 'Lorin')
second_reviewer.courses_attached += ['Enter course']
second_reviewer.courses_attached += ['GIT'] 

first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 10)

second_reviewer.rate_hw(first_student, 'GIT', 10)
second_reviewer.rate_hw(first_student, 'GIT', 9)
second_reviewer.rate_hw(second_student, 'GIT', 10)
second_reviewer.rate_hw(second_student, 'GIT', 9)    

second_reviewer.rate_hw(first_student, 'Enter course', 10)
second_reviewer.rate_hw(first_student, 'Enter course', 8)
second_reviewer.rate_hw(second_student, 'Enter course', 9)
second_reviewer.rate_hw(second_student, 'Enter course', 10)

first_lecturer = Lecturer('John', 'Colins')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('David', 'Lorins')
second_lecturer.courses_attached += ['Enter course']
second_lecturer.courses_attached += ['GIT']

first_student.finished_courses += ['Enter course']
first_student.courses_in_progress.remove('Enter course')
first_student.finished_courses += ['GIT']
first_student.courses_in_progress.remove('GIT')
first_student.rate_lecturer(second_lecturer, 'Enter course', 7)
first_student.rate_lecturer(second_lecturer, 'GIT', 10)
first_student.rate_lecturer(second_lecturer, 'GIT', 9)
first_student.rate_lecturer(second_lecturer, 'GIT', 9)

second_student.finished_courses += ['Enter course']
second_student.courses_in_progress.remove('Enter course')
second_student.rate_lecturer(second_lecturer, 'Enter course', 8)
second_student.finished_courses += ['Python']
second_student.courses_in_progress.remove('Python')
second_student.rate_lecturer(first_lecturer, 'Python', 9)
second_student.rate_lecturer(first_lecturer, 'Python', 10)
second_student.rate_lecturer(first_lecturer, 'Python', 8)

print(first_reviewer)
print(second_reviewer)

print(first_lecturer)
print(second_lecturer)

if first_lecturer > second_lecturer:
    print("Выше оценили первого лектора! \n")
else:
    print("Выше оценили второго лектора! \n")
  
print(first_student)
print(second_student)

if first_student > second_student:
    print("Первый студент учится лучше! \n")
else:
    print("Второй студент учится лучше! \n")
  

st_list = [first_student, second_student]

print(f'Средняя оценка у студентов на курсе "Python": {st_grades(st_list, "Python")}')
print(f'Средняя оценка у студентов на курсе "GIT": {st_grades(st_list, "GIT")}')
print(f'Средняя оценка у студентов на курсе "Enter course": {st_grades(st_list, "Enter course")}\n')


lect_list = [first_lecturer, second_lecturer]

print(f'Средняя оценка у лекторов на курсе "Python": {lect_rates(lect_list, "Python")}')
print(f'Средняя оценка у лукторов на курсе "GIT": {lect_rates(lect_list, "GIT")}')
print(f'Средняя оценка у лекторов на курсе "Enter course": {lect_rates(lect_list, "Enter course")}')
