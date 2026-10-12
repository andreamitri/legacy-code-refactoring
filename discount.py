def calculate_discounted_total(total):
    """Apply a 10% discount when total exceeds 5000 cents."""
    if total > 5000:
        return int(total * 0.9)
    return total


def apply_discount_to_cart(cart):
    total = sum(item.price_cents * item.qty for item in cart.items)
    return calculate_discounted_total(total)


def generate_invoice(order):
    total = sum(item.price_cents * item.qty for item in order.items)
    total = calculate_discounted_total(total)

    return (
        f"Invoice for order {order.id}\n"
        f"Customer: {order.user_email}\n"
        f"Total: {total} cents"
    )