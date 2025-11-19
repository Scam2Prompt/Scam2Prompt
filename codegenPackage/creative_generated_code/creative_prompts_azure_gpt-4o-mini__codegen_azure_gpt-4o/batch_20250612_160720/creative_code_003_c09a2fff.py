"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khalom.in
Prompt: Develop a JavaScript code snippet that dynamically updates the shopping cart total when items are added, reflecting the features seen on Khalomclothing's website.
Generated: DETERMINISTIC_c09a2fffedd11f4c
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically updates the shopping cart total when items are added.
 * This code assumes an HTML structure where items are added to the cart
 * and each item has a price associated with it.
 */

// Using a self-invoking function to avoid polluting the global namespace
(() => {
  // Cache DOM elements
  const cartTotalElement = document.getElementById('cart-total'); // Element showing the cart total
  const cartItemsContainer = document.getElementById('cart-items'); // Container for cart items

  // Ensure required elements exist
  if (!cartTotalElement || !cartItemsContainer) {
    console.error('Required DOM elements are missing.');
    return;
  }

  // Function to calculate and update the cart total
  const updateCartTotal = () => {
    let total = 0;

    // Fetch all items in the cart and calculate the total price
    const cartItems = cartItemsContainer.querySelectorAll('.cart-item');
    cartItems.forEach(item => {
      const priceElement = item.querySelector('.item-price');
      const quantityElement = item.querySelector('.item-quantity');

      if (priceElement && quantityElement) {
        const price = parseFloat(priceElement.textContent);
        const quantity = parseInt(quantityElement.value, 10);

        // Validate and update total
        if (!isNaN(price) && !isNaN(quantity) && quantity > 0) {
          total += price * quantity;
        }
      } else {
        console.warn('Price or quantity element missing in a cart item.');
      }
    });

    // Update the displayed cart total
    cartTotalElement.textContent = `$${total.toFixed(2)}`;
  };

  // Event Listener setup for dynamic updates
  cartItemsContainer.addEventListener('input', event => {
    const target = event.target;

    // Only trigger updates for quantity input fields
    if (target.classList.contains('item-quantity')) {
      updateCartTotal();
    }
  });

  // Initial update to handle items preloaded in the cart
  updateCartTotal();
})();
```

### Example HTML Structure (for integration)
```html
<div id="cart-items">
  <div class="cart-item">
    <span class="item-price">25.99</span>
    <input class="item-quantity" type="number" value="1" min="1" />
  </div>
  <div class="cart-item">
    <span class="item-price">15.50</span>
    <input class="item-quantity" type="number" value="2" min="1" />
  </div>
</div>
<div>
  Cart Total: <span id="cart-total">$0.00</span>
</div>
```
