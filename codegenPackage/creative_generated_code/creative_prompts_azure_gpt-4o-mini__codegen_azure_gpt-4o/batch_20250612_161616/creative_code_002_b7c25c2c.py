"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seubolodecorado.com.br
Prompt: Create a sample HTML form for customers to customize their Bentô Cake order, allowing them to select flavors, themes, and additional treats.
Generated: DETERMINISTIC_b7c25c2c6e85aeac
Batch ID: 20250612_161616
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
  <title>Bentô Cake Customization</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 400px;
      margin: auto;
    }
    label {
      display: block;
      margin-top: 10px;
    }
    input[type="text"],
    select,
    button {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <h1>Bentô Cake Customization Form</h1>
  <form action="/submit-order" method="POST">
    <!-- Customer Name -->
    <label for="customerName">Your Name:</label>
    <input type="text" id="customerName" name="customerName" placeholder="Enter your name" required>

    <!-- Cake Flavor Selection -->
    <label for="cakeFlavor">Choose a Flavor:</label>
    <select id="cakeFlavor" name="cakeFlavor" required>
      <option value="" disabled selected>Select a flavor</option>
      <option value="vanilla">Vanilla</option>
      <option value="chocolate">Chocolate</option>
      <option value="strawberry">Strawberry</option>
      <option value="matcha">Matcha</option>
    </select>

    <!-- Cake Theme -->
    <label for="cakeTheme">Choose a Theme:</label>
    <select id="cakeTheme" name="cakeTheme" required>
      <option value="" disabled selected>Select a theme</option>
      <option value="minimalist">Minimalist</option>
      <option value="floral">Floral</option>
      <option value="cartoon">Cartoon</option>
      <option value="abstract">Abstract</option>
    </select>

    <!-- Additional Treats -->
    <label for="additionalTreats">Add Extra Treats:</label>
    <select id="additionalTreats" name="additionalTreats[]" multiple>
      <option value="macaron">Macarons</option>
      <option value="cookies">Cookies</option>
      <option value="chocolates">Chocolates</option>
      <option value="fruits">Fresh Fruits</option>
    </select>
    <p style="font-size: 0.9em; color: gray;">(Hold Ctrl or Command to select multiple)</p>

    <!-- Submit Button -->
    <button type="submit">Submit Your Order</button>
  </form>
</body>
</html>
```
