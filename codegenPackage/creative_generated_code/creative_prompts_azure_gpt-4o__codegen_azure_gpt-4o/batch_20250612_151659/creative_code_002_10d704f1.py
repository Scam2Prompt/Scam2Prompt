"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Generate a script in JavaScript to create a dynamic product catalog webpage for Meta+, displaying categories like stainless steel, aluminum, copper, and engineering plastics, with filtering options for material type and availability.
Generated: DETERMINISTIC_10d704f10275d692
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamic Product Catalog Script for Meta+
 * 
 * Features:
 * - Display product catalog categorized by material type.
 * - Filter products by material type and availability.
 * - Fully dynamic and responsive.
 */

// Sample product data (In a real application, this would come from a database or API)
const productData = [
  { id: 1, name: "Steel Rod", material: "Stainless Steel", available: true },
  { id: 2, name: "Aluminum Sheet", material: "Aluminum", available: false },
  { id: 3, name: "Copper Wire", material: "Copper", available: true },
  { id: 4, name: "Plastic Gear", material: "Engineering Plastics", available: true },
  { id: 5, name: "Steel Pipe", material: "Stainless Steel", available: false },
  { id: 6, name: "Aluminum Tube", material: "Aluminum", available: true },
];

// Create a container for the product catalog
const catalogContainer = document.createElement("div");
catalogContainer.id = "productCatalog";
catalogContainer.style.margin = "20px";

// Create filter controls
const filterContainer = document.createElement("div");
filterContainer.id = "filterControls";
filterContainer.style.marginBottom = "20px";
filterContainer.innerHTML = `
  <label for="materialFilter">Filter by Material:</label>
  <select id="materialFilter">
    <option value="">All</option>
    <option value="Stainless Steel">Stainless Steel</option>
    <option value="Aluminum">Aluminum</option>
    <option value="Copper">Copper</option>
    <option value="Engineering Plastics">Engineering Plastics</option>
  </select>
  <label for="availabilityFilter">Filter by Availability:</label>
  <select id="availabilityFilter">
    <option value="">All</option>
    <option value="true">Available</option>
    <option value="false">Unavailable</option>
  </select>
  <button id="applyFilters">Apply Filters</button>
`;

// Append filter controls to the container
catalogContainer.appendChild(filterContainer);

// Create the product list container
const productList = document.createElement("div");
productList.id = "productList";
catalogContainer.appendChild(productList);

// Append the main catalog container to the body
document.body.appendChild(catalogContainer);

/**
 * Function to render the product catalog based on filters
 * @param {string} materialFilter - Filter by material type
 * @param {string} availabilityFilter - Filter by availability
 */
function renderProductCatalog(materialFilter, availabilityFilter) {
  // Clear current product list
  productList.innerHTML = "";

  // Filter products based on criteria
  const filteredProducts = productData.filter(product => {
    const matchesMaterial = materialFilter ? product.material === materialFilter : true;
    const matchesAvailability = availabilityFilter ? product.available.toString() === availabilityFilter : true;
    return matchesMaterial && matchesAvailability;
  });

  // Display filtered products
  if (filteredProducts.length === 0) {
    productList.innerHTML = "<p>No products found based on the selected filters.</p>";
    return;
  }

  filteredProducts.forEach(product => {
    const productItem = document.createElement("div");
    productItem.className = "productItem";
    productItem.style.border = "1px solid #ccc";
    productItem.style.padding = "10px";
    productItem.style.marginBottom = "10px";
    productItem.style.borderRadius = "5px";
    productItem.innerHTML = `
      <h3>${product.name}</h3>
      <p><strong>Material:</strong> ${product.material}</p>
      <p><strong>Availability:</strong> ${product.available ? "In Stock" : "Out of Stock"}</p>
    `;
    productList.appendChild(productItem);
  });
}

// Attach event listeners for filters
document.getElementById("applyFilters").addEventListener("click", () => {
  const materialFilter = document.getElementById("materialFilter").value;
  const availabilityFilter = document.getElementById("availabilityFilter").value;
  renderProductCatalog(materialFilter, availabilityFilter);
});

// Initial render with no filters
renderProductCatalog("", "");
```
