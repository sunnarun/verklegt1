class EmployeeManagementUI():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2" or user_input == "3":
            print(''' ___________________________________________''')
            print('''|       NaN Air - Employee management       |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Create employee                       |''')
            print('''| (2) Get employee data                     |''')
            print('''| (3) Update employee                       |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input()
            self.get_employee_info()
    
    def get_employee_info(self):
        self.role = self.get_role()
        self.ssn = input("Enter SSN: ")
        self.name = input("Enter name: ")
        self.rank = input("Enter rank: ")
        self.address = input("Enter address: ")
        self.phone_no = input("Enter phone number: ")
        if self.role == "Pilot":
            self.license = input("Enter license: ")
        else:
            self.license = "N/A"
        self.display_info()

    def display_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|  NaN Air - Employee successfully created  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| SSN: {:37}|'''.format(self.ssn))
        print('''| Name: {:36}|'''.format(self.name))
        print('''| Role: {:36}|'''.format(self.role))
        print('''| Rank: {:36}|'''.format(self.rank))
        print('''| Address: {:33}|'''.format(self.address))
        print('''| Phone number: {:28}|'''.format(self.phone_no))
        print('''| License: {:33}|'''.format(self.license))
        print('''|                                           |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Create another employee               |''')
        print('''| (2) Go back to home page                  |''')
        print('''| (3) Edit                                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
    
    def create_employee(self):
        pass
        self.employee = Employee(self.ssn, self.name, self.role, self.rank, self.address, self.phone_no, self.license)
        return self.employee
    
    def get_role(self):
        print()
        print(''' ___________________________________________''')
        print('''|         NaN Air - Create employee         |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Pilot                                 |''')
        print('''| (2) Cabincrew                             |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input()
        self.role = ""
        if user_input == "1":
            self.role = "Pilot"
        elif user_input == "2":
            self.role = "Cabincrew"
        return self.role

a = EmployeeManagementUI()
a.renderMenu()