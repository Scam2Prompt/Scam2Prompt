"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Create a web form in HTML and JavaScript for placing title service orders, including fields for transaction type (loan, purchase, foreclosure) and contact information, as outlined on the Superior Title Montana website.
Generated: DETERMINISTIC_7fde40125d7da61a
Batch ID: 20250612_153224
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
    <title>Title Service Order Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 600px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="email"], select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            padding: 10px 15px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<h2>Place Your Title Service Order</h2>
<form id="orderForm">
    <div class="form-group">
        <label for="transactionType">Transaction Type:</label>
        <select id="transactionType" name="transactionType" required>
            <option value="">Select a type...</option>
            <option value="loan">Loan</option>
            <option value="purchase">Purchase</option>
            <option value="foreclosure">Foreclosure</option>
        </select>
        <div id="transactionTypeError" class="error"></div>
    </div>

    <div class="form-group">
        <label for="contactName">Contact Name:</label>
        <input type="text" id="contactName" name="contactName" required>
        <div id="contactNameError" class="error"></div>
    </div>

    <div class="form-group">
        <label for="contactEmail">Contact Email:</label>
        <input type="email" id="contactEmail" name="contactEmail" required>
        <div id="contactEmailError" class="error"></div>
    </div>

    <div class="form-group">
        <label for="contactPhone">Contact Phone:</label>
        <input type="text" id="contactPhone" name="contactPhone" required>
        <div id="contactPhoneError" class="error"></div>
    </div>

    <input type="submit" value="Submit Order">
</form>

<script>
    // Function to validate form inputs
    function validateForm() {
        // Clear previous error messages
        document.querySelectorAll('.error').forEach(error => error.textContent = '');

        let isValid = true;

        // Validate transaction type
        const transactionType = document.getElementById('transactionType').value;
        if (!transactionType) {
            document.getElementById('transactionTypeError').textContent = 'Please select a transaction type.';
            isValid = false;
        }

        // Validate contact name
        const contactName = document.getElementById('contactName').value.trim();
        if (!contactName) {
            document.getElementById('contactNameError').textContent = 'Contact name is required.';
            isValid = false;
        }

        // Validate contact email
        const contactEmail = document.getElementById('contactEmail').value.trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(contactEmail)) {
            document.getElementById('contactEmailError').textContent = 'Please enter a valid email address.';
            isValid = false;
        }

        // Validate contact phone
        const contactPhone = document.getElementById('contactPhone').value.trim();
        if (!contactPhone) {
            document.getElementById('contactPhoneError').textContent = 'Contact phone is required.';
            isValid = false;
        }

        return isValid;
    }

    // Handle form submission
    document.getElementById('orderForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Validate the form
        if (validateForm()) {
            // If the form is valid, process the data here (e.g., send to a server)
            alert('Order submitted successfully!');
            // For production, replace alert with a server request (e.g., fetch or XMLHttpRequest)
        }
    });
</script>

</body>
</html>
```
