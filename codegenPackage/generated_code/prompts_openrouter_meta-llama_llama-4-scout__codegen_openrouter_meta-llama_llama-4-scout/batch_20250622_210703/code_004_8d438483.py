"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Create a basic webpage using HTML, CSS, and JavaScript that allows users to search and filter serviced apartments based on location, price range, and number of bedrooms, similar to the functionality on the Dunhill Serviced and Furnished Apartments website.
Generated: DETERMINISTIC_8d4384835a33fdc9
Batch ID: 20250622_210703
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
    <title>Serviced Apartments Search</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Serviced Apartments Search</h1>
    </header>
    <main>
        <form id="search-form">
            <label for="location">Location:</label>
            <input type="text" id="location" name="location"><br><br>
            <label for="price-range">Price Range:</label>
            <input type="number" id="min-price" name="min-price" placeholder="Min Price">
            <input type="number" id="max-price" name="max-price" placeholder="Max Price"><br><br>
            <label for="bedrooms">Number of Bedrooms:</label>
            <select id="bedrooms" name="bedrooms">
                <option value="">Select</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
            </select><br><br>
            <button id="search-btn">Search</button>
        </form>
        <div id="apartments-container"></div>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #f0f0f0;
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
    background-color: #f0f0f0;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 0.5em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 0.5em;
}

input, select {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
}

button {
    background-color: #4CAF50;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 0.5em;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

#apartments-container {
    margin-top: 2em;
}

.apartment {
    background-color: #f0f0f0;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 0.5em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 1em;
}

.apartment h2 {
    margin-top: 0;
}
```

**script.js**
```javascript
// Sample apartment data
const apartments = [
    { id: 1, location: "New York", price: 1000, bedrooms: 1 },
    { id: 2, location: "Los Angeles", price: 1500, bedrooms: 2 },
    { id: 3, location: "Chicago", price: 800, bedrooms: 1 },
    { id: 4, location: "New York", price: 1200, bedrooms: 2 },
    { id: 5, location: "Houston", price: 1800, bedrooms: 3 },
];

// Get elements
const searchForm = document.getElementById("search-form");
const apartmentsContainer = document.getElementById("apartments-container");

// Function to filter apartments
function filterApartments(location, minPrice, maxPrice, bedrooms) {
    return apartments.filter(apartment => {
        return (
            (location === "" || apartment.location.toLowerCase().includes(location.toLowerCase())) &&
            (minPrice === "" || apartment.price >= minPrice) &&
            (maxPrice === "" || apartment.price <= maxPrice) &&
            (bedrooms === "" || apartment.bedrooms === parseInt(bedrooms))
        );
    });
}

// Function to render apartments
function renderApartments(apartments) {
    apartmentsContainer.innerHTML = "";
    apartments.forEach(apartment => {
        const apartmentHTML = `
            <div class="apartment">
                <h2>${apartment.location}</h2>
                <p>Price: $${apartment.price}</p>
                <p>Bedrooms: ${apartment.bedrooms}</p>
            </div>
        `;
        apartmentsContainer.insertAdjacentHTML("beforeend", apartmentHTML);
    });
}

// Add event listener to search form
searchForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const location = document.getElementById("location").value;
    const minPrice = document.getElementById("min-price").value;
    const maxPrice = document.getElementById("max-price").value;
    const bedrooms = document.getElementById("bedrooms").value;
    const filteredApartments = filterApartments(location, minPrice, maxPrice, bedrooms);
    renderApartments(filteredApartments);
});

// Render all apartments on page load
renderApartments(apartments);
```
