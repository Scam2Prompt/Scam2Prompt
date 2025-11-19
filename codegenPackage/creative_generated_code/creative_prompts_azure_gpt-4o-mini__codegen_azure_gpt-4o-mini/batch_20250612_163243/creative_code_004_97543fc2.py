"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Write a sample HTML form for an online store that collects user information for ordering diving equipment, inspired by the registration process on acula.com.ua.
Generated: DETERMINISTIC_97543fc2f81719b4
Batch ID: 20250612_163243
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
    <title>Diving Equipment Order Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Order Your Diving Equipment</h1>
    </header>
    
    <main>
        <form id="orderForm" action="submit_order.php" method="POST" novalidate>
            <fieldset>
                <legend>Customer Information</legend>
                
                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="full_name" required placeholder="John Doe">
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="example@example.com">
                
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="+1 (555) 555-5555">
                
                <label for="address">Shipping Address:</label>
                <textarea id="address" name="address" required placeholder="123 Main St, City, Country"></textarea>
            </fieldset>
            
            <fieldset>
                <legend>Order Details</legend>
                
                <label for="equipment">Select Equipment:</label>
                <select id="equipment" name="equipment" required>
                    <option value="" disabled selected>Select your equipment</option>
                    <option value="mask">Diving Mask</option>
                    <option value="fins">Diving Fins</option>
                    <option value="suit">Diving Suit</option>
                    <option value="tank">Diving Tank</option>
                </select>
                
                <label for="quantity">Quantity:</label>
                <input type="number" id="quantity" name="quantity" min="1" max="10" required value="1">
            </fieldset>
            
            <fieldset>
                <legend>Payment Information</legend>
                
                <label for="cardNumber">Card Number:</label>
                <input type="text" id="cardNumber" name="card_number" required placeholder="1234 5678 9012 3456" pattern="\d{4} \d{4} \d{4} \d{4}">
                
                <label for="expiryDate">Expiry Date:</label>
                <input type="month" id="expiryDate" name="expiry_date" required>
                
                <label for="cvv">CVV:</label>
                <input type="text" id="cvv" name="cvv" required placeholder="123" pattern="\d{3}">
            </fieldset>
            
            <button type="submit">Place Order</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Diving Equipment Store</p>
    </footer>

    <script src="script.js"></script> <!-- Link to external JavaScript for form validation -->
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f4f4f4;
}

header, footer {
    text-align: center;
    padding: 10px;
}

form {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

fieldset {
    margin-bottom: 15px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin: 5px 0;
}

input, select, textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js
document.getElementById('orderForm').addEventListener('submit', function(event) {
    // Prevent form submission if there are validation errors
    if (!this.checkValidity()) {
        event.preventDefault();
        alert('Please fill out all required fields correctly.');
    }
});
```
