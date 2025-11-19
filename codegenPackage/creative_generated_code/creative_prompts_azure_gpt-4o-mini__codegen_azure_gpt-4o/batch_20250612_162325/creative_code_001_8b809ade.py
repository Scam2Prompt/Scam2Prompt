"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://montres.pl
Prompt: Write a JavaScript function to filter and display men's watches from Montres.pl based on the selected style, such as sporty or classic.
Generated: DETERMINISTIC_8b809ade781c9069
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and displays men's watches from Montres.pl based on the selected style.
 *
 * @param {Array} watches - Array of watch objects to filter. Each object should have properties: name, gender, style, and price.
 * @param {string} selectedStyle - The style to filter by (e.g., 'sporty', 'classic').
 * @returns {Array} - An array of filtered watch objects matching the selected style.
 */
function filterMensWatches(watches, selectedStyle) {
  try {
    // Validate input
    if (!Array.isArray(watches)) {
      throw new Error("Invalid input: watches should be an array.");
    }
    if (typeof selectedStyle !== "string" || selectedStyle.trim() === "") {
      throw new Error("Invalid input: selectedStyle should be a non-empty string.");
    }

    // Filter watches based on gender and style
    const filteredWatches = watches.filter(
      (watch) =>
        watch.gender === "men" &&
        watch.style.toLowerCase() === selectedStyle.toLowerCase()
    );

    // Display the filtered watches (for demonstration purposes)
    console.log("Filtered Watches:");
    filteredWatches.forEach((watch) => {
      console.log(`Name: ${watch.name}, Style: ${watch.style}, Price: $${watch.price}`);
    });

    // Return the filtered watches
    return filteredWatches;
  } catch (error) {
    // Handle errors gracefully
    console.error(`Error: ${error.message}`);
    return [];
  }
}

/* Example usage */

// Sample data
const watchCatalog = [
  { name: "Sporty Watch A", gender: "men", style: "sporty", price: 150 },
  { name: "Classic Watch B", gender: "men", style: "classic", price: 200 },
  { name: "Sporty Watch C", gender: "women", style: "sporty", price: 180 },
  { name: "Classic Watch D", gender: "men", style: "classic", price: 220 },
];

// Filter for sporty men's watches
const sportyMensWatches = filterMensWatches(watchCatalog, "sporty");

// Filter for classic men's watches
const classicMensWatches = filterMensWatches(watchCatalog, "classic");
```
