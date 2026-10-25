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


class Order:
    def __init__(self, items: Optional[List[FoodItem]] = None):
        self.items = items if items is not None else []

    def calculate_total(self) -> float:
        raise NotImplementedError
