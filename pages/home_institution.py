class Institution:
    def __init__(self, name, age, dob, needs, location, medications, email, phone_num):
        self.name = name
        self.age = age
        self.dob = dob
        self.needs = needs
        self.location = location
        self.medications = medications
        self.email = email
        self.phone_num = phone_num
        self.isHost = True


    def __str__(self):
        return f"{self.name} is {self.age} years old, born on {self.dob}. They need {self.needs} and are located in {self.location}."
        
    def __repr__(self):
        return f"Patient({self.name}, {self.age}, {self.dob}, {self.needs}, {self.location})"