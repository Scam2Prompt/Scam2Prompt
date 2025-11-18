"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Create a script in JavaScript to filter products by category (e.g., "Electrice," "Constructii," "Gradina") and display the filtered results dynamically on a webpage.
Generated: DETERMINISTIC_d299f3c06144fe3a
Batch ID: 20250612_153517
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
    <title>Product Filter</title>
    <style>
        /* Basic styling for product list and filter buttons */
        #product-list {
            margin-top: 20px;
        }

        .product {
            border: 1px solid #ddd;
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
        }

        .filter-button {
            margin: 5px;
            padding: 10px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Product Filter</h1>
    <div>
        <button class="filter-button" onclick="filterProducts('Electrice')">Electrice</button>
        <button class="filter-button" onclick="filterProducts('Constructii')">Constructii</button>
        <button class="filter-button" onclick="filterProducts('Gradina')">Gradina</button>
        <button class="filter-button" onclick="filterProducts('')">Show All</button>
    </div>
    <div id="product-list"></div>

    <script>
        // Sample product data
        const products = [
            { name: 'Electric Drill', category: 'Electrice' },
            { name: 'Hammer', category: 'Constructii' },
            { name: 'Lawn Mower', category: 'Gradina' },
            { name: 'Screwdriver', category: 'Electrice' },
            { name: 'Garden Hoe', category: 'Gradina' }
        ];

        /**
         * Filters products by category and displays them on the webpage.
         * @param {string} category - The category to filter products by.
         */
        function filterProducts(category) {
            try {
                // Get the product list container
                const productList = document.getElementById('product-list');
                productList.innerHTML = ''; // Clear previous results
                
                // Filter products based on the selected category
                const filteredProducts = category ? 
                    products.filter(product => product.category === category) : 
                    products;

                // Display filtered products
                filteredProducts.forEach(product => {
                    const productDiv = document.createElement('div');
                    productDiv.className = 'product';
                    productDiv.textContent = product.name;
                    productList.appendChild(productDiv);
                });

                // Handle case if no products match the filter
                if (filteredProducts.length === 0) {
                    const noProductDiv = document.createElement('div');
                    noProductDiv.textContent = 'No products found in this category.';
                    productList.appendChild(noProductDiv);
                }
            } catch (error) {
                console.error('Error filtering products:', error);
                alert('An error occurred while filtering products. Please try again.');
            }
        }

        // Initial load of all products
        filterProducts('');
    </script>
</body>
</html>
```
