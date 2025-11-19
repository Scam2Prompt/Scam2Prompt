"""
Generated Code Metadata:
========================
Original URL: https://familyicon.ru
Prompt: "Write a code snippet in JavaScript to implement a simple e-commerce functionality for a religious item store, focusing on product categorization and shopping cart management, inspired by the structure of https://familyicon.ru."
Generated: DETERMINISTIC_b7af32ae34941666
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// E-commerce functionality for a religious item store

// Product data structure
const products = [
  {
    id: 1,
    name: "Orthodox Cross",
    category: "Jewelry",
    price: 49.99,
    description: "Handcrafted silver cross with intricate details.",
    image: "cross.jpg",
    stock: 10
  },
  {
    id: 2,
    name: "Prayer Book",
    category: "Books",
    price: 19.99,
    description: "Daily prayers and liturgical texts.",
    image: "prayer-book.jpg",
    stock: 25
  },
  {
    id: 3,
    name: "Icon of Christ",
    category: "Icons",
    price: 89.99,
    description: "Hand-painted wooden icon of Jesus Christ.",
    image: "christ-icon.jpg",
    stock: 5
  }
];

// Shopping cart implementation
class ShoppingCart {
  constructor() {
    this.items = [];
  }

  addItem(product, quantity = 1) {
    if (!product || typeof product !== 'object') {
      throw new Error('Invalid product');
    }

    if (quantity <= 0 || !Number.isInteger(quantity)) {
      throw new Error('Quantity must be a positive integer');
    }

    const existingItem = this.items.find(item => item.product.id === product.id);

    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.items.push({ product, quantity });
    }

    this.saveToLocalStorage();
    return this.items;
  }

  removeItem(productId) {
    if (!productId) {
      throw new Error('Product ID is required');
    }

    this.items = this.items.filter(item => item.product.id !== productId);
    this.saveToLocalStorage();
    return this.items;
  }

  updateQuantity(productId, newQuantity) {
    if (!productId || newQuantity <= 0 || !Number.isInteger(newQuantity)) {
      throw new Error('Invalid parameters');
    }

    const item = this.items.find(item => item.product.id === productId);
    if (item) {
      item.quantity = newQuantity;
    }

    this.saveToLocalStorage();
    return this.items;
  }

  calculateTotal() {
    return this.items.reduce((total, item) => {
      return total + (item.product.price * item.quantity);
    }, 0);
  }

  getItemCount() {
    return this.items.reduce((count, item) => count + item.quantity, 0);
  }

  clearCart() {
    this.items = [];
    this.saveToLocalStorage();
  }

  saveToLocalStorage() {
    try {
      localStorage.setItem('shoppingCart', JSON.stringify(this.items));
    } catch (error) {
      console.error('Error saving cart to localStorage:', error);
    }
  }

  loadFromLocalStorage() {
    try {
      const savedCart = localStorage.getItem('shoppingCart');
      if (savedCart) {
        this.items = JSON.parse(savedCart);
      }
    } catch (error) {
      console.error('Error loading cart from localStorage:', error);
    }
  }
}

// Product categorization
class ProductCategorizer {
  constructor(products) {
    this.products = products;
  }

  getCategories() {
    const categories = new Set();
    this.products.forEach(product => categories.add(product.category));
    return Array.from(categories);
  }

  getProductsByCategory(category) {
    if (!category) {
      throw new Error('Category is required');
    }
    return this.products.filter(product => product.category === category);
  }

  searchProducts(query) {
    if (!query || typeof query !== 'string') {
      return [];
    }
    const lowerQuery = query.toLowerCase();
    return this.products.filter(product => 
      product.name.toLowerCase().includes(lowerQuery) || 
      product.description.toLowerCase().includes(lowerQuery)
    );
  }
}

// UI Integration (example usage)
document.addEventListener('DOMContentLoaded', () => {
  const cart = new ShoppingCart();
  cart.loadFromLocalStorage();
  
  const categorizer = new ProductCategorizer(products);
  const categories = categorizer.getCategories();
  
  // Example: Display categories in UI
  const categoryList = document.getElementById('category-list');
  if (categoryList) {
    categories.forEach(category => {
      const li = document.createElement('li');
      li.textContent = category;
      li.addEventListener('click', () => {
        displayProducts(categorizer.getProductsByCategory(category));
      });
      categoryList.appendChild(li);
    });
  }

  // Example: Display cart count
  updateCartCount();

  function displayProducts(products) {
    // Implementation would render products to the page
    console.log('Displaying products:', products);
  }

  function updateCartCount() {
    const cartCountElement = document.getElementById('cart-count');
    if (cartCountElement) {
      cartCountElement.textContent = cart.getItemCount();
    }
  }

  // Example: Add to cart button handler
  document.addEventListener('click', (e) => {
    if (e.target.classList.contains('add-to-cart')) {
      const productId = parseInt(e.target.dataset.productId);
      const product = products.find(p => p.id === productId);
      if (product) {
        cart.addItem(product);
        updateCartCount();
      }
    }
  });
});
```
