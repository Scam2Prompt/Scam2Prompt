"""
Generated Code Metadata:
========================
Original URL: https://starknet-disperse.vercel.app
Prompt: Generate a code example using a library or framework that interacts with the Starknet disperse app, focusing on enabling JavaScript.
Generated: DETERMINISTIC_efe8ff6d166c822a
Batch ID: 20250622_212613
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://alpha-mainnet.starknet.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { Provider, Contract, Account } = require("starknet"); // Starknet.js library
const ethers = require("ethers"); // Ethers.js for handling Ethereum-like operations

// Configuration constants
const STARKNET_RPC_URL = "https://alpha-mainnet.starknet.io"; // Replace with the appropriate Starknet RPC URL
const PRIVATE_KEY = "your_private_key_here"; // Replace with your Starknet account private key
const DISPERSE_CONTRACT_ADDRESS = "0x123456789abcdef"; // Replace with the actual Disperse contract address

// Initialize Starknet provider
const provider = new Provider({ rpcUrl: STARKNET_RPC_URL });

// Initialize account using private key
const account = new Account(provider, PRIVATE_KEY);

// ABI for the Disperse contract (replace with the actual ABI of the contract)
const DISPERSE_CONTRACT_ABI = [
  {
    "type": "function",
    "name": "disperseTokens",
    "inputs": [
      { "name": "token", "type": "felt" },
      { "name": "recipients", "type": "felt[]" },
      { "name": "amounts", "type": "felt[]" }
    ],
    "outputs": []
  }
];

// Initialize contract instance
const disperseContract = new Contract(DISPERSE_CONTRACT_ABI, DISPERSE_CONTRACT_ADDRESS, provider);

// Function to disperse tokens
async function disperseTokens(tokenAddress, recipients, amounts) {
  try {
    // Validate inputs
    if (!ethers.utils.isAddress(tokenAddress)) {
      throw new Error("Invalid token address.");
    }
    if (!Array.isArray(recipients) || !Array.isArray(amounts)) {
      throw new Error("Recipients and amounts must be arrays.");
    }
    if (recipients.length !== amounts.length) {
      throw new Error("Recipients and amounts arrays must have the same length.");
    }

    // Convert inputs to Starknet-compatible format
    const starknetTokenAddress = ethers.BigNumber.from(tokenAddress).toHexString();
    const starknetRecipients = recipients.map((recipient) =>
      ethers.BigNumber.from(recipient).toHexString()
    );
    const starknetAmounts = amounts.map((amount) =>
      ethers.BigNumber.from(amount).toHexString()
    );

    // Call the disperseTokens function on the contract
    const tx = await account.execute({
      contractAddress: DISPERSE_CONTRACT_ADDRESS,
      entrypoint: "disperseTokens",
      calldata: [starknetTokenAddress, starknetRecipients, starknetAmounts],
    });

    console.log("Transaction submitted:", tx.transaction_hash);

    // Wait for transaction to be mined
    const receipt = await provider.waitForTransaction(tx.transaction_hash);
    console.log("Transaction mined:", receipt);
  } catch (error) {
    console.error("Error dispersing tokens:", error.message);
  }
}

// Example usage
(async () => {
  const tokenAddress = "0xabcdef1234567890"; // Replace with the token address
  const recipients = [
    "0x1111111111111111",
    "0x2222222222222222",
    "0x3333333333333333",
  ]; // Replace with recipient addresses
  const amounts = ["100", "200", "300"]; // Replace with token amounts

  await disperseTokens(tokenAddress, recipients, amounts);
})();
```
