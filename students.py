class Student():
    def __init__(self, age, name, classroom) :
        self.age = age
        self.name = name
        self.classroom = classroom
    
    def getAverage(self, score1, score2, score3) :
        self.average = (score1 + score2 + score3)/3
        return self.average
    
student1 = Student(12, "David", "Biology")
score1 = int(input("Please enter your first test score - "))
score2 = int(input("Please enter your second test score - "))
score3 = int(input("Please enter your third test score - "))
average = student1.getAverage(score1,score2,score3)
print(int(average))

    