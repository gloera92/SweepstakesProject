import user_interface
from contestant import Contestant


class Sweepstake:
    def __init__(self):
        self.contestants = {}

    def register_contestant(self):
        first_name = user_interface.get_string_input('')
        last_name = user_interface.get_string_input('')
        email = user_interface.get_string_input('')
        contestant = Contestant(first_name, last_name, email)

        registration_number = len(self.contestants)
        self.contestants[registration_number] = contestant
