"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Write JavaScript code to implement a "Recently Viewed" section for an e-commerce website, dynamically updating based on user activity, as seen on Multan Designs.
Generated: DETERMINISTIC_02d8bfe281a9ac04
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Recently Viewed section implementation for an e-commerce site

// A maximum number of items to store in the Recently Viewed section
const MAX_RECENTLY_VIEWED_ITEMS = 10;

// Retrieve the recently viewed items from localStorage
function getRecentlyViewedItems() {
  try {
    const items = JSON.parse(localStorage.getItem('recentlyViewed')) || [];
    return Array.isArray(items) ? items : [];
  } catch (error) {
    console.error('Error retrieving recently viewed items from localStorage:', error);
    return [];
  }
}

// Save the recently viewed items to localStorage
function saveRecentlyViewedItems(items) {
  try {
    localStorage.setItem('recentlyViewed', JSON.stringify(items));
  } catch (error) {
    console.error('Error saving recently viewed items to localStorage:', error);
  }
}

// Add a product to the Recently Viewed section
function addRecentlyViewedItem(product) {
  try {
    if (!product || !product.id || !product.name || !product.imageUrl || !product.url) {
      console.error('Invalid product object provided:', product);
      return;
    }

    let recentlyViewed = getRecentlyViewedItems();

    // Check if the product already exists in the list
    recentlyViewed = recentlyViewed.filter((item) => item.id !== product.id);

    // Add the product to the beginning of the list
    recentlyViewed.unshift(product);

    // Limit the array to the maximum number of items
    if (recentlyViewed.length > MAX_RECENTLY_VIEWED_ITEMS) {
      recentlyViewed = recentlyViewed.slice(0, MAX_RECENTLY_VIEWED_ITEMS);
    }

    saveRecentlyViewedItems(recentlyViewed);

    // Dynamically update the UI
    renderRecentlyViewedSection();
  } catch (error) {
    console.error('Error adding recently viewed item:', error);
  }
}

// Render the Recently Viewed section in the UI
function renderRecentlyViewedSection() {
  const recentlyViewedContainer = document.getElementById('recently-viewed');
  if (!recentlyViewedContainer) {
    console.error('Recently Viewed container not found in the DOM.');
    return;
  }

  recentlyViewedContainer.innerHTML = ''; // Clear the container
  const recentlyViewed = getRecentlyViewedItems();

  if (recentlyViewed.length === 0) {
    recentlyViewedContainer.innerHTML = '<p>No items viewed recently.</p>';
    return;
  }

  recentlyViewed.forEach((item) => {
    const productElement = document.createElement('div');
    productElement.classList.add('recently-viewed-item');
    productElement.innerHTML = `
      <a href="${item.url}">
        <img src="${item.imageUrl}" alt="${item.name}" />
        <p>${item.name}</p>
      </a>
    `;
    recentlyViewedContainer.appendChild(productElement);
  });
}

// Event listener for product views (simulated example)
function handleProductView(product) {
  // Simulating a product view
  addRecentlyViewedItem(product);
}

// Example initialization
document.addEventListener('DOMContentLoaded', () => {
  renderRecentlyViewedSection();

  // Simulated product view event (replace with actual logic in production)
  document.querySelectorAll('.product').forEach((productElement) => {
    productElement.addEventListener('click', () => {
      const product = {
        id: productElement.dataset.id,
        name: productElement.dataset.name,
        imageUrl: productElement.dataset.imageUrl,
        url: productElement.dataset.url,
      };
      handleProductView(product);
    });
  });
});
```

**HTML Example:**  
```html
<div id="recently-viewed" class="recently-viewed-section"></div>
<div class="product" data-id="1" data-name="Product A" data-imageUrl="imageA.jpg" data-url="/product-a">Product A</div>
<div class="product" data-id="2" data-name="Product B" data-imageUrl="imageB.jpg" data-url="/product-b">Product B</div>
```

**Notes:** Make sure to style the `recently-viewed-section` and `recently-viewed-item` classes appropriately in your CSS for proper display.
