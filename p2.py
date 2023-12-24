class Car:
    def __init__(self, make, model, year, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.available = available

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Customer: {self.name}"


class Rental:
    def __init__(self):
        self.cars = []

    def rent_car(self, car, customer):
        if car.available:
            car.available = False
            self.cars.append((car, customer))
            print(f"{customer} rented {car}.")
        else:
            print(f"Sorry, {car} is not available for rent.")

    def return_car(self, car):
        for rented_car, customer in self.cars:
            if rented_car == car:
                rented_car.available = True
                self.cars.remove((rented_car, customer))
                print(f"{customer} returned {car}.")
                return
        print(f"Error: {car} is not in the list of rented cars.")

    def display_rented_cars(self):
        if not self.cars:
            print("No cars are currently rented.")
        else:
            print("Rented cars:")
            for rented_car, customer in self.cars:
                print(f"{customer} - {rented_car}")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Focus", 2023)

customer1 = Customer("Alice")
customer2 = Customer("Bob")

rental_system = Rental()

rental_system.rent_car(car1, customer1)
rental_system.rent_car(car2, customer2)
rental_system.display_rented_cars()

rental_system.return_car(car1)
rental_system.display_rented_cars()
