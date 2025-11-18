"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonus-gasspas.com
Prompt: Generate code to display bonus allocation updates for GASS token holders on a webpage after connecting a wallet.
Generated: DETERMINISTIC_93d4bb0f12c78dee
Batch ID: 20250612_145114
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/@ethersproject/wallet/dist/ethers.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@ethersproject/providers/dist/ethers.min.js": {
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
  <title>GASS Token Bonus Allocation</title>
  <script src="https://cdn.jsdelivr.net/npm/@ethersproject/providers/dist/ethers.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@ethersproject/wallet/dist/ethers.min.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }
    #bonus-info {
      margin-top: 20px;
      padding: 10px;
      border: 1px solid #ddd;
      background-color: #fff;
    }
    .error {
      color: red;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>GASS Token Bonus Allocation</h1>
    <button id="connectWalletButton">Connect Wallet</button>
    <div id="bonus-info"></div>
  </div>

  <script>
    // Constants
    const GASS_TOKEN_CONTRACT_ADDRESS = '0xYourContractAddressHere'; // Replace with actual contract address
    const GASS_TOKEN_ABI = [
      // Replace with actual contract ABI
      {
        "constant": true,
        "inputs": [{"name": "_wallet", "type": "address"}],
        "name": "getBonusAllocation",
        "outputs": [{"name": "bonusAmount", "type": "uint256"}],
        "type": "function"
      }
    ];

    // Elements
    const connectWalletButton = document.getElementById('connectWalletButton');
    const bonusInfoElement = document.getElementById('bonus-info');

    // Variables
    let provider;
    let signer;

    /**
     * Connects user's wallet using MetaMask and displays bonus allocation.
     */
    async function connectWallet() {
      try {
        // Check if MetaMask is available
        if (!window.ethereum) {
          throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
        }

        // Request wallet connection
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const walletAddress = accounts[0];
        bonusInfoElement.textContent = `Wallet connected: ${walletAddress}`;

        // Set up ethers.js provider and signer
        provider = new ethers.providers.Web3Provider(window.ethereum);
        signer = provider.getSigner();

        // Fetch and display bonus allocation
        await fetchBonusAllocation(walletAddress);
      } catch (error) {
        displayError(error.message || 'An error occurred while connecting the wallet.');
      }
    }

    /**
     * Fetches and displays bonus allocation for the connected wallet.
     * @param {string} walletAddress - The wallet address of the user.
     */
    async function fetchBonusAllocation(walletAddress) {
      try {
        const contract = new ethers.Contract(GASS_TOKEN_CONTRACT_ADDRESS, GASS_TOKEN_ABI, provider);
        const bonusAmount = await contract.getBonusAllocation(walletAddress);

        // Display bonus allocation
        bonusInfoElement.innerHTML = `
          <p>Your bonus allocation:</p>
          <p><strong>${ethers.utils.formatEther(bonusAmount)} GASS</strong></p>
        `;
      } catch (error) {
        displayError(error.message || 'An error occurred while fetching bonus allocation.');
      }
    }

    /**
     * Displays an error message on the webpage.
     * @param {string} errorMessage - The error message to display.
     */
    function displayError(errorMessage) {
      bonusInfoElement.innerHTML = `<p class="error">${errorMessage}</p>`;
    }

    // Event listener for the "Connect Wallet" button
    connectWalletButton.addEventListener('click', connectWallet);
  </script>
</body>
</html>
```
