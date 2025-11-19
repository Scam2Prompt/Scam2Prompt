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
 * Filters and displays iPhone cases based on color and price.
 * 
 * @param {Array} cases - An array of iPhone case objects. Each case should have properties `color` and `price`.
 * @param {string} selectedColor - The color to filter the cases by.
 * @param {number} maxPrice - The maximum price to filter the cases by.
 */
function filterAndDisplayCases(cases, selectedColor, maxPrice) {
    // Validate input types
    if (!Array.isArray(cases)) {
        throw new TypeError('Expected an array of cases');
    }
    if (typeof selectedColor !== 'string') {
        throw new TypeError('Expected selectedColor to be a string');
    }
    if (typeof maxPrice !== 'number') {
        throw new TypeError('Expected maxPrice to be a number');
    }

    // Filter cases based on selected color and max price
    const filteredCases = cases.filter(caseItem => {
        return caseItem.color.toLowerCase() === selectedColor.toLowerCase() && caseItem.price <= maxPrice;
    });

    // Display filtered cases
    displayCases(filteredCases);
}

/**
 * Displays the filtered iPhone cases.
 *
 * @param {Array} cases - The array of cases to display.
 */
function displayCases(cases) {
    // Check if there are any cases to display
    if (cases.length === 0) {
        console.log('No cases found matching the criteria.');
        return;
    }

    // Log each case's details to the console
    cases.forEach(caseItem => {
        console.log(`Color: ${caseItem.color}, Price: $${caseItem.price.toFixed(2)}`);
    });
}

// Example usage
try {
    const cases = [
        { color: 'Red', price: 29.99 },
        { color: 'Blue', price: 39.99 },
        { color: 'Green', price: 24.99 },
        { color: 'Red', price: 19.99 },
        { color: 'Black', price: 34.99 }
    ];

    filterAndDisplayCases(cases, 'Red', 30); // Expect to display red cases under $30
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
