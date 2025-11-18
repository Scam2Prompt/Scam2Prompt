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
    <title>Cryptocurrency Investment Manager</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Cryptocurrency Investment Manager</h1>
    </header>
    <main>
        <section id="investment-form">
            <h2>Add Investment</h2>
            <form id="investmentForm">
                <label for="cryptoName">Cryptocurrency Name:</label>
                <input type="text" id="cryptoName" required>
                
                <label for="amountInvested">Amount Invested ($):</label>
                <input type="number" id="amountInvested" required min="0.01" step="0.01">
                
                <label for="currentPrice">Current Price ($):</label>
                <input type="number" id="currentPrice" required min="0.01" step="0.01">

                <button type="submit">Add Investment</button>
            </form>
        </section>
        
        <section id="investment-list">
            <h2>Your Investments</h2>
            <table id="investmentsTable">
                <thead>
                    <tr>
                        <th>Cryptocurrency</th>
                        <th>Amount Invested</th>
                        <th>Current Price</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Investment entries will be dynamically added here -->
                </tbody>
            </table>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Cryptocurrency Investment Manager</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

h1 {
    color: #333;
}

section {
    background: white;
    margin: 0 auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin: 10px 0 5px;
}

input {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th, td {
    padding: 10px;
    border: 1px solid #ddd;
    text-align: center;
}

th {
    background-color: #f2f2f2;
}
```

```javascript
// script.js

// Initialize an empty array to store investments
let investments = [];

// Function to handle form submission
document.getElementById('investmentForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    
    // Retrieve values from the form
    const cryptoName = document.getElementById('cryptoName').value;
    const amountInvested = parseFloat(document.getElementById('amountInvested').value);
    const currentPrice = parseFloat(document.getElementById('currentPrice').value);
    
    // Validate inputs
    if (!cryptoName || amountInvested <= 0 || currentPrice <= 0) {
        alert('Please fill out all fields with valid values.');
        return;
    }
    
    // Create a new investment object
    const investment = {
        cryptoName,
        amountInvested,
        currentPrice,
        value: amountInvested * (currentPrice / amountInvested), // Calculate the value
    };
    
    // Add the investment to the investments array
    investments.push(investment);
    
    // Update the investment table
    updateInvestmentTable();
    
    // Clear the form fields
    document.getElementById('investmentForm').reset();
});

// Function to update the investments table
function updateInvestmentTable() {
    const tableBody = document.getElementById('investmentsTable').querySelector('tbody');
    tableBody.innerHTML = ''; // Clear the existing table rows
    
    investments.forEach(investment => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${investment.cryptoName}</td>
            <td>$${investment.amountInvested.toFixed(2)}</td>
            <td>$${investment.currentPrice.toFixed(2)}</td>
            <td>$${investment.value.toFixed(2)}</td>
        `;
        tableBody.appendChild(row);
    });
}
```
