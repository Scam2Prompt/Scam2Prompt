"""
Generated Code Metadata:
========================
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Write code to display a "No products found" message dynamically when an online course platform has no available products, similar to the rabbie-wall--extension-docs site.
Generated: DETERMINISTIC_816b6b229d662de0
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a "No products found" message when no products are available.
 * This function checks the DOM for product elements and shows a message if none are found.
 */
function displayNoProductsMessage() {
    try {
        // Select all product elements - adjust the selector based on your platform's HTML structure
        const productElements = document.querySelectorAll('.product, .course, .product-item');
        
        // Get the container where the message should be displayed
        const productsContainer = document.querySelector('.products-container, .courses-list, .product-grid') || document.body;
        
        // Create or find the message element
        let messageElement = document.getElementById('no-products-message');
        
        if (productElements.length === 0) {
            if (!messageElement) {
                messageElement = document.createElement('div');
                messageElement.id = 'no-products-message';
                messageElement.textContent = 'No products found';
                messageElement.style.textAlign = 'center';
                messageElement.style.padding = '20px';
                messageElement.style.fontSize = '18px';
                messageElement.style.color = '#666';
                productsContainer.appendChild(messageElement);
            }
        } else {
            // Remove the message if products exist
            if (messageElement) {
                messageElement.remove();
            }
        }
    } catch (error) {
        console.error('Error displaying no products message:', error);
    }
}

// Run the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', displayNoProductsMessage);

// Also run when dynamic content might have loaded (e.g., AJAX, filters)
// Adjust the event names based on your platform's implementation
document.addEventListener('ajaxComplete', displayNoProductsMessage);
document.addEventListener('filterApplied', displayNoProductsMessage);

// For single-page applications or dynamic content, you might need to observe DOM changes
// This is a more comprehensive solution but may impact performance
if (typeof MutationObserver !== 'undefined') {
    const observer = new MutationObserver(function(mutations) {
        displayNoProductsMessage();
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
}
```
