"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3api-resolver.pages.dev
Prompt: Provide an example of how to troubleshoot NFT management issues using the Web3 API Resolver's features.
Generated: DETERMINISTIC_4dafffdd5606c08d
Batch ID: 20250612_162346
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
// Import necessary libraries
const Web3 = require('web3');

// Initialize Web3 with an Ethereum provider
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'));

// Function to check the balance of an NFT for a given address
async function checkNFTBalance(contractAddress, ownerAddress) {
    try {
        // Create an instance of the ERC721 contract
        const contract = new web3.eth.Contract(ERC721_ABI, contractAddress);
        
        // Call the balanceOf function from the ERC721 standard
        const balance = await contract.methods.balanceOf(ownerAddress).call();
        
        console.log(`NFT Balance for address ${ownerAddress}: ${balance}`);
        return balance;
    } catch (error) {
        console.error('Error checking NFT balance:', error);
        throw new Error('Failed to check NFT balance');
    }
}

// Function to retrieve NFT ownership details
async function getNFTDetails(contractAddress, tokenId) {
    try {
        const contract = new web3.eth.Contract(ERC721_ABI, contractAddress);
        
        // Call the ownerOf function from the ERC721 standard
        const owner = await contract.methods.ownerOf(tokenId).call();
        
        console.log(`Owner of NFT with Token ID ${tokenId}: ${owner}`);
        return owner;
    } catch (error) {
        console.error('Error retrieving NFT details:', error);
        throw new Error('Failed to retrieve NFT details');
    }
}

// Example Usage
(async () => {
    const contractAddress = 'YOUR_NFT_CONTRACT_ADDRESS'; // Replace with your NFT contract address
    const ownerAddress = 'OWNER_ADDRESS'; // Replace with the owner's Ethereum address
    const tokenId = 'TOKEN_ID'; // Replace with the NFT token ID you want to check

    // Check NFT balance
    await checkNFTBalance(contractAddress, ownerAddress);
    
    // Get NFT ownership details
    await getNFTDetails(contractAddress, tokenId);
})();

// ERC721 ABI definition (simplified for balanceOf and ownerOf functions)
const ERC721_ABI = [
    {
        "constant": true,
        "inputs": [{ "name": "_owner", "type": "address" }],
        "name": "balanceOf",
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{ "name": "_tokenId", "type": "uint256" }],
        "name": "ownerOf",
        "outputs": [{ "name": "", "type": "address" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];
```
