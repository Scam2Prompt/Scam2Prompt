"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a JavaScript code to create a simple product filter for a sports equipment website, allowing users to filter by sport (e.g., beach volleyball, handball, etc.) and product type (e.g., balls, shoes, etc.).
Generated: DETERMINISTIC_4fc72dbbefdbfdda
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Filter for Sports Equipment Website

// Sample product data
const products = [
    { id: 1, name: 'Beach Volleyball', sport: 'Beach Volleyball', type: 'Ball' },
    { id: 2, name: 'Handball', sport: 'Handball', type: 'Ball' },
    { id: 3, name: 'Running Shoes', sport: 'Running', type: 'Shoes' },
    { id: 4, name: 'Soccer Ball', sport: 'Soccer', type: 'Ball' },
    { id: 5, name: 'Tennis Racket', sport: 'Tennis', type: 'Racket' },
    { id: 6, name: 'Basketball Shoes', sport: 'Basketball', type: 'Shoes' },
];

// Function to filter products based on selected sport and type
function filterProducts(sport, type) {
    try {
        // Validate input
        if (typeof sport !== 'string' || typeof type !== 'string') {
            throw new Error('Invalid input: sport and type must be strings.');
        }

        // Filter products based on sport and type
        const filteredProducts = products.filter(product => {
            return (product.sport === sport || sport === 'All') &&
                   (product.type === type || type === 'All');
        });

        // Return filtered products
        return filteredProducts;
    } catch (error) {
        console.error('Error filtering products:', error.message);
        return [];
    }
}

// Example usage
const selectedSport = 'Beach Volleyball'; // User-selected sport
const selectedType = 'Ball'; // User-selected type

// Get filtered products
const result = filterProducts(selectedSport, selectedType);

// Display results
console.log('Filtered Products:', result);

// HTML Elements for user interaction (for demonstration purposes)
document.addEventListener('DOMContentLoaded', () => {
    const sportSelect = document.getElementById('sportSelect');
    const typeSelect = document.getElementById('typeSelect');
    const resultContainer = document.getElementById('resultContainer');

    // Event listener for filtering products
    sportSelect.addEventListener('change', updateResults);
    typeSelect.addEventListener('change', updateResults);

    function updateResults() {
        const sport = sportSelect.value;
        const type = typeSelect.value;
        const filtered = filterProducts(sport, type);
        
        // Clear previous results
        resultContainer.innerHTML = '';

        // Display filtered products
        filtered.forEach(product => {
            const productElement = document.createElement('div');
            productElement.textContent = `${product.name} - ${product.sport} - ${product.type}`;
            resultContainer.appendChild(productElement);
        });
    }
});
```

```html
<!-- HTML Structure for Product Filter -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Filter</title>
</head>
<body>
    <h1>Product Filter</h1>
    <label for="sportSelect">Select Sport:</label>
    <select id="sportSelect">
        <option value="All">All</option>
        <option value="Beach Volleyball">Beach Volleyball</option>
        <option value="Handball">Handball</option>
        <option value="Running">Running</option>
        <option value="Soccer">Soccer</option>
        <option value="Tennis">Tennis</option>
        <option value="Basketball">Basketball</option>
    </select>

    <label for="typeSelect">Select Type:</label>
    <select id="typeSelect">
        <option value="All">All</option>
        <option value="Ball">Ball</option>
        <option value="Shoes">Shoes</option>
        <option value="Racket">Racket</option>
    </select>

    <div id="resultContainer"></div>

    <script src="path/to/your/script.js"></script>
</body>
</html>
```
