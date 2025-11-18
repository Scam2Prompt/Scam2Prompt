"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethvni.com
Prompt: Write JavaScript code to create a Bitcoin pledge system that requires JavaScript to be enabled for proper functionality, as described on the ethvni.com website.
Generated: DETERMINISTIC_5a06cd2c8d9298be
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Bitcoin Pledge System

// Check if JavaScript is enabled
if (typeof window === 'undefined' || !window.document) {
    console.error("JavaScript is not enabled.");
    alert("Please enable JavaScript to use the Bitcoin Pledge System.");
}

// Function to create a pledge
const createPledge = async (amount, address) => {
    try {
        if (!isValidAmount(amount)) throw new Error("Invalid pledge amount.");
        if (!isValidAddress(address)) throw new Error("Invalid Bitcoin address.");

        // Simulate pledge creation
        const response = await fakeApiCall(amount, address);
        console.log("Pledge created successfully:", response);
    } catch (error) {
        console.error("Error creating pledge:", error.message);
        alert("Failed to create pledge: " + error.message);
    }
};

// Validate the pledge amount
const isValidAmount = (amount) => {
    return typeof amount === 'number' && amount > 0;
};

// Validate the Bitcoin address format (simple regex)
const isValidAddress = (address) => {
    const bitcoinAddressRegex = /^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/;
    return bitcoinAddressRegex.test(address);
};

// Simulated API call (replace with actual API logic)
const fakeApiCall = (amount, address) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ amount, address, status: "success" });
        }, 1000);
    });
};

// Function to handle pledge form submission
const handlePledgeFormSubmit = (event) => {
    event.preventDefault();
    const amountInput = document.getElementById('amount');
    const addressInput = document.getElementById('address');

    const amount = parseFloat(amountInput.value);
    const address = addressInput.value.trim();

    createPledge(amount, address);
};

// Document ready function
document.addEventListener("DOMContentLoaded", () => {
    const pledgeForm = document.getElementById('pledge-form');
    pledgeForm.addEventListener('submit', handlePledgeFormSubmit);
});
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
    <form id="pledge-form">
        <label for="amount">Pledge Amount (BTC):</label>
        <input type="number" id="amount" required>
        <label for="address">Bitcoin Address:</label>
        <input type="text" id="address" required>
        <button type="submit">Create Pledge</button>
    </form>
    <script src="pledge.js"></script>
</body>
</html>
```
