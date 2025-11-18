"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herocoineth.com
Prompt: Generate code to implement a feature in MetaMask that allows users to spend crypto for daily purchases using the Card functionality.
Generated: DETERMINISTIC_5e5cf8b9bca48f14
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and dependencies
import { ethers } from 'ethers';

// Constants for MetaMask integration
const CARD_CONTRACT_ADDRESS = '<CardContractAddress>'; // Replace with the actual Card smart contract address
const CARD_ABI = [
  // Include the ABI for the Card smart contract
  {
    "constant": true,
    "inputs": [],
    "name": "spendCrypto",
    "outputs": [{ "name": "success", "type": "bool" }],
    "type": "function",
  },
  // Other required contract methods...
];

// Function to connect to MetaMask and spend crypto
async function spendCryptoWithCard(amount, recipient) {
  try {
    // Ensure MetaMask is installed
    if (!window.ethereum) {
      throw new Error("MetaMask is not detected. Please install MetaMask to proceed.");
    }

    // Request user to connect MetaMask
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (current connected account)
    const signer = provider.getSigner();

    // Instantiate the Card contract
    const cardContract = new ethers.Contract(CARD_CONTRACT_ADDRESS, CARD_ABI, signer);

    // Validate inputs
    if (!ethers.utils.isAddress(recipient)) {
      throw new Error("Recipient address is not valid.");
    }
    if (amount <= 0) {
      throw new Error("Amount must be greater than zero.");
    }

    // Spend crypto using the Card contract
    const tx = await cardContract.spendCrypto(ethers.utils.parseEther(amount.toString()), recipient);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();

    // Confirm transaction success
    if (receipt.status) {
      console.log("Transaction successful:", receipt);
      return receipt;
    } else {
      throw new Error("Transaction failed. Please try again.");
    }
  } catch (error) {
    console.error("Error spending crypto:", error.message);
    throw error; // Rethrow error for further handling
  }
}

// Example usage of the function
(async () => {
  try {
    const amount = 0.01; // Amount in ETH
    const recipient = "<RecipientAddress>"; // Replace with the recipient's address
    console.log("Attempting to spend crypto...");
    const receipt = await spendCryptoWithCard(amount, recipient);
    console.log("Transaction Receipt:", receipt);
  } catch (error) {
    console.error("Transaction failed:", error.message);
  }
})();
```

---

**Notes:**
1. Replace `<CardContractAddress>` and `<RecipientAddress>` with appropriate values.
2. Ensure the `CARD_ABI` matches the actual ABI of the deployed Card contract.
3. The `spendCrypto` method in the smart contract should accept required arguments (`amount`, `recipient`) and implement the logic for spending crypto. If the actual contract differs, adapt the code appropriately.
