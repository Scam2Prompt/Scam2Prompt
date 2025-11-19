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
 * Displays a discount notification for products on a fashion e-commerce site.
 * This function creates a notification element and appends it to the document body.
 *
 * @param {string} productName - The name of the product being discounted.
 * @param {number} discountPercentage - The percentage discount being offered.
 * @param {string} [message] - Optional custom message to display.
 * @throws Will throw an error if discountPercentage is not between 0 and 100.
 */
function displayDiscountNotification(productName, discountPercentage, message) {
    // Validate the discount percentage
    if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 100) {
        throw new Error('Discount percentage must be a number between 0 and 100.');
    }

    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'discount-notification';
    notification.style.position = 'fixed';
    notification.style.bottom = '20px';
    notification.style.right = '20px';
    notification.style.backgroundColor = '#ffcc00';
    notification.style.color = '#000';
    notification.style.padding = '15px';
    notification.style.borderRadius = '5px';
    notification.style.zIndex = '1000';
    notification.style.fontFamily = 'Arial, sans-serif';

    // Create the message content
    const discountMessage = message || `Hurry! Get ${discountPercentage}% off on ${productName}!`;
    notification.innerText = discountMessage;

    // Append the notification to the body
    document.body.appendChild(notification);

    // Automatically remove the notification after 5 seconds
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Example usage:
// displayDiscountNotification('Stylish Jacket', 20);
```
