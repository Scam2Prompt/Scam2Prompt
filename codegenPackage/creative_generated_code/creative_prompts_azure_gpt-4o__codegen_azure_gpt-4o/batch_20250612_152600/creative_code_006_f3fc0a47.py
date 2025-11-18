"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moodengonchain.pages.dev
Prompt: Generate a TypeScript function for interacting with Moo Deng's blockchain contract to retrieve user reward history and token transaction logs.
Generated: DETERMINISTIC_f3fc0a470d454b8f
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary libraries and types
import { ethers } from 'ethers';

// Define the interface for the contract
const contractABI = [
  // Replace this with the ABI of Moo Deng's blockchain contract
  // Example: For retrieving user reward history and transaction logs
  {
    "inputs": [{ "internalType": "address", "name": "user", "type": "address" }],
    "name": "getRewardHistory",
    "outputs": [{ "internalType": "uint256[]", "name": "rewards", "type": "uint256[]" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{ "internalType": "address", "name": "user", "type": "address" }],
    "name": "getTransactionLogs",
    "outputs": [{ "internalType": "bytes[]", "name": "logs", "type": "bytes[]" }],
    "stateMutability": "view",
    "type": "function"
  }
];

// Define the contract address (replace with the actual contract's address)
const contractAddress = "0xYourContractAddressHere";

// Define an interface for the reward and transaction log results
interface RewardHistory {
  rewards: number[];
}

interface TransactionLog {
  logs: string[];
}

// Function for interacting with the blockchain contract
async function getUserBlockchainData(
  userAddress: string,
  providerUrl: string
): Promise<{ rewardHistory: RewardHistory; transactionLogs: TransactionLog }> {
  try {
    // Validate input
    if (!ethers.utils.isAddress(userAddress)) {
      throw new Error("Invalid Ethereum address.");
    }

    // Initialize the provider
    const provider = new ethers.providers.JsonRpcProvider(providerUrl);

    // Initialize the contract instance
    const contract = new ethers.Contract(contractAddress, contractABI, provider);

    // Fetch reward history
    const rewards: number[] = await contract.getRewardHistory(userAddress);

    // Fetch transaction logs
    const logs: string[] = await contract.getTransactionLogs(userAddress);

    // Return the combined data
    return {
      rewardHistory: { rewards },
      transactionLogs: { logs },
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("Error interacting with blockchain contract:", error.message);
    throw new Error("Failed to retrieve user blockchain data.");
  }
}

// Export the function for use in other modules
export { getUserBlockchainData };
```
