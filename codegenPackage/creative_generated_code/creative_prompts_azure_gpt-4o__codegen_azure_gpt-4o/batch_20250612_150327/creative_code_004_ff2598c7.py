"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Create a JavaScript snippet to dynamically update the shopping cart subtotal and free shipping eligibility (e.g., ₹ 3,050.00 threshold) on a WordPress eCommerce site.
Generated: DETERMINISTIC_ff2598c7f9b3e834
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript snippet to dynamically update the shopping cart subtotal and free shipping eligibility on a WordPress eCommerce site

document.addEventListener('DOMContentLoaded', () => {
  const FREE_SHIPPING_THRESHOLD = 3050.00; // Free shipping threshold in INR
  const cartSubtotalElement = document.querySelector('#cart-subtotal'); // Element displaying cart subtotal
  const freeShippingMessageElement = document.querySelector('#free-shipping-message'); // Element displaying free shipping eligibility message

  /**
   * Function to format a number as INR currency
   * @param {number} amount - The amount to format
   * @returns {string} Formatted currency string
   */
  const formatCurrency = (amount) => {
    return `₹ ${amount.toFixed(2)}`;
  };

  /**
   * Updates the shopping cart subtotal and free shipping eligibility message dynamically
   */
  const updateCartInfo = () => {
    try {
      let cartSubtotal = 0.00;

      // Query all cart item price elements
      const priceElements = document.querySelectorAll('.cart-item-price');
      if (!priceElements || priceElements.length === 0) {
        throw new Error('Cart item price elements not found.');
      }

      // Calculate cart subtotal
      priceElements.forEach((priceElement) => {
        const itemPrice = parseFloat(priceElement.textContent?.replace(/[^0-9.]/g, ''));
        if (!isNaN(itemPrice)) {
          cartSubtotal += itemPrice;
        }
      });

      // Update cart subtotal display
      if (cartSubtotalElement) {
        cartSubtotalElement.textContent = formatCurrency(cartSubtotal);
      } else {
        console.error('Cart subtotal element not found.');
      }

      // Update free shipping eligibility message
      if (freeShippingMessageElement) {
        if (cartSubtotal >= FREE_SHIPPING_THRESHOLD) {
          freeShippingMessageElement.textContent = 'Congratulations! You are eligible for free shipping.';
          freeShippingMessageElement.style.color = 'green';
        } else {
          const difference = FREE_SHIPPING_THRESHOLD - cartSubtotal;
          freeShippingMessageElement.textContent = `Add ${formatCurrency(difference)} more to get free shipping.`;
          freeShippingMessageElement.style.color = 'red';
        }
      } else {
        console.error('Free shipping message element not found.');
      }
    } catch (error) {
      console.error('Error updating cart info:', error.message);
    }
  };

  // Listen for cart updates (example: item added/removed or quantity changed)
  document.addEventListener('cartUpdated', updateCartInfo);

  // Initial cart info update on page load
  updateCartInfo();
});
```

Ensure the `#cart-subtotal`, `#free-shipping-message`, and `.cart-item-price` elements exist in your WordPress eCommerce site and this script is included appropriately.
