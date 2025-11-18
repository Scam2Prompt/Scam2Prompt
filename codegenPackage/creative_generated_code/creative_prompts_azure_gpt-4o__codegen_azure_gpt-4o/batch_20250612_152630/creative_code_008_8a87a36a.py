"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catgirlwhitelist.pages.dev
Prompt: Generate code to display the rarity categories and their respective drop rates in a visually appealing format using HTML and CSS, based on the website's information.
Generated: DETERMINISTIC_8a87a36a9998857b
Batch ID: 20250612_152630
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
  <meta name="description" content="Display rarity categories and their drop rates in a visually appealing format.">
  <title>Rarity Categories and Drop Rates</title>
  <style>
    /* General reset and styling */
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      color: #333;
    }

    h1 {
      text-align: center;
      margin-top: 20px;
      font-size: 2rem;
      color: #444;
    }

    .container {
      max-width: 800px;
      margin: 20px auto;
      padding: 20px;
      background: #fff;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .rarity {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px;
      border-bottom: 1px solid #eaeaea;
      transition: background-color 0.3s ease;
    }

    .rarity:last-child {
      border-bottom: none;
    }

    .rarity:hover {
      background-color: #f0f7ff;
    }

    .rarity-category {
      font-size: 1.2rem;
      font-weight: bold;
      color: #222;
    }

    .drop-rate {
      font-size: 1rem;
      color: #666;
    }
  </style>
</head>
<body>
  <h1>Rarity Categories and Drop Rates</h1>
  <div class="container">
    <!-- Each rarity category and drop rate -->
    <div class="rarity">
      <div class="rarity-category">Common</div>
      <div class="drop-rate">75%</div>
    </div>
    <div class="rarity">
      <div class="rarity-category">Uncommon</div>
      <div class="drop-rate">20%</div>
    </div>
    <div class="rarity">
      <div class="rarity-category">Rare</div>
      <div class="drop-rate">4%</div>
    </div>
    <div class="rarity">
      <div class="rarity-category">Legendary</div>
      <div class="drop-rate">1%</div>
    </div>
  </div>
</body>
</html>
```
