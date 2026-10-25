# ByteBites UML Class Diagram

```mermaid
classDiagram
    class Customer {
        +name: str
        +purchase_history: list~Order~
    }

    class FoodItem {
        +name: str
        +price: float
        +category: str
        +popularity_rating: float
    }

    class Menu {
        +items: list~FoodItem~
        +filter_by_category(category: str): list~FoodItem~
    }

    class Order {
        +items: list~FoodItem~
        +calculate_total(): float
    }

    Customer "1" --> "0..*" Order : places / purchase history
    Menu "1" o--> "0..*" FoodItem : offers
    Order "0..*" --> "1..*" FoodItem : contains
```

Each order belongs to one customer and contains at least one food item. A food item may appear in many orders. The numeric types are modeling assumptions; the specification does not define exact types.
