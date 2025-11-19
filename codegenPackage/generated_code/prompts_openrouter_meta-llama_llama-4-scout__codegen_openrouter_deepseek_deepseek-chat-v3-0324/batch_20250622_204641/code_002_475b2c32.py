"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Generate a JavaScript code to create a product catalog page for an e-commerce website featuring products like projectors, headsets, and keyboards.
Generated: DETERMINISTIC_475b2c3283818e6f
Batch ID: 20250622_204641
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Catalog Page for E-Commerce Website

// Product data
const products = [
  {
    id: 1,
    name: "HD Projector Pro",
    category: "projectors",
    price: 499.99,
    description: "Full HD 1080p projector with 3000 lumens brightness",
    image: "projector.jpg",
    stock: 15,
    rating: 4.5
  },
  {
    id: 2,
    name: "Wireless Noise-Canceling Headset",
    category: "headsets",
    price: 199.99,
    description: "Premium wireless headset with active noise cancellation",
    image: "headset.jpg",
    stock: 25,
    rating: 4.8
  },
  {
    id: 3,
    name: "Mechanical Gaming Keyboard",
    category: "keyboards",
    price: 129.99,
    description: "RGB mechanical keyboard with customizable switches",
    image: "keyboard.jpg",
    stock: 30,
    rating: 4.7
  },
  {
    id: 4,
    name: "4K Ultra Short Throw Projector",
    category: "projectors",
    price: 1299.99,
    description: "Cinema-quality 4K projector with ultra short throw technology",
    image: "projector2.jpg",
    stock: 8,
    rating: 4.9
  },
  {
    id: 5,
    name: "Studio Monitor Headphones",
    category: "headsets",
    price: 149.99,
    description: "Professional studio headphones with flat frequency response",
    image: "headset2.jpg",
    stock: 20,
    rating: 4.6
  },
  {
    id: 6,
    name: "Ergonomic Wireless Keyboard",
    category: "keyboards",
    price: 89.99,
    description: "Split-design wireless keyboard for comfortable typing",
    image: "keyboard2.jpg",
    stock: 18,
    rating: 4.4
  }
];

// DOM elements
const productContainer = document.getElementById('product-container');
const categoryFilter = document.getElementById('category-filter');
const searchInput = document.getElementById('search-input');
const sortSelect = document.getElementById('sort-select');

// Initialize the page
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
        <img src="images/${product.image}" alt="${product.name}" onerror="this.src='images/placeholder.jpg'">
        ${product.stock < 5 ? '<span class="low-stock">Low Stock</span>' : ''}
      </div>
      <div class="product-info">
        <h3>${product.name}</h3>
        <div class="product-rating">
          ${renderRatingStars(product.rating)}
          <span>(${product.rating})</span>
        </div>
        <p class="product-description">${product.description}</p>
        <p class="product-price">$${product.price.toFixed(2)}</p>
        <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
      </div>
    `;
    productContainer.appendChild(productCard);
  });
}

// Render rating stars
function renderRatingStars(rating) {
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 >= 0.5;
  let stars = '';

  for (let i = 1; i <= 5; i++) {
    if (i <= fullStars) {
      stars += '<i class="fas fa-star"></i>';
    } else if (i === fullStars + 1 && hasHalfStar) {
      stars += '<i class="fas fa-star-half-alt"></i>';
    } else {
      stars += '<i class="far fa-star"></i>';
    }
  }

  return stars;
}

// Filter products based on search and category
function filterProducts() {
  const searchTerm = searchInput.value.toLowerCase();
  const selectedCategory = categoryFilter.value;

  let filteredProducts = products.filter(product => {
    const matchesSearch = product.name.toLowerCase().includes(searchTerm) || 
                         product.description.toLowerCase().includes(searchTerm);
    const matchesCategory = selectedCategory === 'all' || product.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  sortProducts(filteredProducts);
}

// Sort products based on selected option
function sortProducts(productsToSort) {
  const sortOption = sortSelect.value;

  switch (sortOption) {
    case 'price-low':
      productsToSort.sort((a, b) => a.price - b.price);
      break;
    case 'price-high':
      productsToSort.sort((a, b) => b.price - a.price);
      break;
    case 'rating':
      productsToSort.sort((a, b) => b.rating - a.rating);
      break;
    case 'name':
      productsToSort.sort((a, b) => a.name.localeCompare(b.name));
      break;
    default:
      // Default is newest first (by ID)
      productsToSort.sort((a, b) => b.id - a.id);
  }

  renderProducts(productsToSort);
}

// Set up event listeners
function setupEventListeners() {
  categoryFilter.addEventListener('change', filterProducts);
  searchInput.addEventListener('input', filterProducts);
  sortSelect.addEventListener('change', () => filterProducts());
  
  // Delegated event listener for add to cart buttons
  productContainer.addEventListener('click', (e) => {
    if (e.target.classList.contains('add-to-cart')) {
      const productId = parseInt(e.target.getAttribute('data-id'));
      addToCart(productId);
    }
  });
}

// Add product to cart
function addToCart(productId) {
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
  console.log(`Added product ${productId} to cart`);
}

// Error handling for image loading
window.addEventListener('error', (e) => {
  if (e.target.tagName === 'IMG') {
    e.target.src = 'images/placeholder.jpg';
  }
}, true);
```
