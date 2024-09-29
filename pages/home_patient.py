class Patient:
    def __init__(self, name, age, dob, needs, location, medications, password, email):
        self.name = name
        self.age = age
        self.dob = dob
        self.needs = needs
        self.isHost = False

        #self.location = location

        self.medications = medications
        self.password = password
        self.email = email

    def __str__(self):
        return f"{self.name} is {self.age} years old, born on {self.dob}. They need {self.needs} and are located in {self.location}."
        
    def __repr__(self):
        return f"Patient({self.name}, {self.age}, {self.dob}, {self.needs}, {self.location})"