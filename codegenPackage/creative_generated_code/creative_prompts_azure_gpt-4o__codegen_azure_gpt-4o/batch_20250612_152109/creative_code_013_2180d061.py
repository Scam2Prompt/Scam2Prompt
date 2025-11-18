"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Write JavaScript code to create an interactive product catalog for UDIZINE's shelving systems, allowing users to filter by system type (e.g., Vertik, SlatStrip) and shelf material.
Generated: DETERMINISTIC_2180d061e0db6c3d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define the product catalog functionality in JavaScript

// Sample data for the shelving systems
const productCatalog = [
    { id: 1, name: "Vertik System A", type: "Vertik", material: "Wood", price: 150 },
    { id: 2, name: "Vertik System B", type: "Vertik", material: "Metal", price: 200 },
    { id: 3, name: "SlatStrip System A", type: "SlatStrip", material: "Glass", price: 250 },
    { id: 4, name: "SlatStrip System B", type: "SlatStrip", material: "Wood", price: 180 },
    { id: 5, name: "SlatStrip System C", type: "SlatStrip", material: "Metal", price: 210 },
];

// Initialize the DOM elements
document.addEventListener("DOMContentLoaded", () => {
    const catalogContainer = document.getElementById("catalog-container");
    const filterTypeSelect = document.getElementById("filter-type");
    const filterMaterialSelect = document.getElementById("filter-material");
    const filterButton = document.getElementById("filter-button");

    // Render the product catalog
    const renderCatalog = (catalog) => {
        catalogContainer.innerHTML = ""; // Clear previous content

        if (catalog.length === 0) {
            catalogContainer.innerHTML = "<p>No products match your criteria.</p>";
            return;
        }

        catalog.forEach((product) => {
            const productDiv = document.createElement("div");
            productDiv.className = "product-item";
            productDiv.innerHTML = `
                <h3>${product.name}</h3>
                <p>Type: ${product.type}</p>
                <p>Material: ${product.material}</p>
                <p>Price: $${product.price}</p>
            `;
            catalogContainer.appendChild(productDiv);
        });
    };

    // Filter the catalog based on user input
    const filterCatalog = () => {
        const selectedType = filterTypeSelect.value;
        const selectedMaterial = filterMaterialSelect.value;

        const filteredCatalog = productCatalog.filter((product) => {
            return (
                (selectedType === "All" || product.type === selectedType) &&
                (selectedMaterial === "All" || product.material === selectedMaterial)
            );
        });

        renderCatalog(filteredCatalog);
    };

    // Attach event listeners
    filterButton.addEventListener("click", filterCatalog);

    // Initial render of the full catalog
    renderCatalog(productCatalog);
});

// Sample HTML structure for the catalog page
// <div id="filter-section">
//     <label for="filter-type">Filter by Type:</label>
//     <select id="filter-type">
//         <option value="All">All</option>
//         <option value="Vertik">Vertik</option>
//         <option value="SlatStrip">SlatStrip</option>
//     </select>
//     <label for="filter-material">Filter by Material:</label>
//     <select id="filter-material">
//         <option value="All">All</option>
//         <option value="Wood">Wood</option>
//         <option value="Metal">Metal</option>
//         <option value="Glass">Glass</option>
//     </select>
//     <button id="filter-button">Filter</button>
// </div>
// <div id="catalog-container"></div>

// CSS styles for better presentation (optional)
// .product-item {
//     border: 1px solid #ccc;
//     padding: 10px;
//     margin: 10px;
//     border-radius: 5px;
// }
```
