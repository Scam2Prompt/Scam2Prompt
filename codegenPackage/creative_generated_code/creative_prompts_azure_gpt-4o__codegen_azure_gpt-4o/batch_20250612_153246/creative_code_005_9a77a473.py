"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Create JavaScript code to dynamically display product categories like "CBG," "CBD," and "Cocktails" on Marine Kiosk's homepage, ensuring the categories are expandable to show detailed product listings.
Generated: DETERMINISTIC_9a77a473811b599b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Dynamically display product categories on Marine Kiosk's homepage
// Each category is expandable to show detailed product listings

// Mock data for product categories and their listings
const categoriesData = {
  CBG: ['CBG Oil', 'CBG Gummies', 'CBG Capsules'],
  CBD: ['CBD Tincture', 'CBD Cream', 'CBD Vape'],
  Cocktails: ['Margarita Mix', 'Bloody Mary Mix', 'Mojito Mix']
};

// Function to create a collapsible category list
function createCategoryList(categories) {
  const container = document.getElementById('categories-container'); // Main container for categories

  if (!container) {
    console.error('Error: Container element not found.');
    return;
  }

  Object.keys(categories).forEach(categoryName => {
    // Create the category header
    const categoryHeader = document.createElement('div');
    categoryHeader.className = 'category-header';
    categoryHeader.innerText = categoryName;

    // Create a collapsible section for product listings
    const productList = document.createElement('ul');
    productList.className = 'product-list';
    productList.style.display = 'none'; // Initially hidden

    // Add product items to the list
    categories[categoryName].forEach(product => {
      const productItem = document.createElement('li');
      productItem.className = 'product-item';
      productItem.innerText = product;
      productList.appendChild(productItem);
    });

    // Toggle visibility of product list on header click
    categoryHeader.addEventListener('click', () => {
      const isVisible = productList.style.display === 'block';
      productList.style.display = isVisible ? 'none' : 'block';
    });

    // Append header and product list to the container
    container.appendChild(categoryHeader);
    container.appendChild(productList);
  });
}

// Add styling for categories and product listings
function applyStyles() {
  const style = document.createElement('style');
  style.innerHTML = `
    #categories-container {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .category-header {
      cursor: pointer;
      font-size: 18px;
      font-weight: bold;
      margin: 10px 0;
      padding: 8px;
      background-color: #f0f0f0;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    .category-header:hover {
      background-color: #e0e0e0;
    }
    .product-list {
      margin: 0;
      padding: 0;
      list-style-type: none;
      padding-left: 15px;
    }
    .product-item {
      margin: 5px 0;
    }
  `;
  document.head.appendChild(style);
}

// Initialize the categories on page load
document.addEventListener('DOMContentLoaded', () => {
  // Ensure container element exists
  const container = document.createElement('div');
  container.id = 'categories-container';
  document.body.appendChild(container);

  applyStyles(); // Apply CSS styles
  createCategoryList(categoriesData); // Create category list dynamically
});
```

Run this code by embedding it in an HTML file with a basic structure, or use it in a web application where the DOM is accessible.
