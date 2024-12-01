from shopping_cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 3)
    assert len(cart.items) == 1
    assert cart.items[0] == {"name": "apple", "price": 1.0, "quantity": 3}

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 3)
    cart.remove_item("apple")
    assert len(cart.items) == 0

def test_get_total_price():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 3)
    cart.add_item("bananan", 1.5, 2)
    assert cart.get_total_price() == 6.0

def test_apply_discount():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 3)
    cart.add_item("bananan", 1.5, 2)
    cart.apply_discount(10)
    assert cart.get_total_price() == 5.4

def test_cart_string_representation():
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 3)
    cart.add_item("bananan", 1.5, 2)
    expected = "apple: $1.0 x 3\\n banana: $1.5 x 2"
    assert str(cart) == expected