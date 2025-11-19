"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: Write JavaScript code to implement a dynamic product carousel for showcasing Ecoplast sheets, such as "ECOPLAST GREY GALAXY STARS-S6" and "ECOPLAST WHISPER GALAXY STARS-S8."
Generated: DETERMINISTIC_cf4d9999792aa885
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProductCarousel.js

/**
 * A dynamic product carousel for showcasing Ecoplast sheets.
 */

class ProductCarousel {
  /**
   * Constructor for ProductCarousel.
   * @param {HTMLElement} container - The container element for the carousel.
   * @param {Array<string>} products - An array of product names.
   */
  constructor(container, products) {
    this.container = container;
    this.products = products;
    this.currentIndex = 0;
    this.carouselInterval = 5000; // 5 seconds

    // Initialize the carousel.
    this.init();
  }

  /**
   * Initialize the carousel.
   */
  init() {
    // Create the carousel container.
    this.container.classList.add('product-carousel');

    // Create the product list.
    this.productList = document.createElement('div');
    this.productList.classList.add('product-list');
    this.container.appendChild(this.productList);

    // Create the product navigation.
    this.productNav = document.createElement('div');
    this.productNav.classList.add('product-nav');
    this.container.appendChild(this.productNav);

    // Populate the product list and navigation.
    this.products.forEach((product, index) => {
      const productElement = document.createElement('div');
      productElement.classList.add('product');
      productElement.textContent = product;
      this.productList.appendChild(productElement);

      const navButton = document.createElement('button');
      navButton.textContent = `${index + 1}`;
      navButton.addEventListener('click', () => this.navigateTo(index));
      this.productNav.appendChild(navButton);
    });

    // Set up the carousel interval.
    this.intervalId = setInterval(() => this.navigateNext(), this.carouselInterval);

    // Show the first product.
    this.showProduct(0);
  }

  /**
   * Show a product at the specified index.
   * @param {number} index - The index of the product to show.
   */
  showProduct(index) {
    // Hide all products.
    Array.from(this.productList.children).forEach((product) => {
      product.classList.remove('active');
    });

    // Show the selected product.
    this.productList.children[index].classList.add('active');

    // Update the navigation.
    Array.from(this.productNav.children).forEach((button, buttonIndex) => {
      if (buttonIndex === index) {
        button.classList.add('active');
      } else {
        button.classList.remove('active');
      }
    });

    // Update the current index.
    this.currentIndex = index;
  }

  /**
   * Navigate to the next product.
   */
  navigateNext() {
    const nextIndex = (this.currentIndex + 1) % this.products.length;
    this.showProduct(nextIndex);
  }

  /**
   * Navigate to a specific product.
   * @param {number} index - The index of the product to navigate to.
   */
  navigateTo(index) {
    // Clear the interval to prevent multiple intervals.
    clearInterval(this.intervalId);

    // Show the selected product.
    this.showProduct(index);

    // Reset the interval.
    this.intervalId = setInterval(() => this.navigateNext(), this.carouselInterval);
  }

  /**
   * Dispose of the carousel.
   */
  dispose() {
    // Clear the interval.
    clearInterval(this.intervalId);

    // Remove event listeners.
    Array.from(this.productNav.children).forEach((button) => {
      button.removeEventListener('click', () => {});
    });
  }
}

// Example usage:
const products = [
  "ECOPLAST GREY GALAXY STARS-S6",
  "ECOPLAST WHISPER GALAXY STARS-S8",
  "ECOPLAST SILVER MOON-S10",
];

const carouselContainer = document.getElementById('product-carousel');
const carousel = new ProductCarousel(carouselContainer, products);
```

```css
/* styles.css */

.product-carousel {
  position: relative;
  width: 800px;
  height: 600px;
}

.product-list {
  position: relative;
  width: 100%;
  height: 100%;
}

.product {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: none;
}

.product.active {
  display: block;
}

.product-nav {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  text-align: center;
}

.product-nav button {
  width: 30px;
  height: 30px;
  margin: 10px;
  border: none;
  border-radius: 50%;
  background-color: #ccc;
  cursor: pointer;
}

.product-nav button.active {
  background-color: #333;
  color: #fff;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ecoplast Product Carousel</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="product-carousel"></div>
  <script src="ProductCarousel.js"></script>
</body>
</html>
```
