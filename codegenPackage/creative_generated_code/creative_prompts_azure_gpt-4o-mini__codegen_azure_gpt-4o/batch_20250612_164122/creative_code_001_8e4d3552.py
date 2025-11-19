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
// Function to filter merch items based on a price range and display results on a webpage
// This script assumes the presence of an HTML element with ID "results" to display output

/**
 * Filters merch items based on a price range.
 * @param {Array<Object>} merch - An array of merch objects with `name` and `price` properties.
 * @param {number} minPrice - The minimum price for the filter range.
 * @param {number} maxPrice - The maximum price for the filter range.
 */
function filterMerchByPrice(merch, minPrice, maxPrice) {
  try {
    // Validate input
    if (!Array.isArray(merch)) {
      throw new Error("Invalid merch data provided. Expected an array of objects.");
    }
    if (typeof minPrice !== "number" || typeof maxPrice !== "number") {
      throw new Error("Invalid price range. Both minPrice and maxPrice should be numbers.");
    }

    // Filter merch items based on price range
    const filteredMerch = merch.filter(
      (item) => item.price >= minPrice && item.price <= maxPrice
    );

    // Display results on the webpage
    const resultsElement = document.getElementById("results");
    if (!resultsElement) {
      throw new Error("Element with ID 'results' not found on the webpage.");
    }

    // Clear previous results
    resultsElement.innerHTML = "";

    // Check if there are any matching items
    if (filteredMerch.length === 0) {
      resultsElement.innerHTML = "<p>No merch items found in this price range.</p>";
    } else {
      // Create a list of filtered items
      const listElement = document.createElement("ul");
      filteredMerch.forEach((item) => {
        const listItem = document.createElement("li");
        listItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
        listElement.appendChild(listItem);
      });
      resultsElement.appendChild(listElement);
    }
  } catch (error) {
    // Log errors to the console for debugging
    console.error("Error in filterMerchByPrice function:", error.message);

    // Display error message on the webpage
    const resultsElement = document.getElementById("results");
    if (resultsElement) {
      resultsElement.innerHTML =
        "<p>An error occurred while filtering merch items. Please try again later.</p>";
    }
  }
}

// Example usage:
// HTML element with ID "results" should exist in the DOM, e.g., <div id="results"></div>
const merchItems = [
  { name: "Eras Tour T-Shirt", price: 35.0 },
  { name: "Eras Tour Hoodie", price: 65.0 },
  { name: "Eras Tour Poster", price: 25.0 },
  { name: "Eras Tour Vinyl", price: 45.0 },
];

// Call the function with a price range
filterMerchByPrice(merchItems, 30, 50);
```
