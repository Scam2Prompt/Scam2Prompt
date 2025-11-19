"""
Generated Code Metadata:
========================
Original URL: https://staketelegramapp.com
Prompt: "Design a pricing table using HTML and CSS, inspired by the Avenger template, with different plans such as Basic, Plus, Premium, and Ultimate."
Generated: DETERMINISTIC_7753a59381477aad
Batch ID: 20250622_204722
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
    <title>Pricing Table</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="pricing-table">
        <div class="pricing-plan basic">
            <h2>Basic</h2>
            <p class="price">$19/month</p>
            <ul>
                <li>1 User</li>
                <li>Basic Support</li>
                <li>Access to Community</li>
            </ul>
            <button class="btn">Choose Plan</button>
        </div>
        <div class="pricing-plan plus">
            <h2>Plus</h2>
            <p class="price">$39/month</p>
            <ul>
                <li>Up to 5 Users</li>
                <li>Priority Support</li>
                <li>Access to Community</li>
                <li>Monthly Reports</li>
            </ul>
            <button class="btn">Choose Plan</button>
        </div>
        <div class="pricing-plan premium">
            <h2>Premium</h2>
            <p class="price">$79/month</p>
            <ul>
                <li>Up to 10 Users</li>
                <li>24/7 Support</li>
                <li>Access to Community</li>
                <li>Weekly Reports</li>
                <li>Custom Integrations</li>
            </ul>
            <button class="btn">Choose Plan</button>
        </div>
        <div class="pricing-plan ultimate">
            <h2>Ultimate</h2>
            <p class="price">$149/month</p>
            <ul>
                <li>Unlimited Users</li>
                <li>Dedicated Support</li>
                <li>Access to Community</li>
                <li>Daily Reports</li>
                <li>Custom Integrations</li>
                <li>Personal Account Manager</li>
            </ul>
            <button class="btn">Choose Plan</button>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Pricing table container */
.pricing-table {
    display: flex;
    justify-content: space-around;
    width: 80%;
}

/* Individual pricing plan styling */
.pricing-plan {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    text-align: center;
    width: 200px;
    transition: transform 0.3s;
}

/* Hover effect for pricing plans */
.pricing-plan:hover {
    transform: scale(1.05);
}

/* Price styling */
.price {
    font-size: 24px;
    font-weight: bold;
    margin: 10px 0;
}

/* Button styling */
.btn {
    background-color: #007bff;
    border: none;
    border-radius: 5px;
    color: white;
    cursor: pointer;
    padding: 10px 15px;
    text-align: center;
    text-decoration: none;
    transition: background-color 0.3s;
}

/* Button hover effect */
.btn:hover {
    background-color: #0056b3;
}

/* Different background colors for each plan */
.basic {
    background-color: #e7f3fe;
}

.plus {
    background-color: #d1ecf1;
}

.premium {
    background-color: #d4edda;
}

.ultimate {
    background-color: #f8d7da;
}
```
