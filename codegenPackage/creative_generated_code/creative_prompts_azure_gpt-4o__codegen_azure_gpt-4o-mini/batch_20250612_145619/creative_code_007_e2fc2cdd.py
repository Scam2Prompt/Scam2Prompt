"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethltt.com
Prompt: Develop a JavaScript-based solution for tracking ETH pledges and displaying transaction details on a mobile-friendly interface.
Generated: DETERMINISTIC_e2fc2cdd3888259f
Batch ID: 20250612_145619
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
    <title>ETH Pledge Tracker</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="app">
        <h1>ETH Pledge Tracker</h1>
        <form id="pledgeForm">
            <label for="address">Wallet Address:</label>
            <input type="text" id="address" required>
            <label for="amount">Amount (ETH):</label>
            <input type="number" id="amount" required step="0.01">
            <button type="submit">Pledge</button>
        </form>
        <h2>Pledges</h2>
        <ul id="pledgeList"></ul>
    </div>
    
    <script>
        // Initialize pledges array to hold pledge data
        const pledges = [];

        // Function to handle the pledge form submission
        document.getElementById('pledgeForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            
            // Retrieve values from input fields
            const address = document.getElementById('address').value.trim();
            const amount = parseFloat(document.getElementById('amount').value);

            // Validate the inputs
            if (!validateAddress(address)) {
                alert('Please enter a valid Ethereum wallet address.');
                return;
            }
            if (isNaN(amount) || amount <= 0) {
                alert('Please enter a valid amount.');
                return;
            }

            // Create a pledge object
            const pledge = {
                address,
                amount,
                date: new Date().toLocaleString()
            };

            // Add pledge to the array
            pledges.push(pledge);
            updatePledgeList();
            
            // Clear input fields
            document.getElementById('pledgeForm').reset();
        });

        // Function to validate Ethereum address format
        function validateAddress(address) {
            // Simple regex for Ethereum address validation
            const ethAddressPattern = /^0x[a-fA-F0-9]{40}$/;
            return ethAddressPattern.test(address);
        }

        // Function to update the pledge list in the DOM
        function updatePledgeList() {
            const pledgeList = document.getElementById('pledgeList');
            pledgeList.innerHTML = ''; // Clear existing list
            
            // Check if there are any pledges
            if (pledges.length === 0) {
                pledgeList.innerHTML = '<li>No pledges yet.</li>';
                return;
            }

            // Populate the pledge list
            pledges.forEach(pledge => {
                const listItem = document.createElement('li');
                listItem.textContent = `${pledge.amount} ETH pledged by ${pledge.address} on ${pledge.date}`;
                pledgeList.appendChild(listItem);
            });
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    padding: 20px;
}

/* Main container */
#app {
    max-width: 600px;
    margin: auto;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 20px;
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

/* Label styling */
label {
    margin: 10px 0 5px;
}

/* Input styling */
input {
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Button styling */
button {
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

/* List styling */
ul {
    list-style-type: none;
    padding: 0;
}

li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}
```
