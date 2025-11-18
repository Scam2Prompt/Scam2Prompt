"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-staking-xi.vercel.app
Prompt: Recommend libraries or tools for interacting with the Exeptra NFT-staking Dapp smart contracts on the Polygon testnet and provide an example of their usage.
Generated: DETERMINISTIC_a07f1fc30f85d127
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc-mumbai.maticvigil.com/": {
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
// Import the required libraries
const { ethers } = require("ethers");

// Define the provider for the Polygon testnet
const provider = new ethers.providers.JsonRpcProvider("https://rpc-mumbai.maticvigil.com/");

// Define the contract ABI and address (replace with actual values)
const contractABI = [
    // The ABI of the contract should be provided here as an array of objects
    // Example:
    // {
    //     "inputs": [],
    //     "name": "stake",
    //     "outputs": [],
    //     "stateMutability": "nonpayable",
    //     "type": "function"
    // },
    // Add more functions as needed
];

const contractAddress = "0xYourContractAddress"; // Replace with the actual contract address

// Create a contract instance
const contract = new ethers.Contract(contractAddress, contractABI, provider);

// Function to stake NFTs
async function stakeNFT(tokenId, userPrivateKey) {
    try {
        // Create a wallet instance
        const wallet = new ethers.Wallet(userPrivateKey, provider);

        // Connect the contract to the wallet
        const contractWithSigner = contract.connect(wallet);

        // Call the stake function
        const tx = await contractWithSigner.stake(tokenId);
        console.log(`Staking NFT with token ID ${tokenId}. Transaction Hash: ${tx.hash}`);

        // Wait for the transaction to be mined
        await tx.wait();
        console.log('Stake successful!');
    } catch (error) {
        console.error('Error staking NFT:', error);
    }
}

// Function to check staking status
async function checkStakeStatus(tokenId) {
    try {
        const isStaked = await contract.isStaked(tokenId);
        console.log(`NFT with token ID ${tokenId} is ${isStaked ? 'currently staked.' : 'not staked.'}`);
    } catch (error) {
        console.error('Error checking stake status:', error);
    }
}

// Example usage:
const userPrivateKey = "0xYourPrivateKey"; // Replace with the user's private key
const tokenId = 1; // Replace with the actual token ID to stake

// Stake an NFT
stakeNFT(tokenId, userPrivateKey);

// Check staking status
checkStakeStatus(tokenId);
```
