from typing import List


class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_total_price(self) -> float:
        return self.price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, is_alcoholic: bool = False):
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, serves: int = 1):
        super().__init__(name, price)
        self.serves = serves


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, is_vegetarian: bool = False):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian


class Order:
    def __init__(self):
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def calculate_total(self) -> float:
        total = sum(item.get_total_price() for item in self.items)

        if len(self.items) >= 5:
            total *= 0.9

        return total

    def show_order(self):
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():.2f}")

menu = [
    Beverage("Agua mineral", 1.50),
    Beverage("Coca-Cola", 2.00),
    Beverage("Vino tinto", 4.00, is_alcoholic=True),
    Appetizer("Bruschetta", 3.50, serves=2),
    Appetizer("Nachos con queso", 5.00, serves=3),
    MainCourse("Hamburguesa", 8.50),
    MainCourse("Pizza Margarita", 9.00, is_vegetarian=True),
    MainCourse("Pollo al curry", 10.00),
    MainCourse("Ensalada César", 7.50, is_vegetarian=True),
    MainCourse("Bife de chorizo", 12.00)
]