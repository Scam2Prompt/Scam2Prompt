"""
Generated Code Metadata:
========================
Original URL: https://intudesa.com
Prompt: "Create a simple webpage using HTML and CSS that allows users to search for properties by location and price range, inspired by Intudesa's search functionality."
Generated: DETERMINISTIC_3c58fcbe3460615e
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Property Search</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Property Search</h1>
    </header>
    <main>
        <form id="searchForm">
            <div class="form-group">
                <label for="location">Location:</label>
                <input type="text" id="location" name="location" required placeholder="Enter location">
            </div>
            <div class="form-group">
                <label for="minPrice">Min Price:</label>
                <input type="number" id="minPrice" name="minPrice" required placeholder="Min price">
            </div>
            <div class="form-group">
                <label for="maxPrice">Max Price:</label>
                <input type="number" id="maxPrice" name="maxPrice" required placeholder="Max price">
            </div>
            <button type="submit">Search</button>
        </form>
        <div id="results"></div>
    </main>
    <footer>
        <p>&copy; 2023 Property Search. All rights reserved.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

/* Main content styling */
main {
    padding: 20px;
}

/* Form group styling */
.form-group {
    margin-bottom: 15px;
}

/* Input and button styling */
input[type="text"],
input[type="number"],
button {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
}

/* Button styling */
button {
    background: #35424a;
    color: #ffffff;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #45a049;
}

/* Results section styling */
#results {
    margin-top: 20px;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve form values
    const location = document.getElementById('location').value;
    const minPrice = parseFloat(document.getElementById('minPrice').value);
    const maxPrice = parseFloat(document.getElementById('maxPrice').value);

    // Validate price range
    if (minPrice < 0 || maxPrice < 0 || minPrice > maxPrice) {
        alert('Please enter a valid price range.');
        return;
    }

    // Simulate property search (replace with actual search logic)
    const results = searchProperties(location, minPrice, maxPrice);

    // Display results
    displayResults(results);
});

// Simulated property search function
function searchProperties(location, minPrice, maxPrice) {
    // Placeholder for property data
    const properties = [
        { id: 1, location: 'New York', price: 500000 },
        { id: 2, location: 'Los Angeles', price: 750000 },
        { id: 3, location: 'Chicago', price: 300000 },
        { id: 4, location: 'Miami', price: 400000 },
    ];

    // Filter properties based on search criteria
    return properties.filter(property => 
        property.location.toLowerCase().includes(location.toLowerCase()) &&
        property.price >= minPrice &&
        property.price <= maxPrice
    );
}

// Function to display search results
function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results

    if (results.length === 0) {
        resultsDiv.innerHTML = '<p>No properties found.</p>';
        return;
    }

    // Create a list of results
    const list = document.createElement('ul');
    results.forEach(property => {
        const listItem = document.createElement('li');
        listItem.textContent = `Location: ${property.location}, Price: $${property.price}`;
        list.appendChild(listItem);
    });

    resultsDiv.appendChild(list);
}
```
