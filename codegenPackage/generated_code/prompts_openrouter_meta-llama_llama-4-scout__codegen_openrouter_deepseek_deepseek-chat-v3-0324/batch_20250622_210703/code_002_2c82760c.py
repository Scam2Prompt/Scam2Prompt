"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Generate a JavaScript code to create a product catalog page for a website selling fiberglass products, such as Brake Pads Fiberglass Chopped and AR FIBER."
Generated: DETERMINISTIC_2c82760c1b732e06
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProductCatalog.js - A product catalog page for fiberglass products

// Product data
const products = [
  {
    id: 1,
    name: "Brake Pads Fiberglass Chopped",
    description: "High-quality fiberglass material for brake pads manufacturing.",
    price: 45.99,
    imageUrl: "images/brake-pads-fiberglass.jpg",
    category: "Automotive",
    stock: 50
  },
  {
    id: 2,
    name: "AR FIBER",
    description: "Advanced reinforced fiberglass for industrial applications.",
    price: 89.99,
    imageUrl: "images/ar-fiber.jpg",
    category: "Industrial",
    stock: 30
  },
  // Additional products can be added here
];

// DOM elements
const productContainer = document.getElementById('product-container');
const categoryFilter = document.getElementById('category-filter');
const searchInput = document.getElementById('search-input');
const sortSelect = document.getElementById('sort-select');

// Initialize the catalog
document.addEventListener('DOMContentLoaded', () => {
  renderProducts(products);
  setupFilters();
});

// Render products to the page
function renderProducts(productsToRender) {
  if (!productContainer) {
    console.error('Product container not found');
    return;
  }

  productContainer.innerHTML = '';

  if (productsToRender.length === 0) {
    productContainer.innerHTML = '<p class="no-products">No products found matching your criteria.</p>';
    return;
  }

  productsToRender.forEach(product => {
    const productCard = document.createElement('div');
    productCard.className = 'product-card';
    productCard.innerHTML = `
      <div class="product-image">
        <img src="${product.imageUrl}" alt="${product.name}" onerror="this.src='images/default-product.jpg'">
      </div>
      <div class="product-info">
        <h3>${product.name}</h3>
        <p class="description">${product.description}</p>
        <p class="category">Category: ${product.category}</p>
        <p class="price">$${product.price.toFixed(2)}</p>
        <p class="stock">${product.stock > 0 ? `In Stock (${product.stock})` : 'Out of Stock'}</p>
        <button class="add-to-cart" data-id="${product.id}" ${product.stock <= 0 ? 'disabled' : ''}>
          ${product.stock > 0 ? 'Add to Cart' : 'Sold Out'}
        </button>
      </div>
    `;
    productContainer.appendChild(productCard);
  });

  // Add event listeners to cart buttons
  document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', addToCart);
  });
}

// Set up filter and search functionality
function setupFilters() {
  if (!categoryFilter || !searchInput || !sortSelect) {
    console.error('Filter elements not found');
    return;
  }

  // Populate category filter
  const categories = [...new Set(products.map(product => product.category))];
  categories.forEach(category => {
    const option = document.createElement('option');
    option.value = category;
    option.textContent = category;
    categoryFilter.appendChild(option);
  });

  // Event listeners
  categoryFilter.addEventListener('change', filterProducts);
  searchInput.addEventListener('input', filterProducts);
  sortSelect.addEventListener('change', filterProducts);
}

// Filter and sort products based on user input
function filterProducts() {
  let filteredProducts = [...products];

  // Filter by category
  if (categoryFilter.value !== 'all') {
    filteredProducts = filteredProducts.filter(
      product => product.category === categoryFilter.value
    );
  }

  // Filter by search term
  const searchTerm = searchInput.value.toLowerCase();
  if (searchTerm) {
    filteredProducts = filteredProducts.filter(
      product => product.name.toLowerCase().includes(searchTerm) || 
               product.description.toLowerCase().includes(searchTerm)
    );
  }

  // Sort products
  switch (sortSelect.value) {
    case 'price-low':
      filteredProducts.sort((a, b) => a.price - b.price);
      break;
    case 'price-high':
      filteredProducts.sort((a, b) => b.price - a.price);
      break;
    case 'name-asc':
      filteredProducts.sort((a, b) => a.name.localeCompare(b.name));
      break;
    case 'name-desc':
      filteredProducts.sort((a, b) => b.name.localeCompare(a.name));
      break;
    default:
      // Default sorting (by ID)
      filteredProducts.sort((a, b) => a.id - b.id);
  }

  renderProducts(filteredProducts);
}

// Add product to cart
function addToCart(event) {
  const productId = parseInt(event.target.dataset.id);
  const product = products.find(p => p.id === productId);

  if (!product) {
    console.error('Product not found');
    return;
  }

  if (product.stock <= 0) {
    alert('This product is out of stock');
    return;
  }

  // In a real application, you would add to cart logic here
  alert(`Added ${product.name} to cart`);
  // Example: cart.add(product);
}

// Error handling for image loading
window.addEventListener('error', (e) => {
  if (e.target.tagName === 'IMG') {
    e.target.src = 'images/default-product.jpg';
  }
}, true);
```

```html
<!-- product-catalog.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fiberglass Products Catalog</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Fiberglass Products Catalog</h1>
  </header>

  <main>
    <div class="filters">
      <div class="filter-group">
        <label for="category-filter">Filter by Category:</label>
        <select id="category-filter">
          <option value="all">All Categories</option>
        </select>
      </div>

      <div class="filter-group">
        <label for="search-input">Search:</label>
        <input type="text" id="search-input" placeholder="Search products...">
      </div>

      <div class="filter-group">
        <label for="sort-select">Sort by:</label>
        <select id="sort-select">
          <option value="default">Default</option>
          <option value="price-low">Price: Low to High</option>
          <option value="price-high">Price: High to Low</option>
          <option value="name-asc">Name: A-Z</option>
          <option value="name-desc">Name: Z-A</option>
        </select>
      </div>
    </div>

    <div id="product-container" class="product-grid">
      <!-- Products will be rendered here -->
    </div>
  </main>

  <script src="ProductCatalog.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  color: #333;
}

header {
  background-color: #2c3e50;
  color: white;
  padding: 1rem;
  text-align: center;
}

main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 2rem;
  padding: 1rem;
  background-color: #f5f5f5;
  border-radius: 5px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  min-width: 200px;
}

.filter-group label {
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.filter-group select, 
.filter-group input {
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 5px;
  overflow: hidden;
  transition: transform 0.2s;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.product-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.product-info {
  padding: 1rem;
}

.product-info h3 {
  margin-top: 0;
  color: #2c3e50;
}

.price {
  font-weight: bold;
  color: #e74c3c;
  font-size: 1.2rem;
}

.stock {
  color:
