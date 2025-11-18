"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Create a web design template for a billing software system, incorporating responsive design principles highlighted by MDA Tech Sys.
Generated: DETERMINISTIC_ba9e26c77cb81726
Batch ID: 20250612_152045
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
    <title>Billing Software System</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Billing Software System</h1>
        <nav>
            <ul>
                <li><a href="#dashboard">Dashboard</a></li>
                <li><a href="#invoices">Invoices</a></li>
                <li><a href="#payments">Payments</a></li>
                <li><a href="#settings">Settings</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="dashboard">
            <h2>Dashboard</h2>
            <div class="card">
                <h3>Total Invoices</h3>
                <p>$5,000</p>
            </div>
            <div class="card">
                <h3>Total Payments</h3>
                <p>$4,500</p>
            </div>
            <div class="card">
                <h3>Outstanding Balance</h3>
                <p>$500</p>
            </div>
        </section>

        <section id="invoices">
            <h2>Invoices</h2>
            <table>
                <thead>
                    <tr>
                        <th>Invoice Number</th>
                        <th>Date</th>
                        <th>Amount</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>#001</td>
                        <td>01/10/2023</td>
                        <td>$1,000</td>
                        <td>Paid</td>
                    </tr>
                    <tr>
                        <td>#002</td>
                        <td>01/11/2023</td>
                        <td>$1,500</td>
                        <td>Unpaid</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section id="payments">
            <h2>Payments</h2>
            <form id="payment-form">
                <label for="invoice-number">Invoice Number:</label>
                <input type="text" id="invoice-number" name="invoice-number" required>
                
                <label for="amount">Amount:</label>
                <input type="number" id="amount" name="amount" required>
                
                <button type="submit">Submit Payment</button>
            </form>
            <div id="payment-message"></div>
        </section>

        <section id="settings">
            <h2>Settings</h2>
            <form id="settings-form">
                <label for="company-name">Company Name:</label>
                <input type="text" id="company-name" name="company-name" required>
                
                <label for="currency">Currency:</label>
                <select id="currency" name="currency">
                    <option value="USD">USD</option>
                    <option value="EUR">EUR</option>
                    <option value="GBP">GBP</option>
                </select>
                
                <button type="submit">Save Settings</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 MDA Tech Sys. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Base styles for the body */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

/* Header styles */
header {
    background: #007bff;
    color: #fff;
    padding: 1rem 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Card styles */
.card {
    background: #f8f9fa;
    padding: 15px;
    margin: 10px 0;
    border-radius: 5px;
}

/* Table styles */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background: #007bff;
    color: #fff;
}

/* Responsive design */
@media (max-width: 768px) {
    nav ul li {
        display: block;
        margin: 10px 0;
    }
}
```

```javascript
// script.js

document.addEventListener('DOMContentLoaded', () => {
    // Handle payment form submission
    const paymentForm = document.getElementById('payment-form');
    paymentForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const invoiceNumber = document.getElementById('invoice-number').value;
        const amount = document.getElementById('amount').value;
        const paymentMessage = document.getElementById('payment-message');

        try {
            // Simple validation
            if (!invoiceNumber || !amount) {
                throw new Error("Both fields are required.");
            }
            
            // Simulate payment processing (replace with actual API call)
            await fakePaymentProcessing(invoiceNumber, amount);

            // Display success message
            paymentMessage.textContent = `Payment of $${amount} for Invoice #${invoiceNumber} was successful.`;
            paymentMessage.style.color = 'green';
        } catch (error) {
            // Display error message
            paymentMessage.textContent = `Error: ${error.message}`;
            paymentMessage.style.color = 'red';
        }
    });
});

// Simulated payment processing function
async function fakePaymentProcessing(invoiceNumber, amount) {
    return new Promise((resolve) => {
        setTimeout(resolve, 1000); // Simulate network delay
    });
}
```
