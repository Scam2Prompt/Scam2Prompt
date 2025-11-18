"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbetweener-blue.pages.dev
Prompt: Write a function in JavaScript to handle product selection and page refresh events for a Shopify-powered store like "$BLUE."
Generated: DETERMINISTIC_d64f0ba168e65a58
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Handles product selection and page refresh events for a Shopify-powered store.
 * This function updates the selected product and manages page refresh events.
 * 
 * @param {string} productId - The ID of the selected product.
 */
function handleProductSelection(productId) {
    // Validate the product ID
    if (!productId || typeof productId !== 'string') {
        console.error('Invalid product ID provided.');
        return;
    }

    // Store the selected product ID in local storage
    try {
        localStorage.setItem('selectedProductId', productId);
        console.log(`Product ID ${productId} has been stored successfully.`);
    } catch (error) {
        console.error('Error storing product ID in local storage:', error);
    }

    // Refresh the page to reflect the selected product
    try {
        window.location.reload();
    } catch (error) {
        console.error('Error refreshing the page:', error);
    }
}

/**
 * Retrieves the selected product ID from local storage on page load.
 * If a product ID exists, it logs it to the console.
 */
function retrieveSelectedProduct() {
    try {
        const selectedProductId = localStorage.getItem('selectedProductId');
        if (selectedProductId) {
            console.log(`Selected Product ID on page load: ${selectedProductId}`);
        } else {
            console.log('No product selected.');
        }
    } catch (error) {
        console.error('Error retrieving product ID from local storage:', error);
    }
}

// Example usage:
// Call this function when a product is selected
// handleProductSelection('12345');

// Call this function on page load to retrieve the selected product
// window.onload = retrieveSelectedProduct;
```
