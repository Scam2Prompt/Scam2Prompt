"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code to implement a search bar for an e-commerce site that allows users to filter products by price range and category, similar to the functionality described on "asacanelbrazzz."
Generated: DETERMINISTIC_dce782b5f0428a19
Batch ID: 20250612_145249
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
    <title>E-commerce Search Bar</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="search-bar">
        <h1>Product Search</h1>
        <form id="searchForm" onsubmit="return handleSearch(event)">
            <input type="text" id="searchInput" placeholder="Search products..." required>
            <select id="categorySelect">
                <option value="">All Categories</option>
                <option value="electronics">Electronics</option>
                <option value="clothing">Clothing</option>
                <option value="home">Home</option>
                <option value="books">Books</option>
            </select>
            <label for="minPrice">Min Price:</label>
            <input type="number" id="minPrice" placeholder="0" min="0" step="0.01">
            <label for="maxPrice">Max Price:</label>
            <input type="number" id="maxPrice" placeholder="1000" min="0" step="0.01">
            <button type="submit">Search</button>
        </form>
    </div>

    <div id="resultsContainer"></div>

    <script>
        // Handle search form submission
        function handleSearch(event) {
            event.preventDefault(); // Prevent the default form submission

            // Get values from the form
            const query = document.getElementById('searchInput').value.trim();
            const category = document.getElementById('categorySelect').value;
            const minPrice = parseFloat(document.getElementById('minPrice').value) || 0;
            const maxPrice = parseFloat(document.getElementById('maxPrice').value) || Infinity;

            // Fetch and display products according to search criteria
            fetchProducts(query, category, minPrice, maxPrice);
        }

        // Fetch products from the server (mock API call)
        async function fetchProducts(query, category, minPrice, maxPrice) {
            try {
                // Simulated API endpoint; replace with actual endpoint
                const response = await fetch('/api/products'); 
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const products = await response.json();
                const filteredProducts = filterProducts(products, query, category, minPrice, maxPrice);
                displayResults(filteredProducts);
            } catch (error) {
                console.error('Error fetching products:', error);
                alert('There was an error fetching products. Please try again later.');
            }
        }

        // Filter products based on search criteria
        function filterProducts(products, query, category, minPrice, maxPrice) {
            return products.filter(product => {
                const matchesQuery = product.name.toLowerCase().includes(query.toLowerCase());
                const matchesCategory = !category || product.category === category;
                const matchesPrice = product.price >= minPrice && product.price <= maxPrice;
                return matchesQuery && matchesCategory && matchesPrice;
            });
        }

        // Display search results
        function displayResults(products) {
            const resultsContainer = document.getElementById('resultsContainer');
            resultsContainer.innerHTML = ''; // Clear previous results

            if (products.length === 0) {
                resultsContainer.innerHTML = '<p>No products found.</p>';
                return;
            }

            // Create product elements
            products.forEach(product => {
                const productElement = document.createElement('div');
                productElement.classList.add('product');
                productElement.innerHTML = `
                    <h2>${product.name}</h2>
                    <p>Category: ${product.category}</p>
                    <p>Price: $${product.price.toFixed(2)}</p>
                `;
                resultsContainer.appendChild(productElement);
            });
        }
    </script>
    <style>
        /* Basic styling for the search bar and results */
        .search-bar {
            margin: 20px;
        }
        .product {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px 0;
        }
    </style>
</body>
</html>
```
