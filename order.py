class Order:
    def __init__(self, user_id, user_email, items):
        self.user_id = user_id
        self.user_email = user_email
        self.items = items


class OrderRepository:
    def save(self, order):
        print(f"Saving order for user {order.user_id}")


order = Order(1, "student@example.com", ["Book", "Pen"])

repository = OrderRepository()
repository.save(order)