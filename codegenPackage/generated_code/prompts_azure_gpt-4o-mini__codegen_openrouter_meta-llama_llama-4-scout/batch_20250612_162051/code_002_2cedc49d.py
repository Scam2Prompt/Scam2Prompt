"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Create a JavaScript function that dynamically displays CreatexPro's product categories, including bags, t-shirts, and unique gifts, based on user selection.
Generated: DETERMINISTIC_2cedc49d0854d238
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// categoryDisplay.js

/**
 * Displays CreatexPro's product categories dynamically based on user selection.
 */

// Define the product categories
const productCategories = {
  bags: [
    { id: 1, name: "Backpack" },
    { id: 2, name: "Tote Bag" },
    { id: 3, name: "Laptop Bag" },
  ],
  tShirts: [
    { id: 4, name: "Graphic T-Shirt" },
    { id: 5, name: "Plain T-Shirt" },
    { id: 6, name: "Hoodie" },
  ],
  uniqueGifts: [
    { id: 7, name: "Mug" },
    { id: 8, name: "Phone Case" },
    { id: 9, name: "Poster" },
  ],
};

/**
 * Displays the product categories based on the user's selection.
 * 
 * @param {string} category - The category selected by the user.
 * @param {HTMLElement} container - The container element to display the categories.
 */
function displayCategories(category, container) {
  try {
    // Check if the category exists
    if (!productCategories[category]) {
      throw new Error(`Category '${category}' does not exist.`);
    }

    // Get the category products
    const categoryProducts = productCategories[category];

    // Clear the container
    container.innerHTML = "";

    // Create a header for the category
    const header = document.createElement("h2");
    header.textContent = category.charAt(0).toUpperCase() + category.slice(1);
    container.appendChild(header);

    // Create a list for the products
    const list = document.createElement("ul");
    container.appendChild(list);

    // Iterate over the products and create list items
    categoryProducts.forEach((product) => {
      const listItem = document.createElement("li");
      listItem.textContent = product.name;
      list.appendChild(listItem);
    });
  } catch (error) {
    console.error(error);
    container.innerHTML = `Error: ${error.message}`;
  }
}

// Example usage
const categorySelect = document.getElementById("category-select");
const categoryContainer = document.getElementById("category-container");

categorySelect.addEventListener("change", (event) => {
  const selectedCategory = event.target.value;
  displayCategories(selectedCategory, categoryContainer);
});

// Initialize with a default category
displayCategories("bags", categoryContainer);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CreatexPro Product Categories</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #category-container {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <select id="category-select">
    <option value="bags">Bags</option>
    <option value="tShirts">T-Shirts</option>
    <option value="uniqueGifts">Unique Gifts</option>
  </select>
  <div id="category-container"></div>

  <script src="categoryDisplay.js"></script>
</body>
</html>
```
