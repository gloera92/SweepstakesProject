from contestant import Contestant
from sweepstake import Sweepstake


class UserInterface:
    def __init__(self):
        self.user = Contestant()
        self.sweepstake = Sweepstake()

    def generate_contestant_info(self):
        self.user.first_name = input("enter first name")
        self.user.last_name = input("enter last name")
        self.user.email = input("enter email")
        self.user.registration_number = input("enter registration number")
        return self

    def fill_dictionary(self):
        self.sweepstake.contestants_dict["first_name"] = [self.user.first_name]
        self.sweepstake.contestants_dict["last_name"] = [self.user.last_name]
        self.sweepstake.contestants_dict["email"] = [self.user.email]
        self.sweepstake.contestants_dict["registration_number"] = [self.user.registration_number]
        print(self.sweepstake.contestants_dict)


test = UserInterface()
test.generate_contestant_info()
test.fill_dictionary()







