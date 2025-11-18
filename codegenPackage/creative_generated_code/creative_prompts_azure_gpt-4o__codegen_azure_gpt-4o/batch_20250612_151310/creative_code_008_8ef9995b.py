"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubatewhitelist.pages.dev
Prompt: Write a script using ethers.js to connect a wallet and retrieve staking data, including reward calculations and lock terms, as described on Decubate's whitelist portal.
Generated: DETERMINISTIC_8ef9995b4e4d98f2
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js
const { ethers } = require("ethers");

// Decubate whitelist portal contract address & ABI (update these values accordingly)
const DECUBATE_CONTRACT_ADDRESS = "0xYourDecubateContractAddressHere";
const DECUBATE_CONTRACT_ABI = [
  // ABI goes here, truncated for brevity
  {
    "constant": true,
    "inputs": [{ "name": "account", "type": "address" }],
    "name": "getStakingData",
    "outputs": [
      { "name": "stakedAmount", "type": "uint256" },
      { "name": "rewardsEarned", "type": "uint256" },
      { "name": "lockDuration", "type": "uint256" }
    ],
    "type": "function"
  },
  // Add other relevant functions if needed
];

async function main() {
  try {
    // Set up Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Request user to connect their wallet
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();

    // Get user's wallet address
    const walletAddress = await signer.getAddress();
    console.log(`Connected wallet: ${walletAddress}`);

    // Connect to Decubate whitelist portal contract
    const contract = new ethers.Contract(
      DECUBATE_CONTRACT_ADDRESS,
      DECUBATE_CONTRACT_ABI,
      signer
    );

    // Fetch staking data for the connected wallet
    const stakingData = await contract.getStakingData(walletAddress);

    // Extract staking information
    const stakedAmount = ethers.utils.formatUnits(stakingData.stakedAmount, 18); // Assuming token has 18 decimals
    const rewardsEarned = ethers.utils.formatUnits(stakingData.rewardsEarned, 18); // Format rewards similarly
    const lockDuration = stakingData.lockDuration; // Assuming lockDuration is in seconds

    // Convert lock duration into a more human-readable format
    const lockDurationDays = Math.floor(lockDuration / (60 * 60 * 24)); // Convert seconds to days
    
    // Log staking data
    console.log("Staking Data:");
    console.log(`- Staked Amount: ${stakedAmount} tokens`);
    console.log(`- Rewards Earned: ${rewardsEarned} tokens`);
    console.log(`- Lock Duration: ${lockDurationDays} days`);
  } catch (error) {
    // Handle errors appropriately
    console.error("An error occurred while fetching staking data:", error);
  }
}

// Execute the script
main();
```

**Important Notes:**
1. Replace the `DECUBATE_CONTRACT_ADDRESS` and `DECUBATE_CONTRACT_ABI` placeholders with the actual address and ABI of the Decubate whitelist portal contract.
2. Ensure that the wallet being used has access to the blockchain network where Decubate operates.
3. This script assumes the existence of a `getStakingData` method on the Decubate contract—double-check the contract's ABI and documentation to confirm this.
