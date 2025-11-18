"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jamcards.io
Prompt: Develop a script using web3.js to query Ethereum blockchain data for the ownership distribution of the "Heart Full of Love JamCards" collection.
Generated: DETERMINISTIC_19be8561b9e2ebba
Batch ID: 20250612_150034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`": {
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
// Import required libraries
const Web3 = require('web3');

// Define constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura Project ID
const CONTRACT_ADDRESS = "0xYourContractAddress";  // Replace with the JamCards contract address
const ABI = [                                     // Replace with the ABI of the JamCards contract
  // Add the ABI definition here
];

// Initialize Web3 instance
const web3 = new Web3(`https://mainnet.infura.io/v3/${INFURA_PROJECT_ID}`);

// Create a contract instance
const jamCardsContract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

/**
 * Fetch ownership data for the JamCards collection.
 */
async function fetchOwnershipDistribution() {
  try {
    console.log("Fetching total supply of JamCards...");

    // Query the total supply of JamCards
    const totalSupply = await jamCardsContract.methods.totalSupply().call();

    console.log(`Total supply: ${totalSupply}`);

    const ownershipDistribution = {};

    // Iterate through each token ID to find its owner
    for (let tokenId = 1; tokenId <= totalSupply; tokenId++) {
      console.log(`Fetching owner for token ID: ${tokenId}...`);

      const owner = await jamCardsContract.methods.ownerOf(tokenId).call();

      // Accumulate ownership counts
      if (ownershipDistribution[owner]) {
        ownershipDistribution[owner]++;
      } else {
        ownershipDistribution[owner] = 1;
      }
    }

    // Log ownership distribution
    console.log("Ownership distribution:");
    console.log(ownershipDistribution);

    return ownershipDistribution;

  } catch (error) {
    console.error("Error fetching ownership distribution:", error.message);
    throw new Error("Failed to fetch ownership data.");
  }
}

// Entry point
(async () => {
  try {
    console.log("Starting ownership distribution query...");
    const distribution = await fetchOwnershipDistribution();
    console.log("Successfully fetched ownership distribution:", distribution);
  } catch (error) {
    console.error("An error occurred during execution:", error.message);
  }
})();
```

**Note:**
1. Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura Project ID.
2. Replace `0xYourContractAddress` with the actual contract address for the "Heart Full of Love JamCards" collection.
3. Replace the ABI array with the actual ABI of the contract. If you don't have the ABI, you can fetch it from a blockchain explorer like Etherscan.
