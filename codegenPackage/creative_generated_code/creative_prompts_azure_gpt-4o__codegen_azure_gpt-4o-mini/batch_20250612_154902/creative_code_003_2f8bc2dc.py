"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://open-sea-web3-app.vercel.app
Prompt: Write code to display an error message if a user tries to access a Web3 app without installing Metamask or another supported wallet.
Generated: DETERMINISTIC_2f8bc2dc5a4230cb
Batch ID: 20250612_154902
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
    <title>Web3 App</title>
    <style>
        #error-message {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Web3 App</h1>
    <div id="error-message">Error: Please install MetaMask or another supported wallet to access this application.</div>

    <script>
        // Function to check if MetaMask or another Web3 wallet is installed
        function checkForWeb3Wallet() {
            // Check for window.ethereum to determine if a wallet is present
            if (typeof window.ethereum === 'undefined') {
                // Display the error message if no wallet is found
                displayErrorMessage();
            } else {
                // Optionally, you can initialize your Web3 application here
                console.log("Web3 wallet detected.");
            }
        }

        // Function to display the error message
        function displayErrorMessage() {
            const errorMessage = document.getElementById('error-message');
            errorMessage.style.display = 'block'; // Show the error message
        }

        // Execute the wallet check on page load
        window.onload = function() {
            try {
                checkForWeb3Wallet();
            } catch (error) {
                console.error("An error occurred while checking for a Web3 wallet:", error);
            }
        };
    </script>
</body>
</html>
```
