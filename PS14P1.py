class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

    def calculateBonus(self, bonusRate):
        return self.salary * bonusRate


def main():
    # Test Employee class
    employee1 = Employee("John Doe", 50000)
    employee1.displayEmployee()
    bonus = employee1.calculateBonus(0.1)
    print("Bonus: ", bonus)

if __name__ == "__main__":
    main()