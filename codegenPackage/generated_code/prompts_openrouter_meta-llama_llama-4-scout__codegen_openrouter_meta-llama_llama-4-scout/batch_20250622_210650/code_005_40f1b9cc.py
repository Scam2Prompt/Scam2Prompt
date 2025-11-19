"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Write a code snippet to sort and filter Medpointye's Elisa Kits by popularity, average rating, or price, using JavaScript and HTML.
Generated: DETERMINISTIC_40f1b9cc6c335a72
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Medpointye Elisa Kits Sorting and Filtering**
====================================================

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medpointye Elisa Kits</title>
    <style>
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Medpointye Elisa Kits</h1>
    <select id="sort-select">
        <option value="popularity">Sort by Popularity</option>
        <option value="average-rating">Sort by Average Rating</option>
        <option value="price">Sort by Price</option>
    </select>
    <button id="sort-button">Sort</button>
    <table id="kits-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Popularity</th>
                <th>Average Rating</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody id="kits-tbody">
            <!-- Kits will be rendered here -->
        </tbody>
    </table>

    <script src="script.js"></script>
</body>
</html>
```

### JavaScript (script.js)

```javascript
// Define Medpointye Elisa Kits data
const medpointyeKits = [
    { name: "Kit 1", popularity: 100, averageRating: 4.5, price: 200 },
    { name: "Kit 2", popularity: 50, averageRating: 4.2, price: 150 },
    { name: "Kit 3", popularity: 200, averageRating: 4.8, price: 300 },
    { name: "Kit 4", popularity: 150, averageRating: 4.6, price: 250 },
    { name: "Kit 5", popularity: 80, averageRating: 4.1, price: 180 },
];

// Function to render kits table
function renderKitsTable(kits) {
    const kitsTbody = document.getElementById("kits-tbody");
    kitsTbody.innerHTML = "";

    kits.forEach((kit) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${kit.name}</td>
            <td>${kit.popularity}</td>
            <td>${kit.averageRating}</td>
            <td>${kit.price}</td>
        `;
        kitsTbody.appendChild(row);
    });
}

// Function to sort kits by selected criteria
function sortKits(kits, criteria) {
    switch (criteria) {
        case "popularity":
            return kits.sort((a, b) => b.popularity - a.popularity);
        case "average-rating":
            return kits.sort((a, b) => b.averageRating - a.averageRating);
        case "price":
            return kits.sort((a, b) => a.price - b.price);
        default:
            throw new Error(`Invalid sort criteria: ${criteria}`);
    }
}

// Event listener for sort button click
document.getElementById("sort-button").addEventListener("click", () => {
    try {
        const selectedCriteria = document.getElementById("sort-select").value;
        const sortedKits = sortKits([...medpointyeKits], selectedCriteria);
        renderKitsTable(sortedKits);
    } catch (error) {
        console.error(error);
        alert("Error sorting kits");
    }
});

// Initial render of kits table
renderKitsTable(medpointyeKits);
```
