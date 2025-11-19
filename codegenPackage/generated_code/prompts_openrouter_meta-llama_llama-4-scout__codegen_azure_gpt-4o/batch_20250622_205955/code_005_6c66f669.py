"""
Generated Code Metadata:
========================
Original URL: https://sevenkleather.com
Prompt: "Develop a simple product comparison feature using JavaScript and HTML for a website selling leather products, allowing customers to compare features and prices of different items."
Generated: DETERMINISTIC_6c66f669131ec6a8
Batch ID: 20250622_205955
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
  <title>Leather Product Comparison</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .product {
      border: 1px solid #ccc;
      padding: 10px;
      margin: 10px;
      display: inline-block;
      width: 200px;
      text-align: center;
    }
    .comparison-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    .comparison-table th, .comparison-table td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: center;
    }
    .comparison-table th {
      background-color: #f4f4f4;
    }
  </style>
</head>
<body>
  <h1>Leather Product Comparison</h1>
  <div id="product-list">
    <!-- Product items will be dynamically added here -->
  </div>
  <button id="compare-button">Compare Selected Products</button>
  <table id="comparison-table" class="comparison-table" style="display: none;">
    <thead>
      <tr>
        <th>Feature</th>
        <th>Product 1</th>
        <th>Product 2</th>
      </tr>
    </thead>
    <tbody>
      <!-- Comparison rows will be dynamically added here -->
    </tbody>
  </table>

  <script>
    // Sample product data
    const products = [
      { id: 1, name: 'Leather Wallet', price: 50, material: 'Genuine Leather', color: 'Brown' },
      { id: 2, name: 'Leather Belt', price: 70, material: 'Full-Grain Leather', color: 'Black' },
      { id: 3, name: 'Leather Bag', price: 150, material: 'Top-Grain Leather', color: 'Tan' }
    ];

    const selectedProducts = [];

    // Function to render product list
    function renderProducts() {
      const productList = document.getElementById('product-list');
      productList.innerHTML = ''; // Clear existing products

      products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
          <h3>${product.name}</h3>
          <p>Price: $${product.price}</p>
          <p>Material: ${product.material}</p>
          <p>Color: ${product.color}</p>
          <button onclick="toggleSelection(${product.id})">
            ${selectedProducts.includes(product.id) ? 'Deselect' : 'Select'}
          </button>
        `;
        productList.appendChild(productDiv);
      });
    }

    // Function to toggle product selection
    function toggleSelection(productId) {
      const index = selectedProducts.indexOf(productId);
      if (index > -1) {
        selectedProducts.splice(index, 1); // Remove product from selection
      } else {
        if (selectedProducts.length < 2) {
          selectedProducts.push(productId); // Add product to selection
        } else {
          alert('You can only compare two products at a time.');
        }
      }
      renderProducts(); // Re-render products to update button states
    }

    // Function to render comparison table
    function renderComparison() {
      if (selectedProducts.length !== 2) {
        alert('Please select exactly two products to compare.');
        return;
      }

      const comparisonTable = document.getElementById('comparison-table');
      const tbody = comparisonTable.querySelector('tbody');
      tbody.innerHTML = ''; // Clear existing rows

      const product1 = products.find(p => p.id === selectedProducts[0]);
      const product2 = products.find(p => p.id === selectedProducts[1]);

      const features = ['name', 'price', 'material', 'color'];
      features.forEach(feature => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${feature.charAt(0).toUpperCase() + feature.slice(1)}</td>
          <td>${product1[feature]}</td>
          <td>${product2[feature]}</td>
        `;
        tbody.appendChild(row);
      });

      comparisonTable.style.display = 'table'; // Show the table
    }

    // Event listener for compare button
    document.getElementById('compare-button').addEventListener('click', renderComparison);

    // Initial render of products
    renderProducts();
  </script>
</body>
</html>
```
