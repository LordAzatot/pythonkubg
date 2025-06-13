class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Початкова швидкість

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(0, self.speed - 5)  # Не дозволяємо швидкості бути менше нуля

    def get_speed(self):
        return self.speed


# Створення об'єкта та виклики методів
car = Car("Toyota", "Corolla", 2020)

print("Прискорення:")
for _ in range(5):
    car.accelerate()
    print(f"Поточна швидкість: {car.get_speed()} км/год")

print("\nГальмування:")
for _ in range(5):
    car.brake()
    print(f"Поточна швидкість: {car.get_speed()} км/год")
