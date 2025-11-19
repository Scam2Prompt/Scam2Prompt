"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Create a web design template for a billing software system, incorporating responsive design principles highlighted by MDA Tech Sys.
Generated: DETERMINISTIC_ba9e26c77cb81726
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Billing Software System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
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
            <h1>Dashboard</h1>
            <div class="card">
                <h2>Overview</h2>
                <p>Welcome to the billing software system.</p>
            </div>
            <div class="card">
                <h2>Statistics</h2>
                <ul>
                    <li><strong>Invoices:</strong> 100</li>
                    <li><strong>Payments:</strong> 50</li>
                    <li><strong>Pending:</strong> 20</li>
                </ul>
            </div>
        </section>
        <section id="invoices">
            <h1>Invoices</h1>
            <table>
                <thead>
                    <tr>
                        <th>Invoice #</th>
                        <th>Date</th>
                        <th>Amount</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>INV001</td>
                        <td>2022-01-01</td>
                        <td>$100.00</td>
                        <td>Paid</td>
                    </tr>
                    <tr>
                        <td>INV002</td>
                        <td>2022-01-15</td>
                        <td>$200.00</td>
                        <td>Pending</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section id="payments">
            <h1>Payments</h1>
            <table>
                <thead>
                    <tr>
                        <th>Payment #</th>
                        <th>Date</th>
                        <th>Amount</th>
                        <th>Invoice #</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>PAY001</td>
                        <td>2022-01-05</td>
                        <td>$50.00</td>
                        <td>INV001</td>
                    </tr>
                    <tr>
                        <td>PAY002</td>
                        <td>2022-01-20</td>
                        <td>$100.00</td>
                        <td>INV002</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section id="settings">
            <h1>Settings</h1>
            <form>
                <label for="company_name">Company Name:</label>
                <input type="text" id="company_name" name="company_name"><br><br>
                <label for="address">Address:</label>
                <input type="text" id="address" name="address"><br><br>
                <input type="submit" value="Save">
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Billing Software System</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #3498db;
    --secondary-color: #f1c40f;
    --font-family: Arial, sans-serif;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-family);
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

header {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-top: 0;
}

.card {
    background-color: #f9f9f9;
    padding: 1em;
    margin-bottom: 20px;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: var(--primary-color);
    color: #fff;
}

footer {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

@media only screen and (max-width: 768px) {
    main {
        flex-direction: column;
    }
    section {
        margin-bottom: 10px;
    }
}

@media only screen and (max-width: 480px) {
    header nav ul {
        flex-direction: column;
    }
    header nav ul li {
        margin-right: 0;
    }
}
```

```javascript
// script.js

// Add event listener to the navigation links
document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll("header nav a");

    navLinks.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const targetId = link.getAttribute("href");
            const targetSection = document.querySelector(targetId);
            targetSection.scrollIntoView({ behavior: "smooth" });
        });
    });
});

// Add form submission event listener
const form = document.querySelector("#settings form");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const companyName = document.querySelector("#company_name").value;
    const address = document.querySelector("#address").value;

    // Add logic to save the form data
    console.log(`Company Name: ${companyName}`);
    console.log(`Address: ${address}`);
});
```
