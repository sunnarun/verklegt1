class EmployeeManagement():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2" or user_input == "3":
            print('''+ ----------------------------------------- +''')
            print('''|                  NaN Air                  |''')
            print('''+ ----------------------------------------- + ''')
            print('''| (1) Create employee                       |''')
            print('''| (2) Get employee data                     |''')
            print('''| (3) Update employee                       |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print('''+ ----------------------------------------- +''')
            print()
            user_input = input()