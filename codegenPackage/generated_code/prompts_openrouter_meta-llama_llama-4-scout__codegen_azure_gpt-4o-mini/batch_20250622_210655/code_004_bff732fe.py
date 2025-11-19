"""
Generated Code Metadata:
========================
Original URL: https://careandsmile.ae
Prompt: Write a code snippet in JavaScript to implement a search functionality on an e-commerce website like Care and Smile, which has a large collection of products across various categories.
Generated: DETERMINISTIC_bff732fe3361ee07
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Search Functionality for E-commerce Website

// Sample product data (in a real application, this would likely come from a database)
const products = [
    { id: 1, name: "Organic Face Cream", category: "Skincare", price: 29.99 },
    { id: 2, name: "Herbal Shampoo", category: "Haircare", price: 19.99 },
    { id: 3, name: "Natural Lip Balm", category: "Skincare", price: 9.99 },
    { id: 4, name: "Aloe Vera Gel", category: "Skincare", price: 15.99 },
    { id: 5, name: "Tea Tree Oil", category: "Essential Oils", price: 12.99 },
    // ... more products
];

/**
 * Searches for products based on a search term.
 * @param {string} searchTerm - The term to search for in product names.
 * @returns {Array} - An array of products that match the search term.
 */
function searchProducts(searchTerm) {
    // Validate input
    if (typeof searchTerm !== 'string') {
        console.error("Invalid input: searchTerm must be a string.");
        return [];
    }

    // Normalize the search term to lower case for case-insensitive search
    const normalizedTerm = searchTerm.toLowerCase();

    // Filter products based on the search term
    const filteredProducts = products.filter(product => 
        product.name.toLowerCase().includes(normalizedTerm)
    );

    return filteredProducts;
}

/**
 * Displays the search results on the webpage.
 * @param {Array} results - The array of products to display.
 */
function displaySearchResults(results) {
    // Get the results container element
    const resultsContainer = document.getElementById('search-results');
    
    // Clear previous results
    resultsContainer.innerHTML = '';

    // Check if there are results to display
    if (results.length === 0) {
        resultsContainer.innerHTML = '<p>No products found.</p>';
        return;
    }

    // Create and append product elements to the results container
    results.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product-item';
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>Category: ${product.category}</p>
            <p>Price: $${product.price.toFixed(2)}</p>
        `;
        resultsContainer.appendChild(productElement);
    });
}

// Event listener for the search input
document.getElementById('search-input').addEventListener('input', (event) => {
    const searchTerm = event.target.value;
    const results = searchProducts(searchTerm);
    displaySearchResults(results);
});
```

```html
<!-- HTML Structure for Search Functionality -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Product Search</title>
    <style>
        /* Basic styles for the search results */
        #search-results {
            margin-top: 20px;
        }
        .product-item {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Product Search</h1>
    <input type="text" id="search-input" placeholder="Search for products..." />
    <div id="search-results"></div>

    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```
