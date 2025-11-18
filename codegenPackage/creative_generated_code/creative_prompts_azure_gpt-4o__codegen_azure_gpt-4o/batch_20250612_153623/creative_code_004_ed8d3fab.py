"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://help-phatom.teachable.com
Prompt: Write HTML and CSS code to replicate the "Sort by" and "Product filters" functionality described on the Teachable help page.
Generated: DETERMINISTIC_ed8d3fab8fd81751
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sort By and Product Filters</title>
  <style>
    /* General styles for the container */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .container {
      max-width: 1200px;
      margin: 20px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    .filters {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      margin-bottom: 30px;
    }
    .filter-group {
      flex: 1;
      min-width: 200px;
    }
    label {
      display: block;
      font-weight: bold;
      margin-bottom: 8px;
    }
    select, input[type="checkbox"] {
      width: 100%;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .product-list {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }
    .product {
      flex: 1;
      min-width: 300px;
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 15px;
      background-color: #fafafa;
    }
    .product h3 {
      margin: 0 0 10px 0;
    }
    button {
      background-color: #007bff;
      border: none;
      color: white;
      padding: 10px 15px;
      text-align: center;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Filters Section -->
    <div class="filters">
      <!-- Sort By Filter -->
      <div class="filter-group">
        <label for="sort-by">Sort by</label>
        <select id="sort-by">
          <option value="price-asc">Price: Low to High</option>
          <option value="price-desc">Price: High to Low</option>
          <option value="name-asc">Name: A to Z</option>
          <option value="name-desc">Name: Z to A</option>
        </select>
      </div>
      <!-- Product Filters -->
      <div class="filter-group">
        <label>Product Filters</label>
        <div>
          <input type="checkbox" id="filter-sale" value="sale">
          <label for="filter-sale">On Sale</label>
        </div>
        <div>
          <input type="checkbox" id="filter-in-stock" value="in-stock">
          <label for="filter-in-stock">In Stock</label>
        </div>
        <div>
          <input type="checkbox" id="filter-new-arrival" value="new-arrival">
          <label for="filter-new-arrival">New Arrival</label>
        </div>
      </div>
    </div>

    <!-- Product List Section -->
    <div class="product-list">
      <div class="product">
        <h3>Product 1</h3>
        <p>Price: $10</p>
        <button>Buy Now</button>
      </div>
      <div class="product">
        <h3>Product 2</h3>
        <p>Price: $20</p>
        <button>Buy Now</button>
      </div>
      <div class="product">
        <h3>Product 3</h3>
        <p>Price: $30</p>
        <button>Buy Now</button>
      </div>
      <!-- Add more products as needed -->
    </div>
  </div>
</body>
</html>
```
