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

**index.html**
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
        <form id="search-form">
            <label for="location">Location:</label>
            <input type="text" id="location" name="location" required>

            <label for="min-price">Min Price:</label>
            <input type="number" id="min-price" name="min-price" min="0" required>

            <label for="max-price">Max Price:</label>
            <input type="number" id="max-price" name="max-price" min="0" required>

            <button id="search-btn">Search</button>
        </form>
        <div id="search-results"></div>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

#search-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 0.5em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    margin-bottom: 0.5em;
}

input[type="text"], input[type="number"] {
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
}

button {
    padding: 0.5em 1em;
    background-color: #333;
    color: #fff;
    border: none;
    border-radius: 0.5em;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}

#search-results {
    padding: 1em;
}
```

**script.js**
```javascript
// Get the search form and results elements
const searchForm = document.getElementById('search-form');
const searchResults = document.getElementById('search-results');

// Add event listener to the search form
searchForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the search form data
    const location = document.getElementById('location').value.trim();
    const minPrice = parseInt(document.getElementById('min-price').value);
    const maxPrice = parseInt(document.getElementById('max-price').value);

    // Validate the search form data
    if (isNaN(minPrice) || isNaN(maxPrice)) {
        alert('Invalid price range');
        return;
    }

    if (location === '') {
        alert('Please enter a location');
        return;
    }

    if (minPrice >= maxPrice) {
        alert('Min price must be less than max price');
        return;
    }

    // Simulate a search API call (replace with actual API call)
    const properties = [
        { id: 1, location: 'New York', price: 100000 },
        { id: 2, location: 'New York', price: 200000 },
        { id: 3, location: 'Los Angeles', price: 300000 },
        { id: 4, location: 'Chicago', price: 400000 },
    ];

    const filteredProperties = properties.filter((property) => {
        return property.location.toLowerCase().includes(location.toLowerCase()) &&
               property.price >= minPrice && property.price <= maxPrice;
    });

    // Display the search results
    searchResults.innerHTML = '';
    if (filteredProperties.length > 0) {
        filteredProperties.forEach((property) => {
            const propertyHTML = `
                <div>
                    <h2>Property ${property.id}</h2>
                    <p>Location: ${property.location}</p>
                    <p>Price: $${property.price}</p>
                </div>
            `;
            searchResults.insertAdjacentHTML('beforeend', propertyHTML);
        });
    } else {
        searchResults.innerHTML = '<p>No properties found</p>';
    }
});
```
