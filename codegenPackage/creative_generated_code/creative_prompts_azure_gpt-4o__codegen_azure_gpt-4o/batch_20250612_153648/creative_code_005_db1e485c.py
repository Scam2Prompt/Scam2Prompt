"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Develop a front-end interface for an NFT minting platform that includes wallet selection and whitelist integration, similar to the Immortals NFT minting page.
Generated: DETERMINISTIC_db1e485cc3c2f52e
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js": {
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
  <title>NFT Minting Platform</title>
  <link rel="stylesheet" href="styles.css">
  <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script>
</head>

<body>
  <div class="minting-container">
    <h1>Immortals NFT Minting</h1>

    <!-- Wallet Selection Section -->
    <div id="wallet-selection">
      <button id="connect-wallet-btn">Connect Wallet</button>
      <p id="wallet-status" class="status">Wallet not connected.</p>
    </div>

    <!-- Whitelist and Minting Section -->
    <div id="minting-section">
      <form id="minting-form">
        <label for="wallet-address">Wallet Address:</label>
        <input type="text" id="wallet-address" readonly />

        <label for="whitelist-code">Whitelist Code:</label>
        <input type="text" id="whitelist-code" placeholder="Enter whitelist code" />

        <label for="quantity">Number of NFTs to Mint:</label>
        <input type="number" id="quantity" min="1" max="10" value="1" />

        <button type="submit" id="mint-btn">Mint NFT</button>
      </form>
      <p id="mint-status" class="status"></p>
    </div>
  </div>

  <script>
    // Check if Web3 is injected (e.g., via MetaMask)
    let web3 = null;
    let userWallet = null;

    document.getElementById("connect-wallet-btn").addEventListener("click", async () => {
      try {
        if (window.ethereum) {
          web3 = new Web3(window.ethereum);

          // Request wallet connection
          const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
          userWallet = accounts[0];
          document.getElementById("wallet-address").value = userWallet;
          document.getElementById("wallet-status").textContent = `Connected wallet: ${userWallet}`;
        } else {
          alert("MetaMask or other Ethereum wallet not detected. Please install one.");
        }
      } catch (error) {
        console.error("Error connecting wallet:", error);
        alert("Failed to connect wallet. Please try again.");
      }
    });

    document.getElementById("minting-form").addEventListener("submit", async (event) => {
      event.preventDefault();

      const whitelistCode = document.getElementById("whitelist-code").value;
      const quantity = parseInt(document.getElementById("quantity").value);

      if (!userWallet) {
        alert("Please connect your wallet first.");
        return;
      }

      if (!whitelistCode) {
        alert("Please enter a valid whitelist code.");
        return;
      }

      if (quantity < 1 || quantity > 10) {
        alert("Please enter a minting quantity between 1 and 10.");
        return;
      }

      try {
        // Here you would interact with your smart contract
        // For example:
        // const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);
        // const mintResult = await contract.methods.mint(quantity, whitelistCode).send({ from: userWallet });

        // Simulating contract interaction
        document.getElementById("mint-status").textContent = `Minting ${quantity} NFT(s)...`;
        setTimeout(() => {
          document.getElementById("mint-status").textContent = `Successfully minted ${quantity} NFT(s)!`;
        }, 2000);
      } catch (error) {
        console.error("Minting failed:", error);
        document.getElementById("mint-status").textContent = "Minting failed. Please try again.";
      }
    });
  </script>
</body>

</html>
```

```css
/* styles.css */

body {
  font-family: Arial, sans-serif;
  background-color: #121212;
  color: #ffffff;
  margin: 0;
  padding: 0;
}

.minting-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: #1d1d1d;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
}

h1 {
  text-align: center;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #444;
  border-radius: 4px;
  background-color: #222;
  color: #fff;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bfc;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #005bb5;
}

.status {
  margin-top: 10px;
  font-size: 0.9em;
  color: #00ff00;
}

.status.error {
  color: #ff0000;
}
```

This code provides a clean and well-commented front-end setup for an NFT minting page, complete with wallet integration and whitelist functionality. It includes error handling and client-side validations. You'll need to add your smart contract's ABI and address in the JavaScript if you want to enable actual minting functionality.
