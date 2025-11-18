"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Create a function in JavaScript to dynamically update the "Wall Memes" shopping cart when a user adds or removes products, ensuring compatibility with PrestaShop-based platforms.
Generated: DETERMINISTIC_3398e1f8e543913d
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Updates the "Wall Memes" shopping cart dynamically when a user adds or removes products.
 * Designed for compatibility with PrestaShop-based platforms.
 *
 * @param {string} action - The action to perform ('add' or 'remove').
 * @param {number} productId - The ID of the product to add or remove.
 * @param {number} quantity - The quantity to add or remove (default is 1).
 */
async function updateCart(action, productId, quantity = 1) {
  try {
    // Validate inputs
    if (!['add', 'remove'].includes(action)) {
      throw new Error('Invalid action. Use "add" or "remove".');
    }
    if (!Number.isInteger(productId) || productId <= 0) {
      throw new Error('Invalid productId. Provide a positive integer.');
    }
    if (!Number.isInteger(quantity) || quantity <= 0) {
      throw new Error('Invalid quantity. Provide a positive integer.');
    }

    // Build the request URL and data payload
    const apiUrl = '/api/cart/update'; // Adjust the endpoint as per your PrestaShop setup
    const payload = {
      action: action,
      product_id: productId,
      quantity: quantity,
    };

    // Send the request to the server
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    // Handle response
    if (!response.ok) {
      const errorDetails = await response.json();
      throw new Error(`Failed to update cart: ${errorDetails.message || response.statusText}`);
    }

    const result = await response.json();

    // Optionally update the UI (Example for PrestaShop platforms)
    if (result.success) {
      const cartElement = document.getElementById('shopping-cart');
      if (cartElement) {
        cartElement.innerHTML = result.updatedCartHtml; // Assuming the server returns updated cart HTML
      }
      console.log('Cart updated successfully:', result);
    } else {
      throw new Error(result.message || 'Unknown error occurred while updating the cart.');
    }
  } catch (error) {
    // Log the error and notify the user
    console.error('Error updating cart:', error.message);
    alert(`Error updating cart: ${error.message}`);
  }
}

// Example usage:
// Adding 2 units of product with ID 101
// updateCart('add', 101, 2);

// Removing 1 unit of product with ID 102
// updateCart('remove', 102, 1);
```
