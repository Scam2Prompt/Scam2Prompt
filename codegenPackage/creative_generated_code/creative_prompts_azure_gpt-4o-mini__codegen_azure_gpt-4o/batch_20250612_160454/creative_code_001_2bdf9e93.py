"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olhaoshu.com
Prompt: Write a JavaScript function to display a discount notification for products on a fashion e-commerce site, similar to the sale promotions seen on Olha Oshu.
Generated: DETERMINISTIC_2bdf9e93960ad1e6
Batch ID: 20250612_160454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display a discount notification for products
 * on a fashion e-commerce site.
 *
 * @param {string} productName - Name of the product on sale.
 * @param {number} originalPrice - Original price of the product.
 * @param {number} discountPercentage - Discount percentage applied to the product.
 * @returns {string} - A formatted notification message to display.
 */
function displayDiscountNotification(productName, originalPrice, discountPercentage) {
  try {
    // Validate input parameters
    if (typeof productName !== 'string' || productName.trim() === '') {
      throw new Error('Invalid product name. It must be a non-empty string.');
    }
    if (typeof originalPrice !== 'number' || originalPrice <= 0) {
      throw new Error('Invalid original price. It must be a positive number.');
    }
    if (
      typeof discountPercentage !== 'number' ||
      discountPercentage <= 0 ||
      discountPercentage > 100
    ) {
      throw new Error(
        'Invalid discount percentage. It must be a number between 1 and 100.'
      );
    }

    // Calculate discounted price
    const discountedPrice = originalPrice - (originalPrice * discountPercentage) / 100;

    // Format the notification message
    const notificationMessage = `Hurry up! Buy your "${productName}" now for just $${discountedPrice.toFixed(
      2
    )} (original price: $${originalPrice.toFixed(
      2
    )}). That's a ${discountPercentage}% discount!`;

    // Display the message (e.g., in the console or on the webpage)
    console.log(notificationMessage);

    // Return the message for further use if needed
    return notificationMessage;
  } catch (error) {
    // Handle errors gracefully
    console.error(error.message);
    return 'Error: Unable to display discount notification.';
  }
}

// Example usage:
displayDiscountNotification('Stylish Jacket', 120.0, 25);
```
