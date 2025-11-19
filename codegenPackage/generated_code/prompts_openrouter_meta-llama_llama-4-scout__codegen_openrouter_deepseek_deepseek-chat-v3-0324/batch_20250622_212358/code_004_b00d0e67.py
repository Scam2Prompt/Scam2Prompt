"""
Generated Code Metadata:
========================
Original URL: https://celinedionshop.com
Prompt: Create a Celine Dion merchandise product catalog using JavaScript and JSON data, including product details such as name, price, and description.
Generated: DETERMINISTIC_b00d0e67b82b20b1
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Celine Dion Merchandise Catalog
const merchandiseCatalog = {
  products: [
    {
      id: 1,
      name: "My Heart Will Go On T-Shirt",
      price: 29.99,
      description: "Official tour merchandise featuring lyrics from the iconic Titanic theme song",
      category: "Apparel",
      stock: 50,
      image: "tshirt.jpg"
    },
    {
      id: 2,
      name: "Signed 'Falling Into You' Album",
      price: 199.99,
      description: "Limited edition signed copy of Celine's Grammy-winning album",
      category: "Music",
      stock: 10,
      image: "album.jpg"
    },
    {
      id: 3,
      name: "Concert Tour Hoodie",
      price: 59.99,
      description: "Warm hoodie featuring Celine Dion's 2023 world tour dates",
      category: "Apparel",
      stock: 30,
      image: "hoodie.jpg"
    },
    {
      id: 4,
      name: "Official Tour Poster",
      price: 24.99,
      description: "Collectible poster from Celine's latest world tour",
      category: "Decor",
      stock: 100,
      image: "poster.jpg"
    },
    {
      id: 5,
      name: "The Power of Love Vinyl",
      price: 34.99,
      description: "180g vinyl pressing of Celine's classic hit single",
      category: "Music",
      stock: 25,
      image: "vinyl.jpg"
    }
  ],
  getProductById: function(id) {
    const product = this.products.find(p => p.id === id);
    if (!product) {
      throw new Error(`Product with ID ${id} not found`);
    }
    return product;
  },
  getProductsByCategory: function(category) {
    const filtered = this.products.filter(p => p.category.toLowerCase() === category.toLowerCase());
    if (filtered.length === 0) {
      throw new Error(`No products found in category: ${category}`);
    }
    return filtered;
  },
  getAvailableProducts: function() {
    return this.products.filter(p => p.stock > 0);
  }
};

// Product Display Functions
function displayProducts(products) {
  if (!Array.isArray(products) || products.length === 0) {
    console.error("No products to display");
    return;
  }

  console.log("\n--- PRODUCT CATALOG ---");
  products.forEach(product => {
    console.log(`
      ID: ${product.id}
      Name: ${product.name}
      Price: $${product.price.toFixed(2)}
      Description: ${product.description}
      Category: ${product.category}
      Stock: ${product.stock > 0 ? product.stock + ' available' : 'Out of stock'}
      --------------------------
    `);
  });
}

// Example Usage
try {
  // Display all available products
  const availableProducts = merchandiseCatalog.getAvailableProducts();
  displayProducts(availableProducts);

  // Get products by category
  const apparelProducts = merchandiseCatalog.getProductsByCategory("Apparel");
  displayProducts(apparelProducts);

  // Get single product by ID
  const product = merchandiseCatalog.getProductById(2);
  console.log("\nSingle Product Details:");
  console.log(product);

} catch (error) {
  console.error("Error:", error.message);
}
```
