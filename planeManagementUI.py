class PlaneManagementUI():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2":
            print(''' -------------------------------------------''')
            print('''|                  NaN Air                  |''')
            print(''' ------------------------------------------- ''')
            print('''| (1) Create plane                          |''')
            print('''| (2) Get list of planes                    |''')
            print('''|                                           |''')
            print('''| (press "b" for back)                      |''')
            print(''' -------------------------------------------''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.create_new_plane()
            elif user_input == "2":
                pass
            elif user_input == "b":
                pass
                

    def create_new_plane(self):
        self.registration = input("Enter aircraft registration: ")
        self.plane_type = input("Enter aircraft type: ")
        self.manufacturer = input("Enter aircraft manufacturer: ")
        self.seats = input("Enter number of seats: ")
        self.display_info()

    def display_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|  NaN Air - Employee successfully created  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Aircraft registration: {:19}|'''.format(self.registration))
        print('''| Aircraft type: {:27}|'''.format(self.plane_type))
        print('''| Aircraft manufacturer: {:19}|'''.format(self.manufacturer))
        print('''| Number of seats: {:25}|'''.format(self.seats))
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Create another plane                  |''')
        print('''| (2) Go back to home page                  |''')
        print('''| (3) Edit                                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.create_new_plane()
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass

a = PlaneManagementUI()
a.renderMenu()