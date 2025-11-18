"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimprize-130.web.app
Prompt: Generate code to display a "Connect Wallet" button for Phantom, Solflare, and Slope wallets, and enable claiming DUST tokens upon connection.
Generated: DETERMINISTIC_7816b0700d694cef
Batch ID: 20250612_153702
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/solana-web3.js/1.31.0/solana-web3.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-backend-api/claim-dust": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connect Wallet</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/solana-web3.js/1.31.0/solana-web3.min.js"></script>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f3f4f6;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #4caf50;
            color: white;
        }
    </style>
</head>
<body>

<button id="connectButton">Connect Wallet</button>

<script>
    // Function to connect to a wallet and claim DUST tokens
    async function connectWallet() {
        try {
            // Check for Phantom, Solflare, or Slope wallets
            const provider = window.solana;

            if (!provider) {
                throw new Error("No wallet provider found. Please install Phantom, Solflare, or Slope wallet.");
            }

            // Connect to the wallet
            const response = await provider.connect();
            const publicKey = response.publicKey.toString();
            console.log("Connected to wallet:", publicKey);

            // Call function to claim DUST tokens
            await claimDustTokens(publicKey);
        } catch (error) {
            console.error("Error connecting to wallet:", error.message);
            alert("Failed to connect wallet: " + error.message);
        }
    }

    // Function to claim DUST tokens
    async function claimDustTokens(publicKey) {
        try {
            // Assuming a backend API is available for claiming DUST tokens
            const response = await fetch('https://your-backend-api/claim-dust', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ walletAddress: publicKey })
            });

            if (!response.ok) {
                throw new Error("Failed to claim DUST tokens. Status: " + response.status);
            }

            const result = await response.json();
            console.log("DUST tokens claimed successfully:", result);
            alert("DUST tokens claimed successfully!");
        } catch (error) {
            console.error("Error claiming DUST tokens:", error.message);
            alert("Failed to claim DUST tokens: " + error.message);
        }
    }

    // Add event listener to the button
    document.getElementById('connectButton').addEventListener('click', connectWallet);
</script>

</body>
</html>
```
