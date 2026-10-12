# Work Requirement 2

## 1. converter.py

### Problem

The original Converter class did not clearly explain what it was
converting. The class name was too general, and the numbers used
in the calculation were difficult to understand.

### Improvement

I renamed the class to `FahrenheitToCelsiusConverter` and added
docstrings to explain what the class and method do.
I also made the conversion formula easier to read.

### Why?

Now other developers can easily understand that the code converts
temperatures from Fahrenheit to Celsius.

## 2. order.py

### Problem

The original Order class was responsible for storing order information
and saving orders to a database. It also depended directly on the
User object's attributes and SQL statements.

This made the code difficult to change and test.

### Improvement

I separated the Order class from the OrderRepository class.
The Order class now handles order information, while the repository
handles saving orders.

I used a simple placeholder instead of a real database.

### Why?

This makes the code easier to maintain because changes to the database
do not require changing the Order class. It also makes testing easier.

## 3. discount.py

### Problem

The original code had the same discount calculation in two functions:
`apply_discount_to_cart()` and `generate_invoice()`.

If the discount percentage or limit changed, both functions would
need to be updated.

### Improvement

I created a separate function called `calculate_discounted_total()`
that handles the discount calculation.

Both the cart and invoice functions now use this shared function.

### Why?

The discount rule is now written in only one place.
This reduces duplicated code and makes future changes easier.

## 4. process_order.py

### Problem

The original `process_order()` method was doing too many things.
It calculated the total, applied discounts, saved the order,
and notified the customer.

This made the method difficult to understand, maintain, and test.

### Improvement

I divided the method into smaller functions:

- `calculate_total()` calculates the order total.
- `apply_discount()` applies the discount.
- `save_order()` represents saving the order.
- `notify_user()` represents notifying the customer.

The main `process_order()` function now calls these smaller functions.

I used simple placeholders instead of real database and email functionality.

### Why?

Each function now has one responsibility.
This makes the code easier to read, test, and modify.

## 5. Personal Reflection

The problem I find most difficult is tight coupling because different parts of the code depend too much on each other. If you change one part, it can cause problems in other parts. This can make the code harder to understand, fix, and test, especially in bigger projects. Before this assignment, I did not really understand why it was important to separate different tasks in the code. When I improved the Order class, I learned that keeping order information and database operations separate makes the code easier to work with. I also learned that small changes can make code better and easier to maintain.

## 6. Running the Code

To run the Converter example:

```bash
python converter.py
```

To run the Order example:

```bash
python order.py
```

The discount and order-processing examples contain functions that
can be tested separately.

To run the unit tests:

```bash
python -m unittest -v
```
