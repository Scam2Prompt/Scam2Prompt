"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Generate an example of a UserOp transaction that can be processed across multiple chains using Particle Network's infrastructure.
Generated: DETERMINISTIC_041af7468a1395b3
Batch ID: 20250612_164305
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.yournetwork.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and dependencies
const { ethers } = require("ethers");
const ParticleNetworkSDK = require("particle-network-sdk"); // Hypothetical SDK import

// Constants
const PARTICLE_NETWORK_API_KEY = "your_api_key_here"; // Replace with your Particle Network API key
const USER_OP_CONTRACT_ADDRESS = "0xYourUserOpContractAddress"; // Replace with your contract's address
const RPC_URL = "https://rpc.yournetwork.com"; // Replace with the RPC URL of the blockchain network

// Initialize Particle Network SDK
const particleNetwork = new ParticleNetworkSDK({
  apiKey: PARTICLE_NETWORK_API_KEY,
});

// Function to submit a UserOp transaction
async function submitUserOpTransaction(userOpData, chainId) {
  try {
    // Initialize the provider for the specified chain
    const provider = new ethers.providers.JsonRpcProvider(RPC_URL);

    // Create a signer (you can use a wallet private key or a Particle Network signer)
    const privateKey = "your_private_key_here"; // Replace with your private key
    const walletSigner = new ethers.Wallet(privateKey, provider);

    // Create a contract instance for interacting with the UserOp smart contract
    const userOpContract = new ethers.Contract(
      USER_OP_CONTRACT_ADDRESS,
      [
        // ABI fragment for the UserOp contract
        "function handleUserOp(bytes calldata userOpData) public",
      ],
      walletSigner
    );

    // Call the contract method "handleUserOp" with the userOpData
    const tx = await userOpContract.handleUserOp(userOpData);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();

    // Log the transaction receipt
    console.log("Transaction succeeded with receipt:", receipt);

    return receipt; // Return the transaction receipt
  } catch (error) {
    // Handle errors gracefully
    console.error("Error submitting UserOp transaction:", error);
    throw new Error("Failed to submit UserOp transaction");
  }
}

// Example usage
(async () => {
  try {
    // Example UserOp data (replace with actual data relevant to your application)
    const userOpData = ethers.utils.hexlify(ethers.utils.toUtf8Bytes("example_data"));

    // Example chain ID (replace with target chain ID)
    const targetChainId = 1; // Ethereum Mainnet as an example

    // Submit the UserOp transaction
    const receipt = await submitUserOpTransaction(userOpData, targetChainId);

    // Log the successful receipt
    console.log("UserOp transaction successfully processed:", receipt);
  } catch (error) {
    console.error("Error processing UserOp transaction:", error);
  }
})();
```
