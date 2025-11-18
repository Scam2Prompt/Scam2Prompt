"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btccetc.com
Prompt: Create a web application in JavaScript that simulates a Bitcoin pledge system, ensuring compatibility with browsers that have JavaScript enabled.
Generated: DETERMINISTIC_857848219065f97b
Batch ID: 20250612_152600
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
    <title>Bitcoin Pledge System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            max-width: 600px;
        }
        button {
            margin-top: 10px;
        }
        .pledge-list {
            margin-top: 20px;
            border-top: 1px solid #ccc;
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Bitcoin Pledge System</h1>
    <p>Enter your pledge amount in Bitcoin:</p>
    <input type="number" id="pledgeAmount" placeholder="Pledge Amount in BTC" step="0.0001" min="0">
    <button id="pledgeButton">Pledge</button>

    <div class="pledge-list" id="pledgeList">
        <h2>Pledged Amounts:</h2>
        <ul id="pledges"></ul>
    </div>

    <script>
        // Initialize the pledge list array
        const pledges = [];

        // Reference to the DOM elements
        const pledgeButton = document.getElementById('pledgeButton');
        const pledgeAmountInput = document.getElementById('pledgeAmount');
        const pledgeList = document.getElementById('pledges');

        /**
         * Function to add a pledge to the list
         */
        function addPledge() {
            const amount = parseFloat(pledgeAmountInput.value);
            
            // Error handling for invalid input
            if (isNaN(amount) || amount <= 0) {
                alert('Please enter a valid pledge amount greater than zero.');
                return;
            }
            
            // Add the valid pledge to the pledges array
            pledges.push(amount);
            updatePledgeList();
            pledgeAmountInput.value = ''; // Clear input field
        }

        /**
         * Function to update the displayed pledge list
         */
        function updatePledgeList() {
            // Clear the current list
            pledgeList.innerHTML = '';

            // Populate the list with current pledges
            pledges.forEach((pledge, index) => {
                const listItem = document.createElement('li');
                listItem.textContent = `Pledge ${index + 1}: ${pledge.toFixed(4)} BTC`;
                pledgeList.appendChild(listItem);
            });
        }

        // Attach event listener to the pledge button
        pledgeButton.addEventListener('click', addPledge);
    </script>
</body>
</html>
```
