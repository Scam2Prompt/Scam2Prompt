"""
Generated Code Metadata:
========================
Original URL: https://bismillahgems.com
Prompt: Write a JavaScript code to create a responsive product grid, similar to the one on Bismillah Gems, to display a collection of gemstones with their images, names, and prices.
Generated: DETERMINISTIC_3bc6e8a6a8e34f8d
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Grid Component
class ProductGrid {
  constructor(containerId, products) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container with ID ${containerId} not found`);
    }
    this.products = products || [];
    this.init();
  }

  init() {
    this.render();
    this.setupEventListeners();
  }

  render() {
    if (!this.products.length) {
      this.container.innerHTML = '<p class="no-products">No products available</p>';
      return;
    }

    const grid = document.createElement('div');
    grid.className = 'product-grid';

    this.products.forEach(product => {
      const productCard = this.createProductCard(product);
      grid.appendChild(productCard);
    });

    this.container.innerHTML = '';
    this.container.appendChild(grid);
  }

  createProductCard(product) {
    if (!product || !product.id || !product.name || !product.price) {
      console.error('Invalid product data', product);
      return document.createElement('div');
    }

    const card = document.createElement('div');
    card.className = 'product-card';
    card.dataset.id = product.id;

    const image = document.createElement('img');
    image.className = 'product-image';
    image.src = product.image || 'placeholder.jpg';
    image.alt = product.name;
    image.loading = 'lazy';

    const name = document.createElement('h3');
    name.className = 'product-name';
    name.textContent = product.name;

    const price = document.createElement('p');
    price.className = 'product-price';
    price.textContent = `$${product.price.toFixed(2)}`;

    card.appendChild(image);
    card.appendChild(name);
    card.appendChild(price);

    return card;
  }

  setupEventListeners() {
    this.container.addEventListener('click', (e) => {
      const card = e.target.closest('.product-card');
      if (card) {
        const productId = card.dataset.id;
        this.handleProductClick(productId);
      }
    });
  }

  handleProductClick(productId) {
    const product = this.products.find(p => p.id === productId);
    if (product) {
      console.log('Product clicked:', product);
      // Custom event for product selection
      const event = new CustomEvent('productSelected', { detail: product });
      document.dispatchEvent(event);
    }
  }

  updateProducts(newProducts) {
    if (!Array.isArray(newProducts)) {
      console.error('Invalid products data');
      return;
    }
    this.products = newProducts;
    this.render();
  }
}

// CSS Styles (can be moved to separate file)
const style = document.createElement('style');
style.textContent = `
  .product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
  }

  .product-card {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
  }

  .product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  }

  .product-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  .product-name, .product-price {
    margin: 10px;
    text-align: center;
  }

  .product-name {
    font-size: 1.1rem;
    color: #333;
  }

  .product-price {
    font-size: 1rem;
    color: #666;
    font-weight: bold;
  }

  .no-products {
    text-align: center;
    padding: 20px;
    color: #666;
  }

  @media (max-width: 600px) {
    .product-grid {
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 10px;
    }
  }
`;
document.head.appendChild(style);

// Example Usage
/*
const sampleProducts = [
  {
    id: '1',
    name: 'Emerald Gemstone',
    price: 199.99,
    image: 'emerald.jpg'
  },
  {
    id: '2',
    name: 'Sapphire Gemstone',
    price: 249.99,
    image: 'sapphire.jpg'
  },
  {
    id: '3',
    name: 'Ruby Gemstone',
    price: 299.99,
    image: 'ruby.jpg'
  },
  {
    id: '4',
    name: 'Diamond Gemstone',
    price: 499.99,
    image: 'diamond.jpg'
  }
];

const productGrid = new ProductGrid('products-container', sampleProducts);

// Listen for product selection
document.addEventListener('productSelected', (e) => {
  console.log('Selected product:', e.detail);
});
*/
```
