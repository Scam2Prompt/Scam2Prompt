"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Generate code to create a web form for SGFC Finance's loan application process, including fields for personal details, loan type (personal, business, group), and repayment preferences.
Generated: DETERMINISTIC_04d98dc98b4309ec
Batch ID: 20250612_145228
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
    <title>SGFC Finance Loan Application</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>SGFC Finance Loan Application</h1>
    </header>
    <main>
        <form id="loanApplicationForm" action="/submit-loan-application" method="POST">
            <fieldset>
                <legend>Personal Details</legend>
                
                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">
                
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email address">
                
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">
                
                <label for="address">Home Address:</label>
                <textarea id="address" name="address" required placeholder="Enter your home address"></textarea>
            </fieldset>

            <fieldset>
                <legend>Loan Details</legend>
                
                <label for="loanType">Loan Type:</label>
                <select id="loanType" name="loanType" required>
                    <option value="" disabled selected>Select loan type</option>
                    <option value="personal">Personal</option>
                    <option value="business">Business</option>
                    <option value="group">Group</option>
                </select>
                
                <label for="amount">Loan Amount:</label>
                <input type="number" id="amount" name="amount" min="1000" max="100000" required placeholder="Enter loan amount">
                
                <label for="repaymentPeriod">Repayment Period (months):</label>
                <input type="number" id="repaymentPeriod" name="repaymentPeriod" min="6" max="60" required placeholder="Enter repayment period">
            </fieldset>

            <fieldset>
                <legend>Repayment Preferences</legend>
                
                <label for="paymentMethod">Preferred Payment Method:</label>
                <select id="paymentMethod" name="paymentMethod" required>
                    <option value="" disabled selected>Select payment method</option>
                    <option value="bankTransfer">Bank Transfer</option>
                    <option value="check">Check</option>
                    <option value="autoDebit">Auto Debit</option>
                </select>
                
                <label for="paymentFrequency">Payment Frequency:</label>
                <select id="paymentFrequency" name="paymentFrequency" required>
                    <option value="" disabled selected>Select frequency</option>
                    <option value="monthly">Monthly</option>
                    <option value="biweekly">Bi-weekly</option>
                    <option value="weekly">Weekly</option>
                </select>
            </fieldset>

            <button type="submit">Submit Application</button>
        </form>
    </main>
    
    <footer>
        <p>&copy; 2023 SGFC Finance. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('loanApplicationForm').onsubmit = function(event) {
            // Implement custom validation or actions before submitting if necessary
            // Example: Show a confirmation dialog
            const confirmation = confirm("Do you want to submit the application?");
            if (!confirmation) {
                event.preventDefault(); // Prevent form submission if user cancels
            }
        };
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the loan application form */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f8f9fa;
}

header, footer {
    text-align: center;
    margin-bottom: 20px;
}

h1 {
    color: #007bff;
}

fieldset {
    border: 1px solid #007bff;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 15px;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ced4da;
    border-radius: 5px;
}

button {
    background-color: #007bff;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```
