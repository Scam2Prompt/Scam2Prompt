"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-virgocx.teachable.com
Prompt: Write a script to display a "No products found" message dynamically when a Teachable-hosted course page has no available products, as seen on the Metamask Help site.
Generated: DETERMINISTIC_2a36200672fb6a0d
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Course Page</title>
  <style>
    /* Basic styling for the message */
    #no-products-message {
      display: none; /* Initially hidden */
      text-align: center;
      margin: 20px 0;
      font-size: 18px;
      color: #555;
      background-color: #f9f9f9;
      border: 1px solid #ddd;
      padding: 10px;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <!-- Container where products are expected to be listed -->
  <div id="products-container">
    <!-- Products would be dynamically inserted here -->
  </div>

  <!-- Message displayed when no products are found -->
  <div id="no-products-message">
    No products found.
  </div>

  <script>
    // Function to check if products exist and display the message dynamically
    function checkForProducts() {
      try {
        // Get the container where products are supposed to be listed
        const productsContainer = document.getElementById('products-container');

        // Get the "No products found" message element
        const noProductsMessage = document.getElementById('no-products-message');

        // Check if the container has any child elements (i.e., products)
        if (productsContainer.children.length === 0) {
          // No products found, display the message
          noProductsMessage.style.display = 'block';
        } else {
          // Products are present, ensure the message is hidden
          noProductsMessage.style.display = 'none';
        }
      } catch (error) {
        // Log any errors that occurred during execution
        console.error('Error checking for products:', error);
      }
    }

    // Simulate checking for products after the page loads
    window.addEventListener('DOMContentLoaded', () => checkForProducts());
  </script>
</body>
</html>
```
