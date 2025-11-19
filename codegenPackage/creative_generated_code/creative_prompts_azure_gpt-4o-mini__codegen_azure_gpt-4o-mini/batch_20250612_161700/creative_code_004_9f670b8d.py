"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Design a user interface for a real estate website that features property listings and includes a search function for specific neighborhoods, as seen on Inmobiliaria Capri's platform.
Generated: DETERMINISTIC_9f670b8d1b4e0c4e
Batch ID: 20250612_161700
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
    <title>Real Estate Listings</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Inmobiliaria Capri</h1>
        <nav>
            <ul>
                <li><a href="#properties">Listings</a></li>
                <li><a href="#search">Search</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="search">
            <h2>Search for Properties</h2>
            <form id="searchForm" onsubmit="handleSearch(event)">
                <input type="text" id="searchInput" placeholder="Enter neighborhood..." required>
                <button type="submit">Search</button>
            </form>
            <div id="searchResults"></div>
        </section>

        <section id="properties">
            <h2>Available Listings</h2>
            <div id="propertyList">
                <!-- Property listings will be dynamically inserted here -->
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Inmobiliaria Capri. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the body and text */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #0077cc;
    color: white;
    padding: 15px 20px;
    text-align: center;
}

nav ul {
    list-style-type: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

main {
    padding: 20px;
}

h2 {
    border-bottom: 2px solid #0077cc;
    padding-bottom: 10px;
}

#searchResults {
    margin-top: 20px;
}

.property-card {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin: 10px 0;
}
```

```javascript
// script.js

// Sample property data, ideally this would come from a server
const properties = [
    { id: 1, neighborhood: "Downtown", description: "Beautiful apartment in the city center." },
    { id: 2, neighborhood: "Uptown", description: "Spacious house with a garden." },
    { id: 3, neighborhood: "Midtown", description: "Modern condo near public transport." },
    { id: 4, neighborhood: "Suburbs", description: "Quiet suburban home with great schools." },
];

/**
 * Handles the search functionality for properties based on neighborhood input.
 * @param {Event} event - The event triggered by form submission.
 */
function handleSearch(event) {
    event.preventDefault(); // Prevent default form submission
    const input = document.getElementById('searchInput').value.toLowerCase();
    const results = properties.filter(prop => prop.neighborhood.toLowerCase().includes(input));
    displayResults(results);
}

/**
 * Displays the search results on the page.
 * @param {Array} results - Array of property objects matching the search.
 */
function displayResults(results) {
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = ''; // Clear previous results

    if (results.length === 0) {
        resultsContainer.innerHTML = '<p>No properties found.</p>';
        return;
    }

    results.forEach(prop => {
        const propertyCard = document.createElement('div');
        propertyCard.classList.add('property-card');
        propertyCard.innerHTML = `<h3>${prop.neighborhood}</h3><p>${prop.description}</p>`;
        resultsContainer.appendChild(propertyCard);
    });
}

// Initial rendering of all properties
function renderProperties() {
    const propertyList = document.getElementById('propertyList');
    properties.forEach(prop => {
        const propertyCard = document.createElement('div');
        propertyCard.classList.add('property-card');
        propertyCard.innerHTML = `<h3>${prop.neighborhood}</h3><p>${prop.description}</p>`;
        propertyList.appendChild(propertyCard);
    });
}

// Initialize the listings on page load
document.addEventListener("DOMContentLoaded", renderProperties);
```
