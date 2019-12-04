#from voyage import Voyage

class VoyageManagementUI():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2":
            print(''' -------------------------------------------''')
            print('''|        NaN Air - Voyage management        |''')
            print(''' ------------------------------------------- ''')
            print('''| (1) Create voyage                         |''')
            print('''| (2) Get voyage data                       |''')
            print('''| (3) Update voyage                         |''')
            print('''|                                           |''')
            print('''| (4) Go back to home page                  |''')
            print(''' -------------------------------------------''')
            print()
            user_input = input()
            if user_input == "1":
                self.get_input()
    
    def get_input(self):
            print(''' -------------------------------------------''')
            print('''|                  NaN Air                  |''')
            print(''' ------------------------------------------- ''')
            print('''| (1) Create new voyage                     |''')
            print('''| (2) Gather crew for voyage                |''')
            print('''| (3) Create destination                    |''')
            print('''|                                           |''')
            print('''| (press "b" for back and "q" to quit)      |''')
            print(''' -------------------------------------------''')        
            print()
            user_input = input()
            if user_input == "3":
                self.get_destination_info()
    
    def get_destination_info(self):
        print()
        print(' _____________________________')
        print("| NaN Air - Enter information |")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ")
        self.country = input(" Enter country: ")
        self.airport = input(" Enter airport: ")
        self.airline = input(" Enter airline: ")
        self.distance = input(" Enter distance: ")
        self.contact_name = input(" Enter contact name: ")  
        self.contact_phone = input(" Enter contact phone: ")
        self.display_info()

    def display_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|        NaN Air - Review information       |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Country: {:33}|'''.format(self.country))
        print('''| Airport: {:33}|'''.format(self.airport))
        print('''| Airline: {:33}|'''.format(self.airline))
        print('''| Distance: {:32}|'''.format(self.distance))
        print('''| Contact name: {:28}|'''.format(self.contact_name))
        print('''| Contact phone: {:27}|'''.format(self.contact_phone))
        print('''|                                           |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Confirm                               |''')
        print('''| (2) Edit                                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input()
        if user_input == '1':
            self.create_destination()
        elif user_input == '2':
            self.edit_info()

    def edit_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|        NaN Air - Edit information         |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Country: {:29}|'''.format(self.country))
        print('''| (2) Airport: {:29}|'''.format(self.airport))
        print('''| (3) Airline: {:29}|'''.format(self.airline))
        print('''| (4) Distance: {:28}|'''.format(self.distance))
        print('''| (5) Contact name: {:24}|'''.format(self.contact_name))
        print('''| (6) Contact phone: {:23}|'''.format(self.contact_phone))
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("What to edit: ")
        print()
        if user_input == '1':
            self.country = input("Enter country: ")
        elif user_input == '2':
            self.airport = input("Enter airport: ")
        elif user_input == '3':
            self.airline = input("Enter airline: ")
        elif user_input == '4':
            self.distance = input("Enter distance: ")
        elif user_input == '5':
            self.contact_name = input("Enter contact name: ")
        elif user_input == '6':
            self.contact_phone = input("Enter contact phone: ")
        self.display_info()

    def print_confirmation(self):
        print()
        print(''' ___________________________________________''')
        print('''|                  NaN Air                  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Destination successfully created!         |''')
        print('''|                                           |''')
        print('''| (1) Create another voyage                 |''')
        print('''| (2) Go back to home page                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input()
        if user_input == '1':
            self.get_destination_info()
        elif user_input == '2':
            return None

    def create_destination(self):
        self.voyage = Voyage(self.country, self.airport, self.airline, self.distance, self.contact_name, self.contact_phone)
        self.print_confirmation()
        return self.voyage

