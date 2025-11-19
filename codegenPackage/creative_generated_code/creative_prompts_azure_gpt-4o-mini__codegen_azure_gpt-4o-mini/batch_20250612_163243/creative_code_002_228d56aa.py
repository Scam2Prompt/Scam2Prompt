"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-mocafoundation.pages.dev
Prompt: Create a simple HTML form that allows users to enter their details to check eligibility for the $MOCA airdrop as described on the Moca Foundation page.
Generated: DETERMINISTIC_228d56aa3dbe2c7c
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
    <title>MOCA Airdrop Eligibility Check</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Check Your Eligibility for the MOCA Airdrop</h1>
        <form id="eligibilityForm" onsubmit="return checkEligibility(event)">
            <!-- User Name Input -->
            <label for="username">User Name:</label>
            <input type="text" id="username" name="username" required placeholder="Enter your username">

            <!-- Wallet Address Input -->
            <label for="wallet">Wallet Address:</label>
            <input type="text" id="wallet" name="wallet" required placeholder="Enter your wallet address">

            <!-- Submit Button -->
            <button type="submit">Check Eligibility</button>
        </form>
        
        <div id="result" class="result"></div> <!-- Container for displaying results -->
    </div>

    <script>
        /**
         * Function to check eligibility for the MOCA airdrop.
         * @param {Event} event - The form submission event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function checkEligibility(event) {
            event.preventDefault(); // Prevent the default form submission

            // Retrieve form data
            const username = document.getElementById('username').value;
            const wallet = document.getElementById('wallet').value;

            // Basic validation (more checks can be added as needed)
            if (!isValidWallet(wallet)) {
                displayResult('Invalid wallet address format.', 'error');
                return false;
            }

            // Simulated eligibility check (replace with actual API call)
            const isEligible = simulateEligibilityCheck(username, wallet);

            // Display result to user
            if (isEligible) {
                displayResult('Congratulations! You are eligible for the MOCA airdrop.', 'success');
            } else {
                displayResult('Sorry, you are not eligible for the MOCA airdrop.', 'error');
            }

            return false; // Prevent default form submission
        }

        /**
         * Function to validate wallet address format (basic regex example).
         * @param {string} wallet - The wallet address to validate.
         * @returns {boolean} - Returns true if valid, otherwise false.
         */
        function isValidWallet(wallet) {
            const walletRegex = /^0x[a-fA-F0-9]{40}$/; // Basic Ethereum wallet format
            return walletRegex.test(wallet);
        }

        /**
         * Simulated eligibility check based on username and wallet.
         * @param {string} username - The user name.
         * @param {string} wallet - The wallet address.
         * @returns {boolean} - Returns true/false based on eligibility.
         */
        function simulateEligibilityCheck(username, wallet) {
            // Example logic: in real-case, this would be an API call
            // Here we just return true for demonstration purposes
            return username.length > 0 && wallet.length === 42;
        }

        /**
         * Function to display results on the page.
         * @param {string} message - The message to display.
         * @param {string} type - The type of message ('success' or 'error').
         */
        function displayResult(message, type) {
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = message;
            resultDiv.className = type; // Add class for styling (e.g., .success or .error)
        }
    </script>

    <style>
        /* Basic styles for the form and results */
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px; }
        .container { max-width: 400px; margin: auto; background: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        h1 { text-align: center; }
        label { display: block; margin: 10px 0 5px; }
        input { width: 100%; padding: 8px; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 5px; }
        button { width: 100%; padding: 10px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #218838; }
        .result { margin-top: 15px; text-align: center; font-weight: bold; }
        .success { color: green; }
        .error { color: red; }
    </style>
</body>
</html>
```
