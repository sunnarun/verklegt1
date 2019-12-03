class Employee():
    def __init__(self, ssn, name, role, rank, address, phone_no):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.address = address
        self.phone_no = phone_no

    def generate_email(self):
        self.email = self.name.replace(" ",".").lower() + "@" + "nanaair.is"
        print(self.email)
        return self.email

isol = Employee("0110972519", "Isol Sigurdardottir", "pilot", "captain", "Einiberg 21", "6613536")
isol.generate_email()