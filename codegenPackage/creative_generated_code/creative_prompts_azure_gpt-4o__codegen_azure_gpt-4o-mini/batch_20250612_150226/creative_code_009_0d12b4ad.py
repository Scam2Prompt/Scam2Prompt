"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e1-9n2.pages.dev
Prompt: Create a script in JavaScript to fetch and display the current total supply of NFTs and the maximum number of NFTs that can be minted from a smart contract.
Generated: DETERMINISTIC_0d12b4ada03ac704
Batch ID: 20250612_150226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Import the necessary libraries
const Web3 = require('web3');
const axios = require('axios');

// Configuration
const INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS'; // Replace with the NFT contract address
const ABI = [ /* ABI of the NFT contract */ ];

// Initialize web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// Initialize the contract
const nftContract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

/**
 * Fetch and display the current total supply of NFTs and the maximum supply.
 */
async function fetchNFTSupply() {
    try {
        // Call the totalSupply method from the smart contract
        const totalSupply = await nftContract.methods.totalSupply().call();
        console.log(`Current Total Supply of NFTs: ${totalSupply}`);

        // Call the maxSupply method from the smart contract (if available)
        const maxSupply = await nftContract.methods.MAX_SUPPLY().call(); // Adjust method name if necessary
        console.log(`Maximum Supply of NFTs: ${maxSupply}`);
    } catch (error) {
        // Handle errors that may occur during the contract calls
        console.error('Error fetching NFT supply:', error.message);
    }
}

// Invoke the function to fetch and display the NFT supply
fetchNFTSupply();
```

**Note:** 
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
- Replace `YOUR_CONTRACT_ADDRESS` with the actual NFT contract address.
- Replace `/* ABI of the NFT contract */` with the actual ABI of the NFT contract.
- Ensure that the method names (`totalSupply` and `MAX_SUPPLY`) match those defined in your NFT smart contract. Adjust accordingly if they are different.
