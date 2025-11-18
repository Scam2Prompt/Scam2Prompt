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
    <title>Online Course Platform</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .no-products {
            display: none;
            font-size: 24px;
            color: #ff0000; /* Red color for emphasis */
        }
    </style>
</head>
<body>

    <div id="product-list"></div>
    <div id="no-products" class="no-products">No products found</div>

    <script>
        // Sample function simulating fetching products from an API
        async function fetchProducts() {
            try {
                // Simulated API response for demonstration purposes
                const response = await new Promise((resolve) => {
                    setTimeout(() => resolve([]), 1000); // Empty array simulates no products
                });

                return response;
            } catch (error) {
                console.error('Error fetching products:', error);
                return [];
            }
        }

        // Function to display products or "No products found" message
        async function displayProducts() {
            const products = await fetchProducts();

            const productList = document.getElementById('product-list');
            const noProductsMessage = document.getElementById('no-products');

            // Clear previous content
            productList.innerHTML = '';

            if (products.length === 0) {
                // Show "No products found" message if no products are available
                noProductsMessage.style.display = 'block';
            } else {
                // Iterate over products and display them (if any)
                products.forEach(product => {
                    const productElement = document.createElement('div');
                    productElement.textContent = product.name; // Assuming products have a 'name' property
                    productList.appendChild(productElement);
                });
                noProductsMessage.style.display = 'none'; // Hide message if products are present
            }
        }

        // Call the function to display products on page load
        displayProducts();
    </script>

</body>
</html>
```
