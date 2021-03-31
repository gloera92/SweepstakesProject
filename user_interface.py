from contestant import Contestant


class UserInterface:
    def __init__(self):
        self.contestants = Contestant()

    def contestant_info(self):
        self.contestants.first_name = input()
        self.contestants.last_name = input()
        self.contestants.email = input()
        self.contestants.registration_number = input()



