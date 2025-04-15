class Superhero:
    def __init__(self, name, superpower, city):
        self.name = name
        self.superpower = superpower
        self.city = city

    def save_the_day(self):
        print(f"{self.name} is saving the day in {self.city} using {self.superpower}!")

    def get_info(self):
        return f"Name: {self.name}\nSuperpower: {self.superpower}\nCity: {self.city}"


# Inheriting from Superhero to create a subclass
class Speedster(Superhero):
    def __init__(self, name, superpower, city, speed):
        super().__init__(name, superpower, city)
        self.speed = speed

    def save_the_day(self):
        print(f"{self.name} is running at {self.speed} mph to save the day in {self.city}!")

# Creating objects
hero = Superhero("Captain Power", "Invisibility", "Metropolis")
print(hero.get_info())
hero.save_the_day()

speedster = Speedster("Flash", "Super Speed", "Central City", 500)
print(speedster.get_info())
speedster.save_the_day()
