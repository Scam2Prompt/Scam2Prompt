"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Create a JavaScript function that can be used to display a list of products with different sizes, styles, and designs, like the 'Skladové okná' section on nellyservis.sk."
Generated: DETERMINISTIC_6d8948669a2efe9b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product class representing a product with different sizes, styles, and designs.
 */
class Product {
  /**
   * @param {string} name - Product name.
   * @param {string[]} sizes - Array of available sizes.
   * @param {string[]} styles - Array of available styles.
   * @param {string[]} designs - Array of available designs.
   * @param {number} price - Product price.
   */
  constructor(name, sizes, styles, designs, price) {
    this.name = name;
    this.sizes = sizes;
    this.styles = styles;
    this.designs = designs;
    this.price = price;
  }
}

/**
 * ProductList class representing a list of products.
 */
class ProductList {
  /**
   * @param {Product[]} products - Array of products.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Render the product list as HTML.
   * @returns {string} HTML string representing the product list.
   */
  render() {
    let html = '';
    this.products.forEach((product) => {
      html += `
        <div class="product">
          <h2>${product.name}</h2>
          <p> Sizes: ${product.sizes.join(', ')} </p>
          <p> Styles: ${product.styles.join(', ')} </p>
          <p> Designs: ${product.designs.join(', ')} </p>
          <p> Price: ${product.price} € </p>
        </div>
      `;
    });
    return html;
  }
}

/**
 * Function to display a list of products.
 * @param {Product[]} products - Array of products to display.
 */
function displayProductList(products) {
  try {
    if (!Array.isArray(products)) {
      throw new Error('Products must be an array.');
    }

    const productList = new ProductList(products);
    const productListHtml = productList.render();

    // Example usage: append the HTML to a container element
    const container = document.getElementById('product-list-container');
    if (container) {
      container.innerHTML = productListHtml;
    } else {
      console.error('Container element not found.');
    }
  } catch (error) {
    console.error('Error displaying product list:', error.message);
  }
}

// Example usage
const products = [
  new Product(
    'Window 1',
    ['Small', 'Medium', 'Large'],
    ['Modern', 'Classic'],
    ['Wooden', 'Metal'],
    100
  ),
  new Product(
    'Window 2',
    ['Small', 'Medium'],
    ['Modern'],
    ['Wooden', 'Plastic'],
    80
  ),
];

displayProductList(products);
```
