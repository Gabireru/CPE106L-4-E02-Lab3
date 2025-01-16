#PostLab1

"""
 Add three methods to the Student class (in the file student.py) that compare two Student objects.
 One method should test for equality.
 A second method should test for less than.
 The third method should test for greater than or equal to.
 In each case, the method returns the result of the comparison of the two students’ names.
 Include a main function that tests all of the comparison operators. (LO: 10.2)
"""

"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
               
    def __eq__(self,other):
        return self.getAverage() == other.getAverage()
    def __lt__(self,other):
        return self.getAverage() < other.getAverage()
    def __ge__(self,other):
        return self.getAverage() >= other.getAverage()

def main():
    """A simple test."""
    student1 = Student("Ken", 3)
    student2 = Student("Takakura", 3)
    
    """Title:"""
    print("Welcome to the Grade Checker Program!")
    print("Below are the Students' grades and comparisons. \n")
    
    print("--------------------")
    """Setting Student Scores:"""
    """Student 1"""
    student1.setScore(1, 100)
    student1.setScore(2, 87)
    student1.setScore(3, 96)
    print(student1)
    
    """Student 2"""
    student2.setScore(1, 80)
    student2.setScore(2, 91)
    student2.setScore(3, 74)
    print(student2)
    print("--------------------")

    print("\nComparing Students...")
    
    print("--------------------")
    print("Student1 == Student2:", student1 == student2)
    print("Student1 < Student2:", student1 < student2)
    print("Student2 >= Student3:", student1 >= student2)
    print("--------------------")


if __name__ == "__main__":
    main()

