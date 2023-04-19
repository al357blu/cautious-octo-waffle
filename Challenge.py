import csv


class ProgramExpenses:
    columns = ['Department', 'BCL', 'Program', '2012']
    year_column = '2012'


    def __init__(self, department, bcl, program, expenses):
        self.department = department
        self.bcl = bcl
        self.program = program
        # self.year = year
        self.expenses = expenses

    def format_expenses(self):
        return '${:,.2f}'.format(self.expenses)

    def from_csv_row(cls, row):
        expenses = int(row[cls.year_column])
        return cls(expenses)


expenses_list = []

with open('../seattle-2012-expenditures.csv') as csv_file:
# The delimeter to specify that the values are separated by a comma
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:

            line_count += 1
        else:
            department = row[0]
            bcl = row[1]
            program = row[2]
            expenses = 0.0
            if row[3] != '':
                expenses = float(row[3])
            program_expenses = ProgramExpenses(department, bcl, program, expenses)

            expenses_list.append(program_expenses)

            line_count =+ 1
    department_expenses = {}

    for year in expenses_list:
        if year.department in department_expenses:
            department_expenses[year.department].append(year.expenses)
        else:
            department_expenses[year.department] = [year.expenses]

print("Department\tTotal Expenses")
print("---------\t--------------")
for department, expenses in department_expenses.items():
    total_expenses = sum(expenses)
    formatted_expenses = '${:,.2f}'.format(total_expenses)
    print(f"{department}\t\t{formatted_expenses}")
