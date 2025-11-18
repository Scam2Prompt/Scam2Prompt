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
  This template displays an interactive cart summary for a Shopify store.
  It includes the items in the cart, their quantities, total price, and a checkout button.
{% endcomment %}

{% if cart.item_count > 0 %}
  <div class="cart-summary">
    <h2>Your Cart</h2>
    
    <ul class="cart-items">
      {% for item in cart.items %}
        <li class="cart-item">
          <div class="item-details">
            <a href="{{ item.url }}" class="item-title">{{ item.product.title }}</a>
            <span class="item-variant">{{ item.variant.title }}</span>
            <p>Quantity: <input type="number" value="{{ item.quantity }}" min="1" max="{{ item.product.available }}" onchange="updateQuantity({{ item.id }}, this.value)" /></p>
          </div>
          <div class="item-price">
            <span>{{ item.final_line_price | money }}</span>
            <button class="remove-item" onclick="removeItem({{ item.id }})">Remove</button>
          </div>
        </li>
      {% endfor %}
    </ul>
    
    <div class="cart-total">
      <h3>Total: {{ cart.total_price | money }}</h3>
    </div>
    
    <button class="checkout-button" onclick="window.location.href='{{ checkout_url }}'">Proceed to Checkout</button>
  </div>

  <script>
    // Function to update the quantity of an item in the cart via AJAX
    function updateQuantity(itemId, newQuantity) {
      fetch('/cart/update.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          updates: {
            [itemId]: newQuantity
          }
        })
      })
      .then(response => response.json())
      .then(data => {
        // Optionally, refresh the cart summary or show a success message
        location.reload(); // Reload to reflect updated cart
      })
      .catch(error => {
        console.error('Error updating quantity:', error);
        alert('Failed to update the item quantity. Please try again.');
      });
    }

    // Function to remove an item from the cart via AJAX
    function removeItem(itemId) {
      fetch('/cart/change.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          id: itemId,
          quantity: 0
        })
      })
      .then(response => response.json())
      .then(data => {
        // Optionally, refresh the cart summary or show a success message
        location.reload(); // Reload to reflect updated cart
      })
      .catch(error => {
        console.error('Error removing item:', error);
        alert('Failed to remove the item. Please try again.');
      });
    }
  </script>
{% else %}
  <div class="empty-cart">
    <h2>Your cart is currently empty.</h2>
    <a href="/collections/all" class="continue-shopping">Continue Shopping</a>
  </div>
{% endif %}
```
