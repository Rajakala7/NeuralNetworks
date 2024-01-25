class Employee:
    num_employees = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        Employee.num_employees += 1

    def average_salary(self):
        total_salary = sum(emp.salary for emp in self)
        return total_salary / len(self) if len(self) > 0 else 0
class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, hours_worked):
        super().__init__(name, family, salary, department)
        self.hours_worked = hours_worked
e1 = Employee ("Rajkala", "Family1", 80000, "HR")
e2 = Employee ("Rjk", "Family2", 55000, "IT")
e3 = Employee ("Kala", "Family3", 25000, "Operations")

full_time_employee = FulltimeEmployee ("Rajji", "Family4", 60000, "Developer", 70)
print(f"Number of Employees: {Employee.num_employees}")
emp_list = {e1, e2, e3, full_time_employee}
average_salary = Employee.average_salary(emp_list)
print(f"Average Salary: ${average_salary}")

print(f"{full_time_employee.name} works in {full_time_employee.department} department and works {full_time_employee.hours_worked} hours per week.")