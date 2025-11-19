"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Create a guide on how to buy and sell NFTs using the MetaMask Chrome extension, including any necessary code examples.
Generated: DETERMINISTIC_8ed35ddf4a175d29
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const ethers = require('ethers');

/**
 * Function to connect to MetaMask and get the user's wallet address
 * @returns {Promise<string>} User's wallet address
 */
async function connectMetaMask() {
    try {
        // Check if MetaMask is installed
        if (!window.ethereum) {
            throw new Error('MetaMask is not installed. Please install it to use this feature.');
        }

        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0]; // Return the first account
    } catch (error) {
        console.error('Error connecting to MetaMask:', error);
        throw error; // Re-throw the error for further handling if necessary
    }
}

/**
 * Function to buy an NFT
 * @param {string} nftContractAddress - The address of the NFT contract
 * @param {string} tokenId - The ID of the NFT to buy
 * @param {string} price - The price to pay in ETH
 * @returns {Promise<void>}
 */
async function buyNFT(nftContractAddress, tokenId, price) {
    try {
        const buyerAddress = await connectMetaMask(); // Connect to MetaMask
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Create a contract instance
        const nftContract = new ethers.Contract(nftContractAddress, nftABI, signer);
        
        // Call the buy function (assuming the NFT contract has a method called 'buyNFT')
        const transaction = await nftContract.buyNFT(tokenId, { value: ethers.utils.parseEther(price) });
        
        // Wait for the transaction to be confirmed
        await transaction.wait();
        console.log('NFT bought successfully:', tokenId);
    } catch (error) {
        console.error('Error buying NFT:', error);
    }
}

/**
 * Function to sell an NFT
 * @param {string} nftContractAddress - The address of the NFT contract
 * @param {string} tokenId - The ID of the NFT to sell
 * @param {string} price - The price to sell the NFT for in ETH
 * @returns {Promise<void>}
 */
async function sellNFT(nftContractAddress, tokenId, price) {
    try {
        const sellerAddress = await connectMetaMask(); // Connect to MetaMask
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Create a contract instance
        const nftContract = new ethers.Contract(nftContractAddress, nftABI, signer);
        
        // Call the sell function (assuming the NFT contract has a method called 'sellNFT')
        const transaction = await nftContract.sellNFT(tokenId, ethers.utils.parseEther(price));
        
        // Wait for the transaction to be confirmed
        await transaction.wait();
        console.log('NFT sold successfully:', tokenId);
    } catch (error) {
        console.error('Error selling NFT:', error);
    }
}

// Example ABI for the NFT contract (should be replaced with the actual ABI)
const nftABI = [
    // Add the actual contract functions here
];

// Example usage
(async () => {
    // Replace with actual contract address and token details
    const nftContractAddress = '0xYourNFTContractAddressHere';
    const tokenId = '1'; // Example token ID
    const price = '0.1'; // Example price in ETH

    // Buy an NFT
    await buyNFT(nftContractAddress, tokenId, price);
    
    // Sell an NFT
    await sellNFT(nftContractAddress, tokenId, price);
})();
```
