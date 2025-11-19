"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Create a JavaScript function that dynamically displays CreatexPro's product categories, including bags, t-shirts, and unique gifts, based on user selection.
Generated: DETERMINISTIC_2cedc49d0854d238
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically displays CreatexPro's product categories based on user selection.
 * Categories include: Bags, T-Shirts, Unique Gifts.
 */

// Sample data for product categories
const productCategories = {
  bags: ["Backpack", "Tote Bag", "Messenger Bag"],
  tShirts: ["Graphic T-Shirt", "Plain T-Shirt", "Sports T-Shirt"],
  uniqueGifts: ["Custom Mug", "Handmade Notebook", "Personalized Keychain"],
};

/**
 * Displays the selected product category on the webpage.
 * @param {string} category - The category selected by the user (e.g., 'bags', 'tShirts', 'uniqueGifts').
 */
function displayCategory(category) {
  // Validate that the category exists
  if (!productCategories[category]) {
    console.error(`Invalid category: "${category}". Available categories are: Bags, T-Shirts, Unique Gifts.`);
    alert("Invalid category selected! Please choose a valid category.");
    return;
  }

  // Get the container element where products will be displayed
  const container = document.getElementById("product-container");
  if (!container) {
    console.error("Error: 'product-container' element not found in the DOM.");
    return;
  }

  // Clear any previous content in the container
  container.innerHTML = "";

  // Create and append a heading for the selected category
  const heading = document.createElement("h2");
  heading.textContent = `Category: ${capitalizeFirstLetter(category)}`;
  container.appendChild(heading);

  // Create a list of products for the selected category
  const productList = document.createElement("ul");
  productCategories[category].forEach((product) => {
    const listItem = document.createElement("li");
    listItem.textContent = product;
    productList.appendChild(listItem);
  });

  // Append the product list to the container
  container.appendChild(productList);
}

/**
 * Capitalizes the first letter of a given string.
 * @param {string} str - The string to capitalize.
 * @returns {string} - The capitalized string.
 */
function capitalizeFirstLetter(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// Example: Setup event listeners for user selection (assuming you have buttons or dropdowns in your HTML)
document.querySelectorAll(".category-selector").forEach((button) => {
  button.addEventListener("click", (event) => {
    const selectedCategory = event.target.dataset.category; // Assume data-category attribute holds the category name
    displayCategory(selectedCategory);
  });
});

/**
 * Example HTML structure for reference:
 * 
 * <div id="product-container"></div>
 * 
 * <button class="category-selector" data-category="bags">Bags</button>
 * <button class="category-selector" data-category="tShirts">T-Shirts</button>
 * <button class="category-selector" data-category="uniqueGifts">Unique Gifts</button>
 * 
 */
```
