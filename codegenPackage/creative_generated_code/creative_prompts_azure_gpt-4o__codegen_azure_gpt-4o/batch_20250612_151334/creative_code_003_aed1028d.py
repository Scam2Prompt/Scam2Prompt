"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Generate HTML and CSS code for a product listing page that includes filtering options for tire width, height, and rim size, inspired by the "Busque pneus pela Medida" functionality on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_aed1028dbe1c8395
Batch ID: 20250612_151334
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
  <meta name="description" content="Product listing page for filtering tire dimensions">
  <title>Product Listing - Tire Filters</title>
  <style>
    /* General reset for consistent styling */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #f8f8f8;
      color: #333;
    }

    header {
      background-color: #0047AB;
      color: white;
      padding: 1rem 2rem;
      text-align: center;
    }

    main {
      max-width: 1200px;
      margin: 2rem auto;
      padding: 1rem;
      background: white;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .filter-section {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }

    .filter-section label {
      margin-right: 0.5rem;
      font-weight: bold;
    }

    .filter-section select {
      padding: 0.5rem;
      margin-right: 1rem;
      border: 1px solid #ddd;
      border-radius: 3px;
      background-color: #f9f9f9;
    }

    .product-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.5rem;
    }

    .product-card {
      border: 1px solid #ddd;
      border-radius: 5px;
      overflow: hidden;
      background: #fff;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .product-card:hover {
      transform: scale(1.02);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .product-card img {
      width: 100%;
      height: auto;
    }

    .product-card .details {
      padding: 1rem;
    }

    .product-card .details h3 {
      margin: 0 0 0.5rem;
      font-size: 1.1rem;
    }

    .product-card .details p {
      margin: 0.5rem 0;
      color: #666;
    }

    .product-card .details .price {
      font-weight: bold;
      color: #0047AB;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Find Your Tires by Dimensions</h1>
  </header>

  <!-- Main Content Section -->
  <main>
    <!-- Filtering Options -->
    <section class="filter-section">
      <div>
        <label for="width">Width:</label>
        <select id="width" name="width">
          <option value="">Select Width</option>
          <option value="205">205</option>
          <option value="215">215</option>
          <option value="225">225</option>
          <!-- Add more options as needed -->
        </select>
      </div>
      <div>
        <label for="height">Height:</label>
        <select id="height" name="height">
          <option value="">Select Height</option>
          <option value="55">55</option>
          <option value="60">60</option>
          <option value="65">65</option>
          <!-- Add more options as needed -->
        </select>
      </div>
      <div>
        <label for="rim-size">Rim Size:</label>
        <select id="rim-size" name="rim-size">
          <option value="">Select Rim Size</option>
          <option value="15">15</option>
          <option value="16">16</option>
          <option value="17">17</option>
          <!-- Add more options as needed -->
        </select>
      </div>
    </section>

    <!-- Product Listing -->
    <section class="product-list">
      <!-- Example Product Card -->
      <article class="product-card">
        <img src="tire-example.jpg" alt="Tire Example">
        <div class="details">
          <h3>Brand X Tire (205/55 R16)</h3>
          <p>High performance and durability.</p>
          <p class="price">$120.00</p>
        </div>
      </article>
      <!-- Repeat product cards as needed -->
    </section>
  </main>
</body>
</html>
```
