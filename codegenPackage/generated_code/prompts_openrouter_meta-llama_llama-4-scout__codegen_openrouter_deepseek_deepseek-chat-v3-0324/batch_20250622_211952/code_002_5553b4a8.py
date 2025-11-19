"""
Generated Code Metadata:
========================
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Generate a JavaScript code to create a product catalog page for a sports supplement website, featuring products like Creatine Hardcore and Nutri Whey Protein.
Generated: DETERMINISTIC_5553b4a807a3dc6b
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Catalog for Sports Supplements Website

// Product data
const products = [
  {
    id: 1,
    name: "Creatine Hardcore",
    description: "Premium creatine monohydrate for enhanced strength and performance",
    price: 29.99,
    image: "creatine-hardcore.jpg",
    category: "performance",
    rating: 4.8,
    stock: 50
  },
  {
    id: 2,
    name: "Nutri Whey Protein",
    description: "High-quality whey protein isolate for muscle recovery and growth",
    price: 39.99,
    image: "nutri-whey-protein.jpg",
    category: "protein",
    rating: 4.9,
    stock: 30
  },
  {
    id: 3,
    name: "Pre-Workout Extreme",
    description: "Powerful pre-workout formula for maximum energy and focus",
    price: 34.99,
    image: "pre-workout-extreme.jpg",
    category: "performance",
    rating: 4.7,
    stock: 25
  },
  {
    id: 4,
    name: "BCAA Pro",
    description: "Essential branched-chain amino acids for muscle recovery",
    price: 24.99,
    image: "bcaa-pro.jpg",
    category: "recovery",
    rating: 4.6,
    stock: 40
  }
];

// DOM elements
const productContainer = document.getElementById('product-container');
const categoryFilter = document.getElementById('category-filter');
const searchInput = document.getElementById('search-input');
const sortSelect = document.getElementById('sort-select');

// Initialize the catalog
document.addEventListener('DOMContentLoaded', () => {
  renderProducts(products);
  setupEventListeners();
});

// Render products to the page
function renderProducts(productsToRender) {
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
        <img src="images/${product.image}" alt="${product.name}">
        ${product.stock < 10 ? '<span class="low-stock">Low Stock</span>' : ''}
      </div>
      <div class="product-info">
        <h3>${product.name}</h3>
        <p class="description">${product.description}</p>
        <div class="rating">${renderStars(product.rating)}</div>
        <div class="price">$${product.price.toFixed(2)}</div>
        <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
      </div>
    `;
    productContainer.appendChild(productCard);
  });
}

// Render star rating
function renderStars(rating) {
  const fullStars = Math.floor(rating);
  const halfStar = rating % 1 >= 0.5;
  let stars = '';
  
  for (let i = 0; i < fullStars; i++) {
    stars += '<i class="fas fa-star"></i>';
  }
  
  if (halfStar) {
    stars += '<i class="fas fa-star-half-alt"></i>';
  }
  
  for (let i = 0; i < 5 - Math.ceil(rating); i++) {
    stars += '<i class="far fa-star"></i>';
  }
  
  return stars;
}

// Filter products by category
function filterByCategory() {
  const selectedCategory = categoryFilter.value;
  let filteredProducts = products;
  
  if (selectedCategory !== 'all') {
    filteredProducts = products.filter(product => product.category === selectedCategory);
  }
  
  return filteredProducts;
}

// Search products by name or description
function searchProducts() {
  const searchTerm = searchInput.value.toLowerCase();
  return products.filter(product => 
    product.name.toLowerCase().includes(searchTerm) || 
    product.description.toLowerCase().includes(searchTerm)
  );
}

// Sort products
function sortProducts(productsToSort) {
  const sortOption = sortSelect.value;
  
  switch (sortOption) {
    case 'price-low':
      return [...productsToSort].sort((a, b) => a.price - b.price);
    case 'price-high':
      return [...productsToSort].sort((a, b) => b.price - a.price);
    case 'rating':
      return [...productsToSort].sort((a, b) => b.rating - a.rating);
    case 'name':
      return [...productsToSort].sort((a, b) => a.name.localeCompare(b.name));
    default:
      return productsToSort;
  }
}

// Update displayed products based on filters
function updateDisplayedProducts() {
  try {
    let filteredProducts = filterByCategory();
    filteredProducts = searchProducts(filteredProducts);
    filteredProducts = sortProducts(filteredProducts);
    renderProducts(filteredProducts);
  } catch (error) {
    console.error('Error updating products:', error);
    productContainer.innerHTML = '<p class="error">An error occurred while loading products. Please try again later.</p>';
  }
}

// Setup event listeners
function setupEventListeners() {
  categoryFilter.addEventListener('change', updateDisplayedProducts);
  searchInput.addEventListener('input', updateDisplayedProducts);
  sortSelect.addEventListener('change', updateDisplayedProducts);
  
  // Add to cart functionality
  document.addEventListener('click', (e) => {
    if (e.target.classList.contains('add-to-cart')) {
      const productId = parseInt(e.target.getAttribute('data-id'));
      addToCart(productId);
    }
  });
}

// Add product to cart
function addToCart(productId) {
  try {
    const product = products.find(p => p.id === productId);
    if (!product) throw new Error('Product not found');
    
    if (product.stock <= 0) {
      alert('This product is out of stock!');
      return;
    }
    
    // In a real app, you would add to cart storage/API
    alert(`Added ${product.name} to cart!`);
    
    // Update stock (in a real app, this would be handled by backend)
    product.stock--;
    updateDisplayedProducts();
  } catch (error) {
    console.error('Error adding to cart:', error);
    alert('Could not add product to cart. Please try again.');
  }
}

// Initialize category filter options
function initCategoryFilter() {
  const categories = ['all', ...new Set(products.map(product => product.category))];
  
  categories.forEach(category => {
    const option = document.createElement('option');
    option.value = category;
    option.textContent = category.charAt(0).toUpperCase() + category.slice(1);
    categoryFilter.appendChild(option);
  });
}

// Initialize sort options
function initSortOptions() {
  const sortOptions = [
    { value: 'default', text: 'Default' },
    { value: 'price-low', text: 'Price: Low to High' },
    { value: 'price-high', text: 'Price: High to Low' },
    { value: 'rating', text: 'Highest Rating' },
    { value: 'name', text: 'Name: A-Z' }
  ];
  
  sortOptions.forEach(option => {
    const element = document.createElement('option');
    element.value = option.value;
    element.textContent = option.text;
    sortSelect.appendChild(element);
  });
}

// Initialize filters and sort options
initCategoryFilter();
initSortOptions();
```
