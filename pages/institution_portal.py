class Institution:
    def __init__(self, name, provides, location, capacity, monthly_rate):
        self.name = name
        self.needs = provides
        self.location = location
        self.capacity = capacity
        self.average_rate = monthly_rate

    def __str__(self):
        return f"{self.name} provides {self.provides} and are located in {self.location}. They have a capacity of {self.capacity}."
        
    def __repr__(self):
        return f"Institution({self.name}, {self.age}, {self.dob}, {self.needs}, {self.location})"