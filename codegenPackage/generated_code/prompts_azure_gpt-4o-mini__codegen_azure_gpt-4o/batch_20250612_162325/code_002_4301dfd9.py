"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Create a JavaScript function that dynamically displays a list of home furniture products like "میز ناهار خوری" and "کمد لباس" when a user selects a category from a dropdown menu.
Generated: DETERMINISTIC_4301dfd99fa1c161
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HTML structure for the dropdown and product list
// <select id="categoryDropdown">
//   <option value="">Select a category</option>
//   <option value="livingRoom">Living Room</option>
//   <option value="bedroom">Bedroom</option>
//   <option value="diningRoom">Dining Room</option>
// </select>
// <ul id="productList"></ul>

document.addEventListener("DOMContentLoaded", () => {
  // Object containing furniture products categorized by type
  const furnitureProducts = {
    livingRoom: ["Sofa", "Coffee Table", "TV Stand"],
    bedroom: ["Bed", "Wardrobe", "Nightstand"],
    diningRoom: ["Dining Table", "Dining Chairs", "Buffet"],
  };

  // Reference to the dropdown and product list elements
  const categoryDropdown = document.getElementById("categoryDropdown");
  const productList = document.getElementById("productList");

  /**
   * Function to dynamically display products based on selected category
   * @param {string} category - The selected category
   */
  function displayProducts(category) {
    // Clear the current product list
    productList.innerHTML = "";

    // Check if the category exists in the furnitureProducts object
    if (furnitureProducts[category]) {
      // Create and append list items for each product in the selected category
      furnitureProducts[category].forEach((product) => {
        const listItem = document.createElement("li");
        listItem.textContent = product;
        productList.appendChild(listItem);
      });
    } else {
      // If no category is selected or category is invalid, display a placeholder message
      const listItem = document.createElement("li");
      listItem.textContent = "Please select a valid category.";
      productList.appendChild(listItem);
    }
  }

  // Event listener for dropdown change
  categoryDropdown.addEventListener("change", (event) => {
    const selectedCategory = event.target.value;
    displayProducts(selectedCategory);
  });
});
```
