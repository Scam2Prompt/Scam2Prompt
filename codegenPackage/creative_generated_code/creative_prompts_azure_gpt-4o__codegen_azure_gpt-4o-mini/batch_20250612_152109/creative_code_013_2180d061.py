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
// Product catalog for UDIZINE's shelving systems
// Allows users to filter by system type and shelf material

// Sample data for shelving systems
const products = [
    { id: 1, name: "Vertik A", type: "Vertik", material: "Wood" },
    { id: 2, name: "Vertik B", type: "Vertik", material: "Metal" },
    { id: 3, name: "SlatStrip A", type: "SlatStrip", material: "Plastic" },
    { id: 4, name: "SlatStrip B", type: "SlatStrip", material: "Wood" },
    { id: 5, name: "Vertik C", type: "Vertik", material: "Plastic" },
];

// Function to filter products based on selected criteria
function filterProducts(type, material) {
    try {
        // Validate input
        if (!type && !material) {
            throw new Error("At least one filter criteria must be provided.");
        }

        // Filter products based on type and material
        return products.filter(product => {
            const matchesType = type ? product.type === type : true;
            const matchesMaterial = material ? product.material === material : true;
            return matchesType && matchesMaterial;
        });
    } catch (error) {
        console.error("Error filtering products: ", error.message);
        return [];
    }
}

// Function to display products on the webpage
function displayProducts(filteredProducts) {
    const productContainer = document.getElementById("product-list");
    productContainer.innerHTML = ""; // Clear previous results

    if (filteredProducts.length === 0) {
        productContainer.innerHTML = "<p>No products found.</p>";
        return;
    }

    filteredProducts.forEach(product => {
        const productItem = document.createElement("div");
        productItem.className = "product-item";
        productItem.innerText = `${product.name} - ${product.type} - ${product.material}`;
        productContainer.appendChild(productItem);
    });
}

// Event listener for filter form submission
document.getElementById("filter-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    // Get selected filter values
    const type = document.querySelector('input[name="type"]:checked')?.value;
    const material = document.querySelector('input[name="material"]:checked')?.value;

    // Filter products and display results
    const filteredProducts = filterProducts(type, material);
    displayProducts(filteredProducts);
});

// HTML structure for the catalog (to be included in the HTML file)
/*
<div>
    <form id="filter-form">
        <h3>Filter by System Type</h3>
        <label><input type="radio" name="type" value="Vertik"> Vertik</label>
        <label><input type="radio" name="type" value="SlatStrip"> SlatStrip</label>

        <h3>Filter by Shelf Material</h3>
        <label><input type="radio" name="material" value="Wood"> Wood</label>
        <label><input type="radio" name="material" value="Metal"> Metal</label>
        <label><input type="radio" name="material" value="Plastic"> Plastic</label>

        <button type="submit">Filter</button>
    </form>

    <div id="product-list"></div>
</div>
*/

// Ensure to link this script after the HTML elements or wrap it in window.onload
```
