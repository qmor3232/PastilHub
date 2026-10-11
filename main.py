# main.py - Pastilicious interactive features (PyScript + Python)
# Each function below is an EVENT HANDLER: it runs when the user does something.

from html import escape
from pyscript import document, when

# Product names and their prices
PRICES = {
    "Regular Chicken Pastil": 35,
    "Spicy Chicken Pastil": 40,
    "Chicken Pastil with Egg": 45,
    "Extra Chicken Pastil": 50,
}


# ---------- Helper functions ----------

def get(element_id):
    """Find an element on the page by its id."""
    return document.getElementById(element_id)


def read_quantity(text):
    """Convert the typed quantity to a whole number. Return 0 if it is invalid."""
    try:
        quantity = int(text)
    except ValueError:
        return 0
    if quantity <= 0:
        return 0
    return quantity


def show_error(text):
    """Show a friendly error message in the order form."""
    get("order-error").innerText = text


def build_summary(product, quantity):
    """Calculate the total and return the order summary as HTML."""
    price = PRICES[product]

    # Calculate the total price
    total = price * quantity

    return f"""
        <div class="summary-box">
            <p><strong>{product}</strong></p>
            <p>{quantity} × ₱{price}</p>
            <p class="total">Total: ₱{total}</p>
        </div>
    """


def check_product_and_quantity():
    """Validate product and quantity. Return (product, quantity) or None."""
    product = get("product-select").value
    quantity = read_quantity(get("quantity").value)

    if product == "":
        show_error("Please select a product.")
        return None
    if quantity == 0:
        show_error("Please enter a valid quantity.")
        return None
    return product, quantity