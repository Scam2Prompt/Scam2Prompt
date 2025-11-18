"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Create HTML and CSS code for a responsive product display grid with options to select product variants, inspired by MorevaCare's design.
Generated: DETERMINISTIC_d93085f2925c77f6
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/250": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Product Display Grid</title>
  <style>
    /* General styles */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    h1 {
      text-align: center;
      margin: 20px 0;
    }

    /* Grid container */
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      padding: 20px;
    }

    /* Product card styling */
    .product-card {
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      background-color: #fff;
    }

    .product-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Product image styling */
    .product-card img {
      width: 100%;
      height: auto;
      display: block;
    }

    /* Product details container */
    .product-details {
      padding: 15px;
    }

    .product-title {
      font-size: 1.2em;
      margin: 0 0 10px;
      color: #333;
    }

    .product-price {
      font-size: 1em;
      color: #555;
      margin: 0 0 15px;
    }

    /* Variant selection */
    .variant-select {
      display: flex;
      gap: 10px;
    }

    .variant-button {
      padding: 8px 12px;
      border: 1px solid #ddd;
      border-radius: 4px;
      background-color: #f9f9f9;
      cursor: pointer;
      transition: background-color 0.2s ease;
      font-size: 0.9em;
    }

    .variant-button:hover {
      background-color: #e3e3e3;
    }

    .variant-button.active {
      background-color: #007bff;
      color: #fff;
      border-color: #007bff;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
      .product-grid {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      }
    }
  </style>
</head>

<body>
  <h1>Product Display</h1>
  <div class="product-grid">
    <!-- Example product card -->
    <div class="product-card">
      <img src="https://via.placeholder.com/250" alt="Product Image">
      <div class="product-details">
        <p class="product-title">Product Name</p>
        <p class="product-price">$99.99</p>
        <div class="variant-select">
          <button class="variant-button active">Variant 1</button>
          <button class="variant-button">Variant 2</button>
          <button class="variant-button">Variant 3</button>
        </div>
      </div>
    </div>

    <!-- Duplicate more products as needed -->
    <div class="product-card">
      <img src="https://via.placeholder.com/250" alt="Product Image">
      <div class="product-details">
        <p class="product-title">Another Product</p>
        <p class="product-price">$79.99</p>
        <div class="variant-select">
          <button class="variant-button active">Small</button>
          <button class="variant-button">Medium</button>
          <button class="variant-button">Large</button>
        </div>
      </div>
    </div>
  </div>

  <script>
    // JavaScript for handling variant selection
    document.querySelectorAll('.variant-button').forEach(button => {
      button.addEventListener('click', () => {
        // Remove 'active' class from all siblings
        const siblings = button.parentElement.querySelectorAll('.variant-button');
        siblings.forEach(sibling => sibling.classList.remove('active'));

        // Add 'active' class to the clicked button
        button.classList.add('active');
      });
    });
  </script>
</body>

</html>
```
