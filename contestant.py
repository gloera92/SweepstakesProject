

class Contestant:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.registration_number = ()

    def notify_winner(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = registration_number

        print(f'{first_name} {last_name} {email} {registration_number} is the winner!')
