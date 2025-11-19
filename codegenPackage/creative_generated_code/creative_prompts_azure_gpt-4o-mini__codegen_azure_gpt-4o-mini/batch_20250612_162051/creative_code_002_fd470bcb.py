"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehiletes.com
Prompt: Create a JavaScript application that allows users to search for and book excursions in Mexico, highlighting the cultural and natural experiences provided by Rehiletes.
Generated: DETERMINISTIC_fd470bcb2fd5a54d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// excursions.js

// Excursion class to represent individual excursions
class Excursion {
    constructor(id, name, description, location, price, available) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.location = location;
        this.price = price;
        this.available = available;
    }
}

// Sample data for excursions
const excursions = [
    new Excursion(1, "Cenote Diving", "Explore the beautiful cenotes of Mexico.", "Yucatan", 150, true),
    new Excursion(2, "Cultural Tour of Oaxaca", "Discover the rich culture of Oaxaca.", "Oaxaca", 100, true),
    new Excursion(3, "Tulum Ruins", "Visit the ancient ruins overlooking the Caribbean.", "Tulum", 80, false),
];

// Function to search for excursions based on query
function searchExcursions(query) {
    if (typeof query !== 'string') {
        throw new Error("Query must be a string.");
    }
    
    return excursions.filter(excursion => 
        excursion.name.toLowerCase().includes(query.toLowerCase()) ||
        excursion.description.toLowerCase().includes(query.toLowerCase())
    );
}

// Function to book an excursion by ID
function bookExcursion(id) {
    const excursion = excursions.find(exc => exc.id === id);
    if (!excursion) {
        throw new Error("Excursion not found.");
    }
    if (!excursion.available) {
        throw new Error("Excursion is not available for booking.");
    }

    excursion.available = false; // Mark excursion as booked
    return `Successfully booked ${excursion.name} for $${excursion.price}.`;
}

// Event listeners for user interface
document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const query = document.getElementById("searchQuery").value;
    
    try {
        const results = searchExcursions(query);
        displayResults(results);
    } catch (error) {
        alert(`Error: ${error.message}`);
    }
});

document.getElementById("results").addEventListener("click", function(event) {
    if (event.target.classList.contains("book-button")) {
        const id = parseInt(event.target.dataset.id);
        
        try {
            const message = bookExcursion(id);
            alert(message);
        } catch (error) {
            alert(`Error: ${error.message}`);
        }
    }
});

// Function to display search results in the UI
function displayResults(results) {
    const resultsContainer = document.getElementById("results");
    resultsContainer.innerHTML = ""; // Clear previous results

    if (results.length === 0) {
        resultsContainer.innerHTML = "<p>No excursions found.</p>";
        return;
    }

    results.forEach(excursion => {
        const excursionElement = document.createElement("div");
        excursionElement.classList.add("excursion-item");
        excursionElement.innerHTML = `
            <h3>${excursion.name}</h3>
            <p>${excursion.description}</p>
            <p>Location: ${excursion.location}</p>
            <p>Price: $${excursion.price}</p>
            <p>${excursion.available ? "Available" : "Not Available"}</p>
            <button class="book-button" data-id="${excursion.id}" ${!excursion.available ? 'disabled' : ''}>Book</button>
        `;
        resultsContainer.appendChild(excursionElement);
    });
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Excursion Booking</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Excursion Booking in Mexico</h1>
    <form id="searchForm">
        <input type="text" id="searchQuery" placeholder="Search for excursions..." required>
        <button type="submit">Search</button>
    </form>

    <div id="results"></div>

    <script src="excursions.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 20px;
}

h1 {
    color: #333;
}

.excursion-item {
    border: 1px solid #ccc;
    margin: 10px 0;
    padding: 15px;
}

button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}

button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}
```
