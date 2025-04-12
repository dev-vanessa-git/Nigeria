# POLY MEANS MANY FORMS SO POLYMORPHISM IS BASICALLY A PROGRAM THAT RUNS IN MANY FORMS
# same name of a method in different classes
class Car:
      def __init__(self, brand, model):
            self.brand = brand
            self.model = model

      def move(self):
            print("Drive!!!")

class Boat:
      def __init__(self, brand, model):
            self.brand = brand
            self.model = model

      def move(self):
            print("Sail!!!")

class Plane:
      def __init__(self, brand, model):
            self.brand = brand
            self.model = model

      def move(self):
            print("Fly!!!")

car1 = Car("Toyota", "Camry")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
      x.move()