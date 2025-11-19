"""
Generated Code Metadata:
========================
Original URL: https://develop--celadon-praline-71fe9f.netlify.app
Prompt: Create a demo application for Aarc Deposit Widget that requires JavaScript to run.
Generated: DETERMINISTIC_2fae8262f5089802
Batch ID: 20250622_210946
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
    <title>Aarc Deposit Widget Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        #depositForm {
            display: flex;
            flex-direction: column;
            max-width: 400px;
        }
        input[type="text"], input[type="number"] {
            margin-bottom: 10px;
            padding: 10px;
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
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <h1>Aarc Deposit Widget</h1>
    <form id="depositForm">
        <label for="accountNumber">Account Number:</label>
        <input type="text" id="accountNumber" required>

        <label for="amount">Deposit Amount:</label>
        <input type="number" id="amount" required min="1">

        <button type="submit">Deposit</button>
        <div class="error" id="errorMessage"></div>
    </form>

    <script>
        // Function to handle form submission
        document.getElementById('depositForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Clear previous error messages
            const errorMessage = document.getElementById('errorMessage');
            errorMessage.textContent = '';

            // Get form values
            const accountNumber = document.getElementById('accountNumber').value.trim();
            const amount = parseFloat(document.getElementById('amount').value);

            // Validate input
            if (!accountNumber || isNaN(amount) || amount <= 0) {
                errorMessage.textContent = 'Please enter valid account number and deposit amount.';
                return;
            }

            // Simulate deposit process
            try {
                deposit(accountNumber, amount);
                alert(`Successfully deposited $${amount} to account ${accountNumber}.`);
            } catch (error) {
                errorMessage.textContent = `Error: ${error.message}`;
            }
        });

        // Simulated deposit function
        function deposit(accountNumber, amount) {
            // Simulate a potential error during the deposit process
            if (accountNumber.length < 5) {
                throw new Error('Account number must be at least 5 characters long.');
            }
            // Here you would typically make an API call to process the deposit
            console.log(`Depositing $${amount} to account ${accountNumber}`);
        }
    </script>

</body>
</html>
```
