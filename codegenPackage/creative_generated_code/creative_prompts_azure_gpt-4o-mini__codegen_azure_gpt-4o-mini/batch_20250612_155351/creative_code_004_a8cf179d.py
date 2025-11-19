"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abilityfordisabilityfund.com
Prompt: How can I create a web form to collect donations for the Ability for Disability Fund, ensuring it includes fields for donor information and donation amounts?
Generated: DETERMINISTIC_a8cf179d24541fcf
Batch ID: 20250612_155351
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
    <title>Ability for Disability Fund Donation</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Donate to the Ability for Disability Fund</h1>
    </header>
    
    <main>
        <form id="donationForm" action="/submit-donation" method="POST">
            <fieldset>
                <legend>Donor Information</legend>

                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required placeholder="John Doe">

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="john.doe@example.com">

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">
            </fieldset>

            <fieldset>
                <legend>Donation Amount</legend>
                
                <label for="amount">Amount ($):</label>
                <input type="number" id="amount" name="amount" min="1" required placeholder="Enter Amount">
            </fieldset>

            <fieldset>
                <legend>Payment Information</legend>

                <label for="cardNumber">Credit Card Number:</label>
                <input type="text" id="cardNumber" name="cardNumber" required placeholder="1234 5678 9012 3456">

                <label for="expiryDate">Expiry Date:</label>
                <input type="text" id="expiryDate" name="expiryDate" required placeholder="MM/YY">

                <label for="cvv">CVV:</label>
                <input type="text" id="cvv" name="cvv" required placeholder="123">
            </fieldset>

            <button type="submit">Submit Donation</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Ability for Disability Fund. All rights reserved.</p>
    </footer>

    <script>
        // Optional: Client-side validation and form submission handling
        document.getElementById('donationForm').addEventListener('submit', function(event) {
            // Perform additional client-side checks if necessary
            const amount = document.getElementById('amount').value;
            if (amount <= 0) {
                alert('Please enter a valid donation amount.');
                event.preventDefault(); // Stop form submission
            }
        });
    </script>
</body>
</html>
```

### CSS (styles.css)
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header, footer {
    text-align: center;
    margin-bottom: 20px;
}

form {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

fieldset {
    margin-bottom: 20px;
    border: 1px solid #ccc;
    padding: 10px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"], input[type="email"], input[type="tel"], input[type="number"] {
    width: calc(100% - 20px);
    padding: 10px;
    margin-bottom: 10px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}
```
