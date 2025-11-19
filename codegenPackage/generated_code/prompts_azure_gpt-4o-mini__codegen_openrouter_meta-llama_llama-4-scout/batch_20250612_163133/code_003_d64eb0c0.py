"""
Generated Code Metadata:
========================
Original URL: https://radical-wear.cz
Prompt: Develop a CSS style guide for an online clothing store that includes options for different skin colors and layout modes, as seen on Radical Wear.
Generated: DETERMINISTIC_d64eb0c074743a5c
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I must point out that the request seems to be asking for CSS, but the conversation started with a request for a programming language (implied by "expert. Generate clean, working code"). I will assume a common programming language for web development and provide CSS as per the request.

However, I will provide a basic CSS style guide as requested. For dynamic skin color and layout mode changes, JavaScript would be required. I'll provide a basic example in CSS and a simple JavaScript example.

### CSS (style.css)

```css
/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Layout Modes */
.layout-mode-dark {
  background-color: #333;
  color: #fff;
}

.layout-mode-light {
  background-color: #f9f9f9;
  color: #333;
}

/* Skin Colors */
.skin-color-fair {
  --primary-color: #f7d2c4;
}

.skin-color-medium {
  --primary-color: #e5b497;
}

.skin-color-dark {
  --primary-color: #c67a73;
}

.product {
  background-color: var(--primary-color);
  padding: 20px;
  margin: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.product img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.product .details {
  padding: 20px;
}

.product .name {
  font-weight: bold;
  font-size: 18px;
  margin-bottom: 10px;
}

.product .price {
  font-size: 16px;
  color: #666;
}

/* Responsive Design */
@media (max-width: 768px) {
  .product {
    margin: 10px;
    padding: 10px;
  }
}
```

### JavaScript (script.js)

```javascript
// Get all skin color and layout mode buttons
const skinColorButtons = document.querySelectorAll('.skin-color-button');
const layoutModeButtons = document.querySelectorAll('.layout-mode-button');

// Add event listeners to skin color buttons
skinColorButtons.forEach(button => {
  button.addEventListener('click', () => {
    const skinColor = button.dataset.skinColor;
    document.body.classList.remove('skin-color-fair', 'skin-color-medium', 'skin-color-dark');
    document.body.classList.add(`skin-color-${skinColor}`);
  });
});

// Add event listeners to layout mode buttons
layoutModeButtons.forEach(button => {
  button.addEventListener('click', () => {
    const layoutMode = button.dataset.layoutMode;
    document.body.classList.remove('layout-mode-dark', 'layout-mode-light');
    document.body.classList.add(`layout-mode-${layoutMode}`);
  });
});
```

### HTML (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Online Clothing Store</title>
  <link rel="stylesheet" href="style.css">
</head>
<body class="skin-color-fair layout-mode-light">
  <h1>Online Clothing Store</h1>
  <button class="skin-color-button" data-skin-color="fair">Fair</button>
  <button class="skin-color-button" data-skin-color="medium">Medium</button>
  <button class="skin-color-button" data-skin-color="dark">Dark</button>
  <button class="layout-mode-button" data-layout-mode="light">Light</button>
  <button class="layout-mode-button" data-layout-mode="dark">Dark</button>
  <div class="products">
    <div class="product">
      <img src="product1.jpg" alt="Product 1">
      <div class="details">
        <h2 class="name">Product 1</h2>
        <p class="price">$19.99</p>
      </div>
    </div>
    <div class="product">
      <img src="product2.jpg" alt="Product 2">
      <div class="details">
        <h2 class="name">Product 2</h2>
        <p class="price">$29.99</p>
      </div>
    </div>
  </div>
  <script src="script.js"></script>
</body>
</html>
```
