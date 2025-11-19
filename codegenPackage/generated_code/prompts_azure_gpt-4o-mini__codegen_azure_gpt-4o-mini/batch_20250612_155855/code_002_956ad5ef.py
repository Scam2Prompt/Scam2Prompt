"""
Generated Code Metadata:
========================
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: Generate a script that calculates the total number of keys bought and displays it on a web page for a presale event.
Generated: DETERMINISTIC_956ad5ef5f50a80f
Batch ID: 20250612_155855
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
    <title>Presale Event Key Counter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        #keyCounter {
            font-size: 24px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Presale Event Key Purchase Tracker</h1>
    <label for="keyInput">Enter number of keys bought:</label>
    <input type="number" id="keyInput" min="0" value="0">
    <button id="addKeyButton">Add Keys</button>
    <div id="keyCounter">Total Keys Bought: 0</div>

    <script>
        // Initialize total keys variable
        let totalKeys = 0;

        // Function to update the displayed total keys
        function updateKeyCounter() {
            const keyCounterElement = document.getElementById('keyCounter');
            keyCounterElement.textContent = `Total Keys Bought: ${totalKeys}`;
        }

        // Function to handle adding keys
        function addKeys() {
            const keyInputElement = document.getElementById('keyInput');
            const keysToAdd = parseInt(keyInputElement.value, 10);

            // Validate input
            if (isNaN(keysToAdd) || keysToAdd < 0) {
                alert('Please enter a valid number of keys.');
                return;
            }

            // Update total keys
            totalKeys += keysToAdd;

            // Reset input field
            keyInputElement.value = 0;

            // Update the displayed total
            updateKeyCounter();
        }

        // Attach event listener to the button
        document.getElementById('addKeyButton').addEventListener('click', addKeys);
    </script>
</body>
</html>
```
