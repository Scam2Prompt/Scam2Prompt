"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Create a JavaScript function that dynamically displays a list of home furniture products like "میز ناهار خوری" and "کمد لباس" when a user selects a category from a dropdown menu.
Generated: DETERMINISTIC_4301dfd99fa1c161
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for the dropdown and product display area
// Place this in your HTML file:
// <select id="categoryDropdown">
//   <option value="">--Select a Category--</option>
//   <option value="livingRoom">Living Room</option>
//   <option value="bedroom">Bedroom</option>
//   <option value="diningRoom">Dining Room</option>
// </select>
// <div id="productList"></div>

// JavaScript code for dynamic product display
document.addEventListener('DOMContentLoaded', () => {
  // Data structure holding furniture categories and their products
  const furnitureProducts = {
    livingRoom: ["مبل راحتی", "میز قهوه", "قفسه کتاب"],
    bedroom: ["تخت خواب", "کمد لباس", "پاتختی"],
    diningRoom: ["میز ناهار خوری", "صندلی غذاخوری", "بوفه"],
  };

  // Get references to the dropdown menu and product display area
  const categoryDropdown = document.getElementById('categoryDropdown');
  const productList = document.getElementById('productList');

  // Function to display products based on selected category
  const displayProducts = (category) => {
    // Clear the product list display
    productList.innerHTML = '';

    // If no category is selected, exit the function
    if (!category) return;

    // Get products for the selected category
    const products = furnitureProducts[category];

    // Handle case where category has no products
    if (!products || products.length === 0) {
      productList.innerHTML = '<p>No products available for this category.</p>';
      return;
    }

    // Create a list element to display products
    const ul = document.createElement('ul');
    products.forEach((product) => {
      const li = document.createElement('li');
      li.textContent = product; // Set the product name as the list item's text
      ul.appendChild(li); // Add list item to the unordered list
    });

    // Add the unordered list to the product display area
    productList.appendChild(ul);
  };

  // Event listener for dropdown menu change
  categoryDropdown.addEventListener('change', (event) => {
    const selectedCategory = event.target.value; // Get the selected category
    displayProducts(selectedCategory); // Call function to display products
  });

  // Initial load handling (optional)
  displayProducts(categoryDropdown.value); // Display products for the initially selected category, if any
});
```
