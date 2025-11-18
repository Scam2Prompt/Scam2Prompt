"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Generate code in JavaScript to create a dynamic product search interface for Brother sewing machines, allowing users to filter by type (e.g., overlock, coverstitch) and price range.
Generated: DETERMINISTIC_a63a451fc6acdf26
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for the product search interface
const html = `
<div id="search-interface">
    <h1>Brother Sewing Machines Search</h1>
    <div>
        <label for="type-filter">Filter by Type:</label>
        <select id="type-filter">
            <option value="">All</option>
            <option value="overlock">Overlock</option>
            <option value="coverstitch">Coverstitch</option>
        </select>
    </div>
    <div>
        <label for="price-min">Min Price:</label>
        <input type="number" id="price-min" placeholder="0" />
    </div>
    <div>
        <label for="price-max">Max Price:</label>
        <input type="number" id="price-max" placeholder="1000" />
    </div>
    <button id="search-button">Search</button>
    <div id="results"></div>
</div>
`;

// Append the HTML to the body
document.body.innerHTML += html;

// Sample data for Brother sewing machines
const products = [
    { id: 1, name: 'Brother 1034D', type: 'overlock', price: 299 },
    { id: 2, name: 'Brother 2340CV', type: 'coverstitch', price: 399 },
    { id: 3, name: 'Brother SE600', type: 'sewing', price: 599 },
    { id: 4, name: 'Brother 4234D', type: 'overlock', price: 399 },
    { id: 5, name: 'Brother 4234D', type: 'coverstitch', price: 479 },
];

// Function to filter products based on user input
const filterProducts = () => {
    // Retrieve filter values
    const typeFilter = document.getElementById('type-filter').value;
    const priceMin = parseFloat(document.getElementById('price-min').value) || 0;
    const priceMax = parseFloat(document.getElementById('price-max').value) || Infinity;

    // Validate price range
    if (priceMin < 0 || priceMax < priceMin) {
        alert('Please enter a valid price range.');
        return;
    }

    // Filter the products based on selected type and price range
    const filteredProducts = products.filter(product => {
        const typeMatch = typeFilter ? product.type === typeFilter : true;
        const priceMatch = product.price >= priceMin && product.price <= priceMax;
        return typeMatch && priceMatch;
    });

    // Display filtered products
    displayResults(filteredProducts);
};

// Function to display search results
const displayResults = (filteredProducts) => {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results

    if (filteredProducts.length === 0) {
        resultsDiv.innerHTML = '<p>No products found.</p>';
        return;
    }

    // Create and append product results to the results div
    filteredProducts.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.innerHTML = `<strong>${product.name}</strong> - $${product.price}`;
        resultsDiv.appendChild(productDiv);
    });
};

// Attach event listener to the search button
document.getElementById('search-button').addEventListener('click', filterProducts);
```
