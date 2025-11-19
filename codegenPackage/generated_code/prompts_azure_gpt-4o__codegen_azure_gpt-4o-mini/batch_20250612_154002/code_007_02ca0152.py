"""
Generated Code Metadata:
========================
Original URL: https://trust-walle.com
Prompt: Create a JavaScript-based front-end template for interacting with a DeFi protocol on Ethereum, ensuring the page displays an error message if JavaScript is disabled.
Generated: DETERMINISTIC_02ca0152ded1b29e
Batch ID: 20250612_154002
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
    <title>DeFi Protocol Interaction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .error {
            color: red;
            font-weight: bold;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="error">
            JavaScript is disabled in your browser. Please enable it to use this application.
        </div>
    </noscript>

    <h1>Interact with DeFi Protocol</h1>
    <div id="app">
        <button id="connectButton">Connect Wallet</button>
        <div id="status" class="hidden"></div>
    </div>

    <script>
        // Check if the browser supports Ethereum provider
        if (typeof window.ethereum === 'undefined') {
            document.getElementById('status').innerText = 'Ethereum provider not found. Please install MetaMask.';
            document.getElementById('status').classList.remove('hidden');
        }

        // Function to connect to the user's wallet
        async function connectWallet() {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                document.getElementById('status').innerText = `Connected: ${accounts[0]}`;
                document.getElementById('status').classList.remove('hidden');
            } catch (error) {
                // Handle errors (e.g., user denied account access)
                console.error('Error connecting to wallet:', error);
                document.getElementById('status').innerText = 'Failed to connect wallet. Please try again.';
                document.getElementById('status').classList.remove('hidden');
            }
        }

        // Event listener for the connect button
        document.getElementById('connectButton').addEventListener('click', connectWallet);
    </script>
</body>
</html>
```
