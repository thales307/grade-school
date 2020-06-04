class School:
    def __init__(self):        
        self.student = {}
        
    def add_student(self, name, grade):
        self.student[name] = grade
        
    def roster(self):
        students = []
        sortedList = sorted(self.student.items())
        for student in sorted(sortedList, key=lambda x: (x[1], x[0])):
            students.append(student[0])
        return students
        
    def grade(self, grade_number):
        gradeStudent = []
        for student in self.student.keys():
            if self.student[student] == grade_number:
                gradeStudent.append(student)
        return sorted(gradeStudent)
