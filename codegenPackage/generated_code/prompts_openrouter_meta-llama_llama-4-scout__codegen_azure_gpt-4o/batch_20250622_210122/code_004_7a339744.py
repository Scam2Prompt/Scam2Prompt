"""
Generated Code Metadata:
========================
Original URL: https://44-cm7.pages.dev
Prompt: Create a simple HTML/CSS template for a collectible item page, inspired by the Pudgy Penguins "GoldFeathers" collectible on NTWRK.
Generated: DETERMINISTIC_7a33974471d7b241
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Collectible Item Page for Pudgy Penguins 'GoldFeathers'">
  <title>GoldFeathers Collectible</title>
  <style>
    /* General Reset */
    body, h1, h2, p, ul, li, img {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Body Styling */
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      color: #333;
      line-height: 1.6;
      margin: 0;
    }

    /* Container Styling */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }

    /* Header Styling */
    header {
      text-align: center;
      padding: 20px 0;
      background-color: #ffd700; /* Gold color for collectible theme */
      color: #fff;
    }

    header h1 {
      font-size: 2.5rem;
      font-weight: bold;
    }

    header p {
      font-size: 1.2rem;
    }

    /* Main Content Styling */
    .main-content {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      margin-top: 20px;
    }

    /* Item Image Section */
    .item-image {
      flex: 1 1 40%;
      text-align: center;
    }

    .item-image img {
      max-width: 100%;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Item Details Section */
    .item-details {
      flex: 1 1 60%;
    }

    .item-details h2 {
      font-size: 2rem;
      margin-bottom: 10px;
    }

    .item-details p {
      margin-bottom: 15px;
    }

    .item-details ul {
      list-style-type: none;
      padding: 0;
    }

    .item-details ul li {
      margin-bottom: 10px;
    }

    /* Footer Styling */
    footer {
      text-align: center;
      padding: 10px 0;
      background-color: #333;
      color: #fff;
      margin-top: 20px;
    }

    footer p {
      font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>GoldFeathers Collectible</h1>
    <p>Exclusive Pudgy Penguins Collectible on NTWRK</p>
  </header>

  <!-- Main Content Section -->
  <div class="container">
    <div class="main-content">
      <!-- Item Image -->
      <div class="item-image">
        <img src="goldfeathers.jpg" alt="GoldFeathers Collectible">
      </div>

      <!-- Item Details -->
      <div class="item-details">
        <h2>About GoldFeathers</h2>
        <p>GoldFeathers is a rare collectible from the Pudgy Penguins series, available exclusively on NTWRK.</p>
        <ul>
          <li><strong>Edition:</strong> Limited</li>
          <li><strong>Material:</strong> Gold-plated resin</li>
          <li><strong>Dimensions:</strong> 5" x 3" x 3"</li>
          <li><strong>Release Date:</strong> October 2023</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 Pudgy Penguins. All rights reserved.</p>
  </footer>
</body>
</html>
```
