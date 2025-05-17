```mermaid
classDiagram
    class MenuItem {
        - name: str
        - price: float
        + get_total_price(): float
    }

    class Beverage {
        - is_alcoholic: bool
    }

    class Appetizer {
        - serves: int
    }

    class MainCourse {
        - is_vegetarian: bool
    }

    class Order {
        - items: List~MenuItem~
        + add_item(item: MenuItem)
        + calculate_total(): float
        + show_order()
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order --> MenuItem : contains
