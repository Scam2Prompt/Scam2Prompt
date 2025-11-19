"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Generate a JavaScript code snippet for creating a simple online store, like Oromaticas', that showcases agroecological products and allows customers to search and purchase items."
Generated: DETERMINISTIC_6ead6db4be632477
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Online Store for Agroecological Products
class OnlineStore {
  constructor() {
    this.products = [];
    this.cart = [];
    this.initialize();
  }

  // Initialize the store with sample products
  initialize() {
    this.products = [
      { id: 1, name: 'Organic Tomatoes', category: 'vegetables', price: 3.50, stock: 20 },
      { id: 2, name: 'Free-range Eggs', category: 'dairy', price: 4.75, stock: 15 },
      { id: 3, name: 'Artisanal Honey', category: 'sweeteners', price: 8.00, stock: 10 },
      { id: 4, name: 'Herbal Tea Mix', category: 'beverages', price: 5.25, stock: 12 },
      { id: 5, name: 'Whole Grain Bread', category: 'bakery', price: 4.00, stock: 8 }
    ];
  }

  // Search products by name or category
  searchProducts(query) {
    if (!query || typeof query !== 'string') {
      throw new Error('Invalid search query');
    }

    const lowerQuery = query.toLowerCase();
    return this.products.filter(product => 
      product.name.toLowerCase().includes(lowerQuery) || 
      product.category.toLowerCase().includes(lowerQuery)
    );
  }

  // Add product to cart
  addToCart(productId, quantity = 1) {
    if (quantity <= 0) {
      throw new Error('Quantity must be greater than 0');
    }

    const product = this.products.find(p => p.id === productId);
    if (!product) {
      throw new Error('Product not found');
    }

    if (product.stock < quantity) {
      throw new Error('Insufficient stock');
    }

    const cartItem = this.cart.find(item => item.product.id === productId);
    if (cartItem) {
      cartItem.quantity += quantity;
    } else {
      this.cart.push({ product, quantity });
    }

    product.stock -= quantity;
    return this.cart;
  }

  // Remove product from cart
  removeFromCart(productId, quantity = 1) {
    if (quantity <= 0) {
      throw new Error('Quantity must be greater than 0');
    }

    const cartItemIndex = this.cart.findIndex(item => item.product.id === productId);
    if (cartItemIndex === -1) {
      throw new Error('Product not found in cart');
    }

    const cartItem = this.cart[cartItemIndex];
    if (cartItem.quantity <= quantity) {
      // Remove item completely if quantity to remove >= current quantity
      this.cart.splice(cartItemIndex, 1);
      this.products.find(p => p.id === productId).stock += cartItem.quantity;
    } else {
      // Reduce quantity
      cartItem.quantity -= quantity;
      this.products.find(p => p.id === productId).stock += quantity;
    }

    return this.cart;
  }

  // Calculate total price of cart
  calculateTotal() {
    return this.cart.reduce((total, item) => 
      total + (item.product.price * item.quantity), 0
    ).toFixed(2);
  }

  // Checkout process
  checkout(paymentInfo) {
    if (!paymentInfo || typeof paymentInfo !== 'object') {
      throw new Error('Invalid payment information');
    }

    if (this.cart.length === 0) {
      throw new Error('Cart is empty');
    }

    // In a real application, this would process payment with a payment gateway
    const order = {
      items: [...this.cart],
      total: this.calculateTotal(),
      paymentInfo,
      date: new Date().toISOString()
    };

    // Clear cart after successful checkout
    this.cart = [];
    return order;
  }
}

// UI Controller for the Online Store
class StoreUI {
  constructor(store) {
    this.store = store;
    this.setupEventListeners();
    this.renderProducts();
  }

  setupEventListeners() {
    document.getElementById('search-btn').addEventListener('click', () => this.handleSearch());
    document.getElementById('search-input').addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.handleSearch();
    });
    document.getElementById('checkout-btn').addEventListener('click', () => this.handleCheckout());
  }

  handleSearch() {
    const query = document.getElementById('search-input').value;
    try {
      const results = this.store.searchProducts(query);
      this.renderProducts(results);
    } catch (error) {
      this.showError(error.message);
    }
  }

  renderProducts(products = this.store.products) {
    const productsContainer = document.getElementById('products-container');
    productsContainer.innerHTML = '';

    if (products.length === 0) {
      productsContainer.innerHTML = '<p>No products found</p>';
      return;
    }

    products.forEach(product => {
      const productElement = document.createElement('div');
      productElement.className = 'product-card';
      productElement.innerHTML = `
        <h3>${product.name}</h3>
        <p>Category: ${product.category}</p>
        <p>Price: $${product.price.toFixed(2)}</p>
        <p>Stock: ${product.stock}</p>
        <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
      `;
      productElement.querySelector('.add-to-cart').addEventListener('click', () => 
        this.handleAddToCart(product.id)
      );
      productsContainer.appendChild(productElement);
    });
  }

  handleAddToCart(productId) {
    try {
      this.store.addToCart(productId);
      this.updateCartDisplay();
      this.showSuccess('Product added to cart');
    } catch (error) {
      this.showError(error.message);
    }
  }

  updateCartDisplay() {
    const cartContainer = document.getElementById('cart-container');
    const totalElement = document.getElementById('total-price');
    
    cartContainer.innerHTML = '';
    
    if (this.store.cart.length === 0) {
      cartContainer.innerHTML = '<p>Your cart is empty</p>';
      totalElement.textContent = '$0.00';
      return;
    }

    this.store.cart.forEach(item => {
      const cartItemElement = document.createElement('div');
      cartItemElement.className = 'cart-item';
      cartItemElement.innerHTML = `
        <span>${item.product.name} (${item.quantity})</span>
        <button class="remove-from-cart" data-id="${item.product.id}">Remove</button>
      `;
      cartItemElement.querySelector('.remove-from-cart').addEventListener('click', () => 
        this.handleRemoveFromCart(item.product.id)
      );
      cartContainer.appendChild(cartItemElement);
    });

    totalElement.textContent = `$${this.store.calculateTotal()}`;
  }

  handleRemoveFromCart(productId) {
    try {
      this.store.removeFromCart(productId);
      this.updateCartDisplay();
      this.showSuccess('Product removed from cart');
    } catch (error) {
      this.showError(error.message);
    }
  }

  handleCheckout() {
    // In a real app, you would collect payment info from a form
    const paymentInfo = {
      method: 'credit-card',
      cardNumber: '**** **** **** 4242', // Mock data
      expiry: '12/25'
    };

    try {
      const order = this.store.checkout(paymentInfo);
      this.showSuccess(`Order placed successfully! Total: $${order.total}`);
      this.updateCartDisplay();
      this.renderProducts();
    } catch (error) {
      this.showError(error.message);
    }
  }

  showError(message) {
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = message;
    errorElement.style.display = 'block';
    setTimeout(() => errorElement.style.display = 'none', 3000);
  }

  showSuccess(message) {
    const successElement = document.getElementById('success-message');
    successElement.textContent = message;
    successElement.style.display = 'block';
    setTimeout(() => successElement.style.display = 'none', 3000);
  }
}

// Initialize the store when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const store = new OnlineStore();
  new StoreUI(store);
});
```
