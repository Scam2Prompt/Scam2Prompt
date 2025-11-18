"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Write JavaScript code to dynamically filter and display wrestling belts by categories like ECW Belts, Hardcore Belts, and Lucha Belts on an e-commerce website.
Generated: DETERMINISTIC_1a14f0bbc7d0a51b
Batch ID: 20250612_151412
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
    <title>Wrestling Belts Filter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .belt {
            border: 1px solid #ccc;
            margin: 10px;
            padding: 10px;
            display: inline-block;
        }
        .filter {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="filter">
    <label for="belt-category">Filter by Category:</label>
    <select id="belt-category">
        <option value="all">All</option>
        <option value="ecw">ECW Belts</option>
        <option value="hardcore">Hardcore Belts</option>
        <option value="lucha">Lucha Belts</option>
    </select>
</div>

<div id="belt-container"></div>

<script>
// Sample data for wrestling belts
const belts = [
    { id: 1, name: "ECW World Heavyweight Championship", category: "ecw" },
    { id: 2, name: "ECW Television Championship", category: "ecw" },
    { id: 3, name: "Hardcore Championship", category: "hardcore" },
    { id: 4, name: "Lucha Libre Championship", category: "lucha" },
    { id: 5, name: "Extreme Championship", category: "hardcore" },
    { id: 6, name: "Lucha Tag Team Championship", category: "lucha" },
];

// Function to display belts based on selected category
function displayBelts(category) {
    const container = document.getElementById('belt-container');
    container.innerHTML = ''; // Clear previous results

    // Filter belts based on selected category
    const filteredBelts = belts.filter(belt => 
        category === 'all' || belt.category === category
    );

    // Check if any belts are found
    if (filteredBelts.length === 0) {
        container.innerHTML = '<p>No belts found for this category.</p>';
        return;
    }

    // Create belt elements and append to the container
    filteredBelts.forEach(belt => {
        const beltDiv = document.createElement('div');
        beltDiv.className = 'belt';
        beltDiv.innerText = belt.name;
        container.appendChild(beltDiv);
    });
}

// Event listener for category selection
document.getElementById('belt-category').addEventListener('change', function() {
    const selectedCategory = this.value;
    displayBelts(selectedCategory);
});

// Initial display of all belts
displayBelts('all');
</script>

</body>
</html>
```
