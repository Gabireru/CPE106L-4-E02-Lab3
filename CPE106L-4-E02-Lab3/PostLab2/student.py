#PostLab 2

"""
This exercise assumes that you have completed Programming Exercise 1.
Place several Student objects containing different names into a list and shuffle it.
Then run the sort method with this list and display all of the students’ information. (LO: 10.1, 10.2)

"""

"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

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
    """Create a list for student objects."""
    students = [
        Student("Ken", 3),
        Student("Takakura", 3),
        Student("Marshall", 3),
        Student("Law", 3),
    ]
    
    """Assign random scores to each student."""
    for student in students:
        for i in range(1, 4):
            student.setScore(i, random.randint(50, 100))
            
    """Shuffle the list of students."""
    random.shuffle(students)
    
    """Title:"""
    print("Welcome to the Grade Checker Program!")
    print("Below are the shuffled and sorted list of the students' scores based on average: \n")
    
    """Display the shuffled list:"""
    print("-----------------------------------------")
    print("Shuffled list of students:")
    print("-----------------------------------------")
    for student in students:
        print(student)
        print()

    """Sort the students by their average score"""
    students.sort()
    
    print("-----------------------------------------")
    print("\nSorting list...\n")
    
    """Dsiplay the sorted list:"""
    print("-----------------------------------------")
    print("Sorted list of students by average score:")
    print("-----------------------------------------")
    for student in students:
        print(student)
        print()


if __name__ == "__main__":
    main()
