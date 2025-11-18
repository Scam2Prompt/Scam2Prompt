"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Develop a JavaScript-based comparison tool for real estate listings on sunnyhurghada.com, allowing users to compare properties by size, price, and location.
Generated: DETERMINISTIC_e94e5b135dd88bd8
Batch ID: 20250612_153224
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
    <title>Real Estate Comparison Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

<h1>Real Estate Comparison Tool</h1>
<form id="comparisonForm">
    <label for="property1">Select Property 1:</label>
    <select id="property1" required>
        <option value="">--Select a Property--</option>
        <!-- Options will be populated dynamically -->
    </select>

    <label for="property2">Select Property 2:</label>
    <select id="property2" required>
        <option value="">--Select a Property--</option>
        <!-- Options will be populated dynamically -->
    </select>

    <button type="submit">Compare</button>
</form>

<div id="error" class="error"></div>
<table id="comparisonTable" style="display:none;">
    <thead>
        <tr>
            <th>Feature</th>
            <th>Property 1</th>
            <th>Property 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Size (sq ft)</td>
            <td id="size1"></td>
            <td id="size2"></td>
        </tr>
        <tr>
            <td>Price ($)</td>
            <td id="price1"></td>
            <td id="price2"></td>
        </tr>
        <tr>
            <td>Location</td>
            <td id="location1"></td>
            <td id="location2"></td>
        </tr>
    </tbody>
</table>

<script>
// Sample data representing real estate listings from sunnyhurghada.com
const properties = [
    { id: 1, name: 'Luxury Villa', size: 2500, price: 500000, location: 'Hurgada Beach' },
    { id: 2, name: 'Modern Apartment', size: 1200, price: 200000, location: 'City Center' },
    { id: 3, name: 'Cozy Studio', size: 600, price: 80000, location: 'Downtown' }
];

// Populate the select elements with property options
function populateProperties() {
    const property1Select = document.getElementById('property1');
    const property2Select = document.getElementById('property2');

    properties.forEach(property => {
        const option1 = new Option(property.name, property.id);
        const option2 = new Option(property.name, property.id);
        property1Select.add(option1);
        property2Select.add(option2);
    });
}

// Compare selected properties and display results
function compareProperties(event) {
    event.preventDefault(); // Prevent form submission

    const property1Id = parseInt(document.getElementById('property1').value);
    const property2Id = parseInt(document.getElementById('property2').value);
    const errorDiv = document.getElementById('error');

    // Clear previous error messages
    errorDiv.textContent = '';

    // Validate selections
    if (isNaN(property1Id) || isNaN(property2Id) || property1Id === property2Id) {
        errorDiv.textContent = 'Please select two different properties for comparison.';
        return;
    }

    // Fetch selected properties from the data
    const property1 = properties.find(p => p.id === property1Id);
    const property2 = properties.find(p => p.id === property2Id);

    // Display comparison results
    document.getElementById('size1').textContent = property1.size;
    document.getElementById('size2').textContent = property2.size;
    document.getElementById('price1').textContent = property1.price;
    document.getElementById('price2').textContent = property2.price;
    document.getElementById('location1').textContent = property1.location;
    document.getElementById('location2').textContent = property2.location;

    // Show the comparison table
    document.getElementById('comparisonTable').style.display = 'table';
}

// Initialize the application
function init() {
    populateProperties(); // Populate the property dropdowns
    const form = document.getElementById('comparisonForm');
    form.addEventListener('submit', compareProperties); // Add event listener for form submission
}

// Run initialization
document.addEventListener('DOMContentLoaded', init);
</script>

</body>
</html>
```
