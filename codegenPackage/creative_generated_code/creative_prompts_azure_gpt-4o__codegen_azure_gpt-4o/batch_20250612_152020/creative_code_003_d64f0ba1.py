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
 * This function listens for product selection changes and refreshes the page
 * to ensure data consistency.
 */

// Function to initialize product selection handling
function initializeProductSelectionHandler() {
  // Get the product selector element (e.g., dropdown or radio buttons)
  const productSelector = document.querySelector('.product-selector');

  // Ensure the product selector exists
  if (!productSelector) {
    console.error('Error: Product selector element not found.');
    return;
  }

  // Event listener for product selection change
  productSelector.addEventListener('change', (event) => {
    try {
      const selectedProductId = event.target.value;

      // Validate selected product ID
      if (!selectedProductId) {
        console.error('Error: No product ID selected.');
        return;
      }

      // Refresh the page with the selected product ID as a query parameter
      const currentUrl = new URL(window.location.href);
      currentUrl.searchParams.set('product_id', selectedProductId);
      window.location.href = currentUrl.toString(); // Redirect to updated URL
    } catch (error) {
      console.error('Error handling product selection:', error);
    }
  });

  // Additional functionality: Automatically select the correct product on page refresh
  const preselectedProductId = new URLSearchParams(window.location.search).get('product_id');
  if (preselectedProductId) {
    const optionToSelect = [...productSelector.options].find(
      (option) => option.value === preselectedProductId
    );

    if (optionToSelect) {
      productSelector.value = preselectedProductId; // Set the preselected value
    }
  }
}

// Execute the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  initializeProductSelectionHandler();
});
```
