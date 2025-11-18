"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Create a user-friendly web interface in HTML/CSS/JavaScript for managing cryptocurrency investments, inspired by Tslaspacetrade's workflow and design.
Generated: DETERMINISTIC_c027ddb2a40eac46
Batch ID: 20250612_154603
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
  <title>Crypto Investment Manager</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Crypto Investment Manager</h1>
  </header>

  <!-- Main Content Section -->
  <main>
    <section class="portfolio">
      <h2>Your Portfolio</h2>
      <table id="portfolioTable">
        <thead>
          <tr>
            <th>Cryptocurrency</th>
            <th>Quantity</th>
            <th>Price (USD)</th>
            <th>Value (USD)</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <!-- Dynamically populated rows -->
        </tbody>
      </table>
    </section>

    <section class="add-investment">
      <h2>Add New Investment</h2>
      <form id="addInvestmentForm">
        <label for="cryptoName">Cryptocurrency:</label>
        <input type="text" id="cryptoName" name="cryptoName" required>
        
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity" step="any" required>
        
        <label for="price">Price (USD):</label>
        <input type="number" id="price" name="price" step="any" required>
        
        <button type="submit">Add Investment</button>
      </form>
    </section>
  </main>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 Crypto Investment Manager. All rights reserved.</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f0f0f0;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1rem;
  text-align: center;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 0.5rem;
  position: fixed;
  bottom: 0;
  width: 100%;
}

main {
  padding: 1rem;
}

h1, h2 {
  color: #333;
}

/* Table Styles */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
}

th, td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: left;
}

th {
  background-color: #333;
  color: #fff;
}

/* Form Styles */
form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

input, button {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #333;
  color: #fff;
  cursor: pointer;
}

button:hover {
  background-color: #555;
}
```

```javascript
// script.js

// Initialize an empty portfolio
let portfolio = [];

// Function to calculate the total value of a cryptocurrency investment
function calculateValue(quantity, price) {
  return quantity * price;
}

// Function to update the portfolio table
function updatePortfolioTable() {
  const tableBody = document.querySelector('#portfolioTable tbody');
  tableBody.innerHTML = ''; // Clear current rows

  portfolio.forEach((investment, index) => {
    const { cryptoName, quantity, price } = investment;
    const value = calculateValue(quantity, price);

    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${cryptoName}</td>
      <td>${quantity}</td>
      <td>${price.toFixed(2)}</td>
      <td>${value.toFixed(2)}</td>
      <td><button class="delete-btn" data-index="${index}">Delete</button></td>
    `;
    tableBody.appendChild(row);
  });

  // Attach delete handlers
  document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', handleDelete);
  });
}

// Function to handle adding an investment
function handleAddInvestment(event) {
  event.preventDefault(); // Prevent form submission

  const cryptoName = document.getElementById('cryptoName').value.trim();
  const quantity = parseFloat(document.getElementById('quantity').value);
  const price = parseFloat(document.getElementById('price').value);

  if (!cryptoName || isNaN(quantity) || isNaN(price) || quantity <= 0 || price <= 0) {
    alert('Please provide valid input values.');
    return;
  }

  portfolio.push({ cryptoName, quantity, price });
  updatePortfolioTable();

  // Clear the form
  event.target.reset();
}

// Function to handle deleting an investment
function handleDelete(event) {
  const index = parseInt(event.target.dataset.index, 10);
  if (isNaN(index) || index < 0 || index >= portfolio.length) {
    alert('Invalid investment index.');
    return;
  }

  portfolio.splice(index, 1); // Remove the investment from the portfolio
  updatePortfolioTable();
}

// Attach event listener to the form
document.getElementById('addInvestmentForm').addEventListener('submit', handleAddInvestment);

// Initial table update
updatePortfolioTable();
```
