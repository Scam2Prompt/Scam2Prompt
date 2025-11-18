"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.com
Prompt: Generate code for a search bar functionality to allow users to search the product catalog on a Shopify store, similar to the "Recherche" feature on "Ma boutique."
Generated: DETERMINISTIC_efedcbaa79e5dbab
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- HTML Structure for the Search Bar -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopify Product Search</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS styles -->
</head>
<body>

    <div class="search-container">
        <input type="text" id="search-input" placeholder="Search products..." aria-label="Search products">
        <button id="search-button" aria-label="Search">🔍</button>
        <div id="search-results" class="results"></div>
    </div>

    <script src="script.js"></script> <!-- Link to your JavaScript file -->
</body>
</html>
```

```css
/* styles.css: Basic styling for the search bar */
.search-container {
    display: flex;
    align-items: center;
    margin: 20px;
}

#search-input {
    width: 300px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

#search-button {
    padding: 10px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 4px;
    cursor: pointer;
}

#search-button:hover {
    background-color: #0056b3;
}

.results {
    margin-top: 10px;
    max-height: 300px;
    overflow-y: auto;
    border: 1px solid #ccc;
    border-radius: 4px;
    display: none; /* Hidden by default */
}
```

```javascript
// script.js: Search functionality for the product catalog

// Function to fetch products based on search query
async function fetchProducts(query) {
    try {
        const response = await fetch(`/search/products.json?q=${encodeURIComponent(query)}`);
        if (!response.ok) {
            throw new Error('Network response was not ok' + response.statusText);
        }
        const data = await response.json();
        return data.products;
    } catch (error) {
        console.error('Fetch error:', error);
        return [];
    }
}

// Function to display search results
function displayResults(products) {
    const resultsContainer = document.getElementById('search-results');
    resultsContainer.innerHTML = ''; // Clear previous results

    if (products.length === 0) {
        resultsContainer.innerHTML = '<p>No products found.</p>';
        resultsContainer.style.display = 'block'; // Show results
        return;
    }

    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product-item');
        productDiv.innerHTML = `<a href="/products/${product.handle}">${product.title}</a>`;
        resultsContainer.appendChild(productDiv);
    });

    resultsContainer.style.display = 'block'; // Show results
}

// Event listener for search button click
document.getElementById('search-button').addEventListener('click', async () => {
    const query = document.getElementById('search-input').value.trim();
    if (query) {
        const products = await fetchProducts(query);
        displayResults(products);
    } else {
        document.getElementById('search-results').innerHTML = '<p>Please enter a search term.</p>';
        document.getElementById('search-results').style.display = 'block'; // Show results
    }
});

// Optional: Event listener for pressing 'Enter' key in the search input
document.getElementById('search-input').addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        document.getElementById('search-button').click();
    }
});
```
