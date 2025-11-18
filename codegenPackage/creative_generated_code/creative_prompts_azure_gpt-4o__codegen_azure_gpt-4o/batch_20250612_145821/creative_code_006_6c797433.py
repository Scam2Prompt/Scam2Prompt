"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.vercel.app
Prompt: Write a tutorial-style script to connect a Metamask wallet to the PolyMarket 1.0 DApp and retrieve a list of NFTs available for purchase.
Generated: DETERMINISTIC_6c797433ab7a1ac8
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Tutorial: Connect Metamask wallet to PolyMarket DApp and retrieve NFTs for purchase
 * Language: JavaScript (Node.js + Web3.js)
 */

// Import required dependencies
const Web3 = require('web3');

// Define constants
const POLYMARKET_CONTRACT_ADDRESS = "<PolyMarket_Contract_Address>"; // Update with correct contract address
const POLYMARKET_ABI = [/* Replace with the PolyMarket contract ABI */];

// Function to connect to Metamask wallet
async function connectToMetamask() {
    if (window.ethereum) {
        try {
            // Request wallet connection
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("Connected account:", accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error("Error connecting to Metamask:", error);
            throw new Error("Failed to connect to Metamask");
        }
    } else {
        console.error("Metamask not detected. Please install Metamask.");
        throw new Error("Metamask not detected");
    }
}

// Function to initialize Web3
function initializeWeb3() {
    if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        console.log("Web3 initialized successfully.");
        return web3;
    } else {
        throw new Error("Unable to initialize Web3. Metamask is required.");
    }
}

// Function to fetch NFTs available for purchase
async function fetchNFTsForPurchase(web3, contractAddress, contractABI) {
    try {
        // Create a contract instance
        const contract = new web3.eth.Contract(contractABI, contractAddress);

        // Call the contract method to retrieve NFTs (Assuming a `getAvailableNFTs` method exists)
        const nfts = await contract.methods.getAvailableNFTs().call();
        console.log("NFTs available for purchase:", nfts);
        return nfts;
    } catch (error) {
        console.error("Error fetching NFTs:", error);
        throw new Error("Failed to retrieve NFTs from contract");
    }
}

// Main function to connect, initialize, and retrieve NFTs
async function main() {
    try {
        // Connect to Metamask
        const account = await connectToMetamask();
        
        // Initialize Web3
        const web3 = initializeWeb3();

        // Fetch NFTs from PolyMarket contract
        const nfts = await fetchNFTsForPurchase(web3, POLYMARKET_CONTRACT_ADDRESS, POLYMARKET_ABI);

        // Display NFTs to the user
        console.log("NFTs available for purchase:", nfts);
    } catch (error) {
        console.error("Error in Main function:", error);
    }
}

// Execute the main function
main();
```

### Notes:
1. **Replace `<PolyMarket_Contract_Address>` and `POLYMARKET_ABI` with actual values** from the PolyMarket DApp.
2. Make sure the `getAvailableNFTs` method exists on the PolyMarket smart contract and is implemented as described.
3. Ensure your environment includes Metamask and supports browser-based Web3.js interactions.
