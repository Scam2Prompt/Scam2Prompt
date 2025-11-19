"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Create a JavaScript function to filter and display iPhone cases based on color and price, inspired by the product listings on Glisten's website.
Generated: DETERMINISTIC_d3b7c2edf65ec0c2
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters a list of iPhone cases based on color and price.
 * 
 * @param {Array} cases - Array of iPhone case objects. Each object should have `name`, `color`, and `price` properties.
 * @param {string} color - The desired color to filter by (e.g., 'black', 'red').
 * @param {number} maxPrice - The maximum price to filter by.
 * @returns {Array} - Array of filtered iPhone case objects that match the criteria.
 */
function filterCasesByColorAndPrice(cases, color, maxPrice) {
    try {
        // Validate input parameters
        if (!Array.isArray(cases)) {
            throw new Error("`cases` must be an array.");
        }
        if (typeof color !== 'string') {
            throw new Error("`color` must be a string.");
        }
        if (typeof maxPrice !== 'number' || maxPrice <= 0) {
            throw new Error("`maxPrice` must be a positive number.");
        }

        // Filter cases by color and price criteria
        const filteredCases = cases.filter((item) => {
            // Ensure item has required properties before filtering
            return (
                item.color?.toLowerCase() === color.toLowerCase() && 
                item.price <= maxPrice
            );
        });

        // Return the filtered results
        return filteredCases;

    } catch (error) {
        console.error("Error filtering cases:", error.message);
        return [];
    }
}

// Example usage
const iPhoneCases = [
    { name: "Slim Black Case", color: "black", price: 19.99 },
    { name: "Luxury Gold Case", color: "gold", price: 34.99 },
    { name: "Red Durable Case", color: "red", price: 24.99 },
    { name: "Blue Silicone Case", color: "blue", price: 14.99 },
];

const filteredResults = filterCasesByColorAndPrice(iPhoneCases, "red", 25.00);
console.log("Filtered Results:", filteredResults);

/*
Expected Output:
Filtered Results: [
    { name: "Red Durable Case", color: "red", price: 24.99 }
]
*/
```
