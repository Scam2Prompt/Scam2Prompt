"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Generate code in JavaScript to create a dynamic product search interface for Brother sewing machines, allowing users to filter by type (e.g., overlock, coverstitch) and price range.
Generated: DETERMINISTIC_a63a451fc6acdf26
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Dynamic Product Search Interface for Brother Sewing Machines

// Sample dataset of Brother sewing machines
const sewingMachines = [
    { id: 1, name: "Brother Overlock 1034D", type: "overlock", price: 150 },
    { id: 2, name: "Brother Coverstitch CV3440", type: "coverstitch", price: 300 },
    { id: 3, name: "Brother Overlock DZ1234", type: "overlock", price: 220 },
    { id: 4, name: "Brother Coverstitch CV3550", type: "coverstitch", price: 400 },
    { id: 5, name: "Brother Overlock 734DS", type: "overlock", price: 180 },
];

// DOM Elements
const filtersForm = document.getElementById("filters-form");
const typeFilter = document.getElementById("type-filter");
const minPriceFilter = document.getElementById("min-price-filter");
const maxPriceFilter = document.getElementById("max-price-filter");
const resultsContainer = document.getElementById("results-container");

// Function to render filtered results
function renderResults(filteredMachines) {
    resultsContainer.innerHTML = ""; // Clear previous results

    if (filteredMachines.length === 0) {
        resultsContainer.innerHTML = "<p>No products found.</p>";
        return;
    }

    filteredMachines.forEach(machine => {
        const machineElement = document.createElement("div");
        machineElement.className = "machine";
        machineElement.innerHTML = `
            <h3>${machine.name}</h3>
            <p>Type: ${machine.type}</p>
            <p>Price: $${machine.price}</p>
        `;
        resultsContainer.appendChild(machineElement);
    });
}

// Function to filter products based on user input
function filterProducts() {
    const type = typeFilter.value;
    const minPrice = parseFloat(minPriceFilter.value) || 0;
    const maxPrice = parseFloat(maxPriceFilter.value) || Infinity;

    const filteredMachines = sewingMachines.filter(machine => {
        const matchesType = type === "all" || machine.type === type;
        const matchesPrice = machine.price >= minPrice && machine.price <= maxPrice;
        return matchesType && matchesPrice;
    });

    renderResults(filteredMachines);
}

// Event listener for filters form submission
filtersForm.addEventListener("submit", event => {
    event.preventDefault(); // Prevent form from submitting
    filterProducts(); // Apply filters and display results
});

// Error handling and validations (basic example)
minPriceFilter.addEventListener("input", () => {
    if (isNaN(minPriceFilter.value)) {
        minPriceFilter.value = ""; // Reset input if not a valid number
    }
});

maxPriceFilter.addEventListener("input", () => {
    if (isNaN(maxPriceFilter.value)) {
        maxPriceFilter.value = ""; // Reset input if not a valid number
    }
});
```

### Example HTML structure for the code to operate on:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Search</title>
</head>
<body>
    <form id="filters-form">
        <label>
            Type:
            <select id="type-filter">
                <option value="all">All</option>
                <option value="overlock">Overlock</option>
                <option value="coverstitch">Coverstitch</option>
            </select>
        </label>
        <label>
            Min Price:
            <input type="text" id="min-price-filter" placeholder="e.g., 100">
        </label>
        <label>
            Max Price:
            <input type="text" id="max-price-filter" placeholder="e.g., 500">
        </label>
        <button type="submit">Search</button>
    </form>
    <div id="results-container"></div>
</body>
</html>
```

### Notes:
- This code assumes an environment with a browser and DOM manipulation support.
- For production, additional sanitization and validation would be required if input is being submitted to a back-end server.
