"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbetweener-blue.pages.dev
Prompt: Generate code to display an interactive cart summary using Shopify's Liquid template language for a store like "$BLUE."
Generated: DETERMINISTIC_db1629850da738df
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```liquid
{% comment %}
  Interactive Cart Summary Template
  This Liquid script displays a detailed cart summary for the Shopify store "$BLUE".
  The template includes error handling and interactive elements for user interaction.
{% endcomment %}

{% assign cart_items = cart.items %}
{% assign cart_total_price = cart.total_price %}
{% assign cart_item_count = cart.item_count %}
{% assign currency = shop.currency %}

<div id="cart-summary">
  <h2>Cart Summary</h2>
  
  {% comment %}
    Check if the cart is empty
  {% endcomment %}
  {% if cart_item_count == 0 %}
    <p>Your cart is currently empty.</p>
  {% else %}
    <ul>
      {% for item in cart_items %}
        <li>
          <div class="cart-item">
            <img src="{{ item.image | default: 'placeholder.jpg' }}" alt="{{ item.title }}" class="cart-item-image">
            <div class="cart-item-details">
              <h3>{{ item.title }}</h3>
              <p>{{ item.quantity }} × {{ item.line_price | money }}</p>
              <form method="post" action="/cart/change">
                <input type="hidden" name="id" value="{{ item.id }}">
                <input type="number" name="quantity" value="{{ item.quantity }}" min="0" class="quantity-input">
                <button type="submit">Update</button>
              </form>
            </div>
          </div>
        </li>
      {% endfor %}
    </ul>
    <div class="cart-total">
      <p><strong>Total:</strong> {{ cart_total_price | money_with_currency }}</p>
    </div>
    <a href="/checkout" class="checkout-button">Proceed to Checkout</a>
  {% endif %}
</div>

<style>
  /* Basic styling for the cart summary */
  #cart-summary {
    margin: 20px;
    font-family: Arial, sans-serif;
  }
  .cart-item {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
  }
  .cart-item-image {
    width: 80px;
    height: 80px;
    margin-right: 10px;
  }
  .cart-item-details {
    flex: 1;
  }
  .quantity-input {
    width: 50px;
  }
  .checkout-button {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #0073e6;
    color: white;
    text-decoration: none;
    border-radius: 5px;
  }
  .checkout-button:hover {
    background-color: #005bb5;
  }
</style>

<script>
  // Basic interactive functionality for quantity input validation
  document.addEventListener('DOMContentLoaded', function() {
    const quantityInputs = document.querySelectorAll('.quantity-input');
    quantityInputs.forEach(input => {
      input.addEventListener('input', function() {
        if (this.value < 0) {
          alert('Quantity cannot be negative.');
          this.value = 0;
        }
      });
    });
  });
</script>
```
