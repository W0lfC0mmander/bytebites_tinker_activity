# Defines Customer, FoodItem, Menu, and Order for the ByteBites ordering system.

from __future__ import annotations

from typing import List, Optional


class Customer:
    def __init__(self, name: str, purchase_history: Optional[List[Order]] = None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []


class FoodItem:
    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        popularity_rating: float,
    ):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items: Optional[List[FoodItem]] = None):
        self.items = items if items is not None else []

    def filter_by_category(self, category: str) -> List[FoodItem]:
        return [item for item in self.items if item.category == category]

    def sort_by_price(self, ascending: bool = True) -> List[FoodItem]:
        return sorted(self.items, key=lambda item: item.price, reverse=not ascending)

    def sort_by_popularity(self, ascending: bool = False) -> List[FoodItem]:
        return sorted(
            self.items,
            key=lambda item: item.popularity_rating,
            reverse=not ascending,
        )


class Order:
    def __init__(self, items: Optional[List[FoodItem]] = None):
        self.items = items if items is not None else []

    def calculate_total(self) -> float:
        return sum((item.price for item in self.items), 0.0)


if __name__ == "__main__":
    menu = Menu(
        [
            FoodItem("Spicy Burger", 8.50, "Mains", 4.7),
            FoodItem("Large Soda", 2.00, "Drinks", 4.2),
            FoodItem("Chocolate Cake", 5.00, "Desserts", 4.9),
        ]
    )

    print("Drinks:", [item.name for item in menu.filter_by_category("Drinks")])
    print("Sorted by price:", [item.name for item in menu.sort_by_price()])
    print("Most popular:", [item.name for item in menu.sort_by_popularity()])

    order = Order([menu.items[0], menu.items[1]])
    print(f"Order total: ${order.calculate_total():.2f}")
