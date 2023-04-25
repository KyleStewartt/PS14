class Student:
    def __init__(self, firstName, lastName, districtCode, enrolledCredits):
        self.firstName = firstName
        self.lastName = lastName
        self.districtCode = districtCode
        self.enrolledCredits = enrolledCredits
    def computeTuitionOwed(self):
        if self.districtCode == "I":
            tuitionRate = 250
        else:
            tuitionRate = 500
        return self.enrolledCredits * tuitionRate
def main():
    # Test Student class
    student1 = Student("Jane", "Doe", "I", 15)
    tuitionOwed = student1.computeTuitionOwed()
    print("Tuition Owed: ", tuitionOwed)
if __name__ == "__main__":
    main()