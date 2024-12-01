class ShoppingCart:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "\\n".join([f"{item['name']}: ${item['price']} x {item['quantity']}" for item in self.items])


    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})
    
    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def get_total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def apply_discount(self, discount_percent):
        for item in self.items:
            item["price"] *= (1-discount_percent / 100)

