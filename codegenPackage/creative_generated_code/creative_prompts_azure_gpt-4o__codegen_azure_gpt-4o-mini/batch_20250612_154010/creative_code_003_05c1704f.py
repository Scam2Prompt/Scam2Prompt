"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepapp-claim.pages.dev
Prompt: Create a script that checks the wallet connection status and displays it dynamically on a webpage, similar to the functionality described on the STEP APP claim page.
Generated: DETERMINISTIC_05c1704ffb60ee98
Batch ID: 20250612_154010
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
    <title>Wallet Connection Status</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f5f5f5;
        }
        #wallet-status {
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            text-align: center;
        }
        .connected {
            color: green;
        }
        .disconnected {
            color: red;
        }
    </style>
</head>
<body>
    <div id="wallet-status" class="disconnected">
        Wallet Status: Disconnected
    </div>

    <script>
        // Function to check the wallet connection status
        async function checkWalletConnection() {
            try {
                // Checking if the wallet is available
                if (window.ethereum) {
                    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                    
                    // Update the wallet status based on account availability
                    if (accounts.length > 0) {
                        updateWalletStatus(true);
                    } else {
                        updateWalletStatus(false);
                    }
                } else {
                    // Notify user that no Ethereum wallet is detected
                    updateWalletStatus(false, "No Ethereum wallet found.");
                }
            } catch (error) {
                console.error("Error checking wallet connection:", error);
                updateWalletStatus(false, "Error checking wallet connection.");
            }
        }

        // Function to update the wallet status on the webpage
        function updateWalletStatus(isConnected, message = "") {
            const walletStatusDiv = document.getElementById('wallet-status');
            if (isConnected) {
                walletStatusDiv.textContent = "Wallet Status: Connected";
                walletStatusDiv.className = "connected";
            } else {
                walletStatusDiv.textContent = "Wallet Status: Disconnected" + (message ? " - " + message : "");
                walletStatusDiv.className = "disconnected";
            }
        }

        // Check wallet connection on page load
        window.onload = checkWalletConnection;

        // Optional: Listen for account changes
        if (window.ethereum) {
            window.ethereum.on('accountsChanged', (accounts) => {
                updateWalletStatus(accounts.length > 0);
            });
        }
    </script>
</body>
</html>
```
