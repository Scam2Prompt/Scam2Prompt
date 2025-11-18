"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Write JavaScript code to dynamically filter car accessories by generation and type, mimicking the search functionality on the Tuning Design website.
Generated: DETERMINISTIC_e53fea744ad14cfa
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CarAccessoryFilter.js

// Sample data representing car accessories
const carAccessories = [
    { id: 1, name: 'Sport Air Filter', type: 'Air Filter', generation: 'A' },
    { id: 2, name: 'Performance Brake Pads', type: 'Brake Pads', generation: 'B' },
    { id: 3, name: 'Turbocharger', type: 'Turbo', generation: 'A' },
    { id: 4, name: 'Sport Exhaust System', type: 'Exhaust', generation: 'C' },
    { id: 5, name: 'Lowering Springs', type: 'Suspension', generation: 'B' },
    // Add more accessories as necessary
];

// Function to filter accessories based on selected generation and type
function filterAccessories(generation, type) {
    try {
        // Validate inputs
        if (!generation && !type) {
            throw new Error("At least one filter must be provided.");
        }

        // Filter the accessories
        const filteredAccessories = carAccessories.filter(accessory => {
            const matchesGeneration = generation ? accessory.generation === generation : true;
            const matchesType = type ? accessory.type === type : true;
            return matchesGeneration && matchesType;
        });

        return filteredAccessories;
    } catch (error) {
        console.error("Error filtering accessories:", error.message);
        return [];
    }
}

// Example of using the filter function
document.addEventListener('DOMContentLoaded', () => {
    const generationSelect = document.getElementById('generation');
    const typeSelect = document.getElementById('type');
    const resultsContainer = document.getElementById('results');

    // Event listener for when the user changes the filters
    function updateResults() {
        const selectedGeneration = generationSelect.value;
        const selectedType = typeSelect.value;
        const results = filterAccessories(selectedGeneration, selectedType);

        // Clear previous results
        resultsContainer.innerHTML = '';

        // Display filtered results
        if (results.length > 0) {
            results.forEach(accessory => {
                const accessoryItem = document.createElement('div');
                accessoryItem.textContent = `${accessory.name} - ${accessory.type} (Generation: ${accessory.generation})`;
                resultsContainer.appendChild(accessoryItem);
            });
        } else {
            resultsContainer.textContent = 'No accessories found for the selected filters.';
        }
    }

    // Attach event listeners to the filter selects
    generationSelect.addEventListener('change', updateResults);
    typeSelect.addEventListener('change', updateResults);
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Accessories Filter</title>
    <script src="CarAccessoryFilter.js" defer></script>
</head>
<body>
    <h1>Filter Car Accessories</h1>
    <label for="generation">Select Generation:</label>
    <select id="generation">
        <option value="">All</option>
        <option value="A">Generation A</option>
        <option value="B">Generation B</option>
        <option value="C">Generation C</option>
    </select>

    <label for="type">Select Type:</label>
    <select id="type">
        <option value="">All</option>
        <option value="Air Filter">Air Filter</option>
        <option value="Brake Pads">Brake Pads</option>
        <option value="Turbo">Turbo</option>
        <option value="Exhaust">Exhaust</option>
        <option value="Suspension">Suspension</option>
    </select>

    <h2>Results:</h2>
    <div id="results"></div>
</body>
</html>
```
