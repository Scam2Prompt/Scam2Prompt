"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Generate a JavaScript code snippet to create a product catalog page for a website selling iron and steel products, including filtering options for products like corte e dobra services."
Generated: DETERMINISTIC_954e2cebcb3a9c95
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Catalog Page for Iron and Steel Products

// Product data
const products = [
  {
    id: 1,
    name: 'Steel Beams',
    category: 'structural',
    price: 120.50,
    description: 'High-quality structural steel beams for construction',
    hasCorteEDobra: false
  },
  {
    id: 2,
    name: 'Iron Sheets',
    category: 'sheet',
    price: 45.75,
    description: 'Durable iron sheets for roofing and cladding',
    hasCorteEDobra: true
  },
  {
    id: 3,
    name: 'Steel Rods',
    category: 'structural',
    price: 30.20,
    description: 'Reinforcement steel rods for concrete structures',
    hasCorteEDobra: false
  },
  {
    id: 4,
    name: 'Decorative Iron Gates',
    category: 'decorative',
    price: 250.00,
    description: 'Custom decorative iron gates with corte e dobra services',
    hasCorteEDobra: true
  }
];

// DOM elements
const productContainer = document.getElementById('product-container');
const categoryFilter = document.getElementById('category-filter');
const priceFilter = document.getElementById('price-filter');
const corteEDobraFilter = document.getElementById('corte-edobra-filter');
const searchInput = document.getElementById('search-input');

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
  renderProducts(products);
  setupEventListeners();
});

// Render products based on filters
function renderProducts(productsToRender) {
  productContainer.innerHTML = '';
  
  if (productsToRender.length === 0) {
    productContainer.innerHTML = '<p class="no-products">No products match your criteria.</p>';
    return;
  }

  productsToRender.forEach(product => {
    const productCard = document.createElement('div');
    productCard.className = 'product-card';
    
    productCard.innerHTML = `
      <h3>${product.name}</h3>
      <p class="category">${product.category}</p>
      <p class="price">$${product.price.toFixed(2)}</p>
      <p class="description">${product.description}</p>
      ${product.hasCorteEDobra ? '<span class="corte-edobra-badge">Corte e Dobra Available</span>' : ''}
      <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
    `;
    
    productContainer.appendChild(productCard);
  });
}

// Setup event listeners for filters
function setupEventListeners() {
  categoryFilter.addEventListener('change', applyFilters);
  priceFilter.addEventListener('change', applyFilters);
  corteEDobraFilter.addEventListener('change', applyFilters);
  searchInput.addEventListener('input', applyFilters);
  
  // Add to cart functionality
  productContainer.addEventListener('click', (e) => {
    if (e.target.classList.contains('add-to-cart')) {
      const productId = parseInt(e.target.getAttribute('data-id'));
      addToCart(productId);
    }
  });
}

// Apply all active filters
function applyFilters() {
  const selectedCategory = categoryFilter.value;
  const selectedPrice = priceFilter.value;
  const onlyCorteEDobra = corteEDobraFilter.checked;
  const searchTerm = searchInput.value.toLowerCase();
  
  let filteredProducts = [...products];
  
  // Category filter
  if (selectedCategory !== 'all') {
    filteredProducts = filteredProducts.filter(
      product => product.category === selectedCategory
    );
  }
  
  // Price filter
  if (selectedPrice === 'low') {
    filteredProducts = filteredProducts.filter(
      product => product.price < 50
    );
  } else if (selectedPrice === 'medium') {
    filteredProducts = filteredProducts.filter(
      product => product.price >= 50 && product.price < 100
    );
  } else if (selectedPrice === 'high') {
    filteredProducts = filteredProducts.filter(
      product => product.price >= 100
    );
  }
  
  // Corte e Dobra filter
  if (onlyCorteEDobra) {
    filteredProducts = filteredProducts.filter(
      product => product.hasCorteEDobra
    );
  }
  
  // Search filter
  if (searchTerm) {
    filteredProducts = filteredProducts.filter(
      product => product.name.toLowerCase().includes(searchTerm) || 
               product.description.toLowerCase().includes(searchTerm)
    );
  }
  
  renderProducts(filteredProducts);
}

// Add product to cart (mock implementation)
function addToCart(productId) {
  const product = products.find(p => p.id === productId);
  if (product) {
    console.log(`Added ${product.name} to cart`);
    // In a real implementation, you would update the cart state here
    alert(`Added ${product.name} to cart`);
  } else {
    console.error('Product not found');
  }
}

// Error handling for missing DOM elements
try {
  if (!productContainer || !categoryFilter || !priceFilter || !corteEDobraFilter || !searchInput) {
    throw new Error('Required DOM elements not found');
  }
} catch (error) {
  console.error('Initialization error:', error.message);
  alert('An error occurred while loading the product catalog. Please refresh the page.');
}
```
