from plane import Plane

class PlaneManagementUI():
    def renderMenu(self):
        user_input = "1"
        while user_input == "1" or user_input == "2":
            print(''' ___________________________________________''')
            print('''|                  NaN Air                  |''')
            print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| ''')
            print('''|                                           |''')   
            print('''| (1) Create plane                          |''')
            print('''| (2) Get list of planes                    |''')
            print('''|                                           |''')
            print('''| (press "b" for back)                      |''')
            print('''|                                           |''')
            print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print()
            user_input = input("Input: ")
            print()
            if user_input == "1":
                self.get_plane_info()
            elif user_input == "2":
                pass
            elif user_input == "b":
                pass

    def get_plane_info(self):
        self.registration = input("Enter aircraft registration: ")
        self.plane_type = input("Enter aircraft type: ")
        self.manufacturer = input("Enter aircraft manufacturer: ")
        self.seats = input("Enter number of seats: ")
        self.display_info()

    def display_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|  NaN Air - Airplane successfully created  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Aircraft registration: {:19}|'''.format(self.registration))
        print('''| Aircraft type: {:27}|'''.format(self.plane_type))
        print('''| Aircraft manufacturer: {:19}|'''.format(self.manufacturer))
        print('''| Number of seats: {:25}|'''.format(self.seats))
        print('''|                                           |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Confirm                               |''')
        print('''| (2) Edit                                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.display_confirmation()
        elif user_input == "2":
            self.edit_info()



    def edit_info(self):
        print()
        print(''' ___________________________________________''')
        print('''|        NaN Air - Edit information         |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Aircraft registration: {:15}|'''.format(self.registration))
        print('''| (2) Aircraft type: {:23}|'''.format(self.plane_type))
        print('''| (3) Aircraft manufacturer: {:15}|'''.format(self.manufacturer))
        print('''| (4) Number of seats: {:21}|'''.format(self.seats))
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("What to edit: ")
        print()
        if user_input == "1":
            self.registration = input("Enter aircraft registration: ")
        elif user_input == "2":
            self.plane_type = input("Enter aircraft type: ")
        elif user_input == "3":
            self.manufacturer = input("Enter aircraft manufacturer: ")
        elif user_input == "4":
            self.seats = input("Enter number of seats: ")
        self.display_info()

    def create_plane(self):
        self.plane = Plane(self.registration, self.plane_type, self.manufacturer, self.seats)
        return self.plane

    def display_confirmation(self):
        print()
        print(''' ___________________________________________''')
        print('''|  NaN Air - Airplane successfully created  |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| Aircraft registration: {:19}|'''.format(self.registration))
        print('''| Aircraft type: {:27}|'''.format(self.plane_type))
        print('''| Aircraft manufacturer: {:19}|'''.format(self.manufacturer))
        print('''| Number of seats: {:25}|'''.format(self.seats))
        print('''|                                           |''')
        print('''|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|''')
        print('''| (1) Create another plane                  |''')
        print('''| (2) Go back to home page                  |''')
        print('''|                                           |''')
        print(''' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print()
        user_input = input("Input: ")
        print()
        if user_input == "1":
            self.create_plane()
        elif user_input == "2":
            pass


a = PlaneManagementUI()
a.renderMenu()