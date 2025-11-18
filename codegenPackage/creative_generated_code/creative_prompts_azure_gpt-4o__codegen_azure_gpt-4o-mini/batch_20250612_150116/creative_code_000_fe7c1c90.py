"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: Write JavaScript code to create a Bitcoin pledge system that validates user input and displays a confirmation message.
Generated: DETERMINISTIC_fe7c1c9055dff3d9
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Bitcoin Pledge System

// Function to validate user input
function validateInput(amount, address) {
    // Check if the amount is a valid number and greater than zero
    if (isNaN(amount) || amount <= 0) {
        throw new Error("Invalid amount. Please enter a positive number.");
    }

    // Regular expression to validate Bitcoin address format
    const bitcoinAddressRegex = /^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/;
    if (!bitcoinAddressRegex.test(address)) {
        throw new Error("Invalid Bitcoin address format. Please check and try again.");
    }
}

// Function to handle the pledge submission
function submitPledge(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get the values from the form inputs
    const amount = parseFloat(document.getElementById("amount").value);
    const address = document.getElementById("address").value;

    try {
        // Validate the user input
        validateInput(amount, address);

        // Display a confirmation message to the user
        const confirmationMessage = `Thank you for your pledge of ${amount} BTC to the address ${address}.`;
        document.getElementById("confirmation").innerText = confirmationMessage;
        document.getElementById("confirmation").style.color = "green"; // Set text color to green for success

    } catch (error) {
        // Handle validation errors and display them to the user
        document.getElementById("confirmation").innerText = error.message;
        document.getElementById("confirmation").style.color = "red"; // Set text color to red for errors
    }
}

// Adding event listener to the pledge form
document.getElementById("pledgeForm").addEventListener("submit", submitPledge);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bitcoin Pledge System</title>
</head>
<body>
    <h1>Bitcoin Pledge System</h1>
    <form id="pledgeForm">
        <label for="amount">Pledge Amount (BTC):</label>
        <input type="text" id="amount" required>
        <br>
        <label for="address">Bitcoin Address:</label>
        <input type="text" id="address" required>
        <br>
        <button type="submit">Submit Pledge</button>
    </form>
    <div id="confirmation"></div>

    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```
