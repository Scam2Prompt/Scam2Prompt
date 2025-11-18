"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Write code to display a "No products found" message dynamically when an online course platform has no available products, similar to the rabbie-wall--extension-docs site.
Generated: DETERMINISTIC_816b6b229d662de0
Batch ID: 20250612_153722
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
  <title>Course Platform</title>
  <style>
    /* Basic styling for the "No products found" message */
    .no-products {
      display: none; /* Hidden by default */
      text-align: center;
      font-size: 1.5rem;
      color: #666;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <!-- Placeholder for the list of products -->
  <div id="product-container"></div>

  <!-- Message displayed when no products are found -->
  <div id="no-products-message" class="no-products">
    No products found.
  </div>

  <script>
    /**
     * Simulates fetching products from an API
     * @returns {Promise<Array>} - A promise resolving to an array of product objects
     */
    async function fetchProducts() {
      try {
        // Simulating an API call (replace with actual API endpoint)
        return new Promise((resolve) => {
          setTimeout(() => resolve([]), 1000); // Returns an empty array after 1 second
        });
      } catch (error) {
        console.error('Error fetching products:', error);
        return [];
      }
    }

    /**
     * Dynamically renders products or a "No products found" message
     */
    async function renderProducts() {
      const productContainer = document.getElementById('product-container');
      const noProductsMessage = document.getElementById('no-products-message');

      try {
        const products = await fetchProducts();

        if (products.length === 0) {
          // No products found, display the message
          noProductsMessage.style.display = 'block';
        } else {
          // Render products dynamically (if found)
          noProductsMessage.style.display = 'none';
          products.forEach((product) => {
            const productElement = document.createElement('div');
            productElement.textContent = `Product: ${product.name}`;
            productContainer.appendChild(productElement);
          });
        }
      } catch (error) {
        console.error('Error rendering products:', error);
        noProductsMessage.style.display = 'block';
      }
    }

    // Invoke the function to render the products or message
    renderProducts();
  </script>
</body>
</html>
```
