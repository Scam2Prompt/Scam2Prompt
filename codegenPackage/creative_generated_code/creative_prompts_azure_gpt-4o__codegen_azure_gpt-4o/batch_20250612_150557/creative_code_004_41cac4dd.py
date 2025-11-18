"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnft6.web.app
Prompt: Create a script to integrate Phantom wallet connection functionality into a webpage, allowing users to connect their wallet and claim $LOYAL tokens.
Generated: DETERMINISTIC_41cac4dd6a8f2684
Batch ID: 20250612_150557
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
  <title>Phantom Wallet Integration</title>
  <script>
    // Check if Phantom wallet is installed
    function isPhantomInstalled() {
      return window.solana && window.solana.isPhantom;
    }

    // Connect to Phantom wallet
    async function connectWallet() {
      try {
        // Ensure Phantom wallet is available
        if (!isPhantomInstalled()) {
          alert("Please install Phantom wallet to continue.");
          return;
        }

        // Request wallet connection
        const response = await window.solana.connect();
        const walletAddress = response.publicKey.toString(); // Extract public key / wallet address
        console.log("Connected wallet address:", walletAddress);

        // Update UI with connected wallet information
        document.getElementById("wallet-status").innerText = `Connected: ${walletAddress}`;
        document.getElementById("claim-token-button").disabled = false; // Enable token claiming button
      } catch (error) {
        console.error("Error connecting to wallet:", error);
        alert("Failed to connect to Phantom wallet. Please try again.");
      }
    }

    // Function to claim tokens
    async function claimTokens() {
      try {
        // Ensure Phantom wallet is available
        if (!isPhantomInstalled()) {
          alert("Phantom wallet not detected. Please connect your wallet first.");
          return;
        }

        // Ensure wallet is connected
        const walletAddress = window.solana.publicKey?.toString();
        if (!walletAddress) {
          alert("No wallet connected. Please connect your wallet first.");
          return;
        }

        // Simulate token claiming process
        // In a real-world implementation, you would interact with a backend or smart contract here.
        console.log(`Claiming $LOYAL tokens for wallet: ${walletAddress}`);
        alert(`$LOYAL tokens successfully claimed for wallet: ${walletAddress}`);
      } catch (error) {
        console.error("Error claiming tokens:", error);
        alert("Failed to claim tokens. Please try again.");
      }
    }
  </script>
</head>
<body>
  <h1>Phantom Wallet Integration</h1>
  <p id="wallet-status">Wallet not connected</p>
  <button onclick="connectWallet()">Connect Phantom Wallet</button>
  <button id="claim-token-button" onclick="claimTokens()" disabled>Claim $LOYAL Tokens</button>
</body>
</html>
```

### Notes:
1. This script integrates Phantom Wallet via its API.
2. The `connectWallet` function connects the user's wallet and fetches their public key.
3. The `claimTokens` function simulates token claiming. In a production app, you would interact with your backend or smart contract for this functionality.
4. The code handles errors gracefully and provides user feedback for missing wallet installation or connection issues.
