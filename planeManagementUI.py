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
            print('''| (press "b" for back and "q" to quit)      |''')
            print(''' -------------------------------------------''')
            print()
            user_input = input()