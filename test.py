from employee import Employee

class EmployeeManagementUI():
    def __init__(self):
        self.user_input = "1"

    def renderMenu(self):
        while self.user_input == "1" or self.user_input == "2" or self.user_input == "3":
            print(''' ___________________________________________''')
            print('''|       NaN Air - Employee management       |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
            print('''| (1) Create employee                       |''')
            print('''| (2) Get employee data                     |''')
            print('''| (3) Update employee                       |''')
            print('''|                                           |''')
            print('''| (press "b" for back)                      |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            self.user_input = input()
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
        else:                               # Cabincrew
            self.license = "N/A"
        self.display_info()
        user_input = input("input: ")
        #'''
        if user_input == "2":
            self.display_info_to_edit()
            while user_input == "2":
                user_input_edit = input()
                if user_input_edit == "1":
                    self.ssn = input("Enter SSN: ")
                elif user_input_edit == "2":
                    self.name = input("Enter name: ")
                elif user_input_edit == "3":
                    self.role = self.get_role()
                elif user_input_edit == "4":
                    self.rank = input("Enter rank: ")
                elif user_input_edit == "5":
                    self.address = input("Enter address: ")
                elif user_input_edit == "6":
                    self.phone_no = input("Enter phone number: ")
                if self.role == "Pilot":
                    if user_input_edit == "7":
                        self.license = input("Enter license: ")
                self.display_info()
                user_input = input()
                self.display_info_to_edit()
                #'''
        if user_input == "1":               # Confirm info
            self.print_confirmation()
            self.create_employee()
            user_input = input()
            if user_input == "1":
                self.get_employee_info()


    def display_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|       NaN Air - Review information        |''')
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
        print('''| (1) Confirm                               |''')
        print('''| (2) Edit                                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()

    def display_info_to_edit(self):
        print()
        print(''' ___________________________________________''')
        print('''|        NaN Air - Edit information         |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) SSN: {:33}|'''.format(self.ssn))
        print('''| (2) Name: {:32}|'''.format(self.name))
        print('''| (3) Role: {:32}|'''.format(self.role))
        print('''| (4) Rank: {:32}|'''.format(self.rank))
        print('''| (5) Address: {:29}|'''.format(self.address))
        print('''| (6) Phone number: {:24}|'''.format(self.phone_no))
        if self.role == "Pilot":
            print('''| (7) License: {:29}|'''.format(self.license))
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
    
    def print_confirmation(self):
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Empployee successfullly created!          |''')
        print('''|                                           |''')
        print('''| (1) Create another employee               |''')
        print('''| (2) Go back to home page                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')
    
    def create_employee(self):
        self.employee = Employee(self.ssn, self.name, self.role, self.rank, \
            self.address, self.phone_no, self.license)
        return self.employee
    
    def get_role(self):
        print()
        print(''' ___________________________________________''')
        print('''|           NaN Air - Select role           |''')
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