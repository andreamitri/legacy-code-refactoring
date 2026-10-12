def calculate_total(items):
    return sum(item.price * item.qty for item in items)


def apply_discount(total, discount_code):
    if discount_code == "VIP":
        return total * 0.8
    elif discount_code == "FREESHIP":
        return total - 50
    return total


def save_order(user, total):
    print(f"Saving order for {user.email}: {total}")


def notify_user(user, total):
    print(f"Email sent to {user.email}: Total is {total}")


def process_order(order, user, discount_code, notify=False):
    total = calculate_total(order.items)
    total = apply_discount(total, discount_code)

    save_order(user, total)

    if notify:
        notify_user(user, total)

    return total