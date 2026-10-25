from models import Customer, FoodItem, Menu, Order


def test_order_calculates_total_for_multiple_items():
    items = [
        FoodItem("Spicy Burger", 8.50, "Entrees", 4.8),
        FoodItem("Large Soda", 2.25, "Drinks", 4.2),
        FoodItem("Fries", 3.00, "Sides", 4.5),
    ]
    order = Order(items)

    assert order.calculate_total() == 13.75


def test_empty_order_has_zero_total():
    order = Order()

    assert order.calculate_total() == 0.0


def test_menu_filters_items_by_category():
    burger = FoodItem("Spicy Burger", 8.50, "Entrees", 4.8)
    soda = FoodItem("Large Soda", 2.25, "Drinks", 4.2)
    water = FoodItem("Bottled Water", 1.50, "Drinks", 4.0)
    menu = Menu([burger, soda, water])

    assert menu.filter_by_category("Drinks") == [soda, water]