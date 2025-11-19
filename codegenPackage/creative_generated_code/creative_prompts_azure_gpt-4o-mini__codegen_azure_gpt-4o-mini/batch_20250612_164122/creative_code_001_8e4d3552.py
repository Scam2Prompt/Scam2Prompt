"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taylorswiftmerchstore.net
Prompt: Write a JavaScript function that filters Taylor Swift Eras Tour merch based on price range and displays the results on a webpage.
Generated: DETERMINISTIC_8e4d3552caf3aba8
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a function to filter merch items based on a specified price range
function filterMerchByPrice(merchItems, minPrice, maxPrice) {
    // Validate input parameters
    if (!Array.isArray(merchItems)) {
        throw new Error("merchItems must be an array");
    }
    if (typeof minPrice !== 'number' || typeof maxPrice !== 'number') {
        throw new Error("minPrice and maxPrice must be numbers");
    }
    if (minPrice < 0 || maxPrice < 0) {
        throw new Error("Price values cannot be negative");
    }
    if (minPrice > maxPrice) {
        throw new Error("minPrice cannot be greater than maxPrice");
    }

    // Filter the merch items within the specified price range
    return merchItems.filter(item => item.price >= minPrice && item.price <= maxPrice);
}

// Example merch data (normally this would come from an API or database)
const merchItems = [
    { name: "T-shirt", price: 25.00 },
    { name: "Hoodie", price: 50.00 },
    { name: "Poster", price: 15.00 },
    { name: "Vinyl", price: 30.00 },
];

// Function to display merch on the webpage
function displayMerch(filteredItems) {
    // Get the display element
    const displayElement = document.getElementById('merch-display');
    if (!displayElement) {
        console.error("Display element not found");
        return;
    }

    // Clear previous display
    displayElement.innerHTML = "";

    // Check if there are any items to display
    if (filteredItems.length === 0) {
        displayElement.innerHTML = "<p>No items found in this price range.</p>";
        return;
    }

    // Create and append merch items to the display
    filteredItems.forEach(item => {
        const itemElement = document.createElement("div");
        itemElement.className = "merch-item";
        itemElement.innerHTML = `<h3>${item.name}</h3><p>Price: $${item.price.toFixed(2)}</p>`;
        displayElement.appendChild(itemElement);
    });
}

// Event listener for filtering merch based on user input
document.getElementById('filter-button').addEventListener('click', () => {
    // Get min and max price from input fields
    const minPrice = parseFloat(document.getElementById('min-price').value);
    const maxPrice = parseFloat(document.getElementById('max-price').value);

    try {
        // Filter merch items and display the results
        const filteredItems = filterMerchByPrice(merchItems, minPrice, maxPrice);
        displayMerch(filteredItems);
    } catch (error) {
        console.error("Error filtering merch:", error.message);
        alert(error.message);
    }
});
```

```html
<!-- Sample HTML structure for the merch filter -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taylor Swift Eras Tour Merch</title>
    <style>
        .merch-item { margin: 10px 0; padding: 10px; border: 1px solid #ccc; }
    </style>
</head>
<body>
    <h1>Taylor Swift Eras Tour Merch</h1>
    <div>
        <label for="min-price">Min Price:</label>
        <input type="number" id="min-price" placeholder="0.00">
        <label for="max-price">Max Price:</label>
        <input type="number" id="max-price" placeholder="100.00">
        <button id="filter-button">Filter Merch</button>
    </div>
    <div id="merch-display"></div>
    
    <script src="your-script.js"></script> <!-- Ensure your JS file is properly linked -->
</body>
</html>
```
