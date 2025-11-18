"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Develop a JavaScript function to interact with an NFT marketplace using the MetaMask Chrome extension for buying and selling NFTs.
Generated: DETERMINISTIC_2b797f2467a02a8a
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script enables interaction with an NFT marketplace using MetaMask to buy and sell NFTs.
 * It assumes the use of Web3.js for blockchain communication.
 * Ensure that MetaMask is installed and Web3.js is included in your project.
 */

// Import Web3 library (Ensure Web3.js is installed using npm or include via CDN in your project)
const Web3 = require('web3');

// Create a Web3 instance and connect to MetaMask's provider
const web3 = new Web3(window.ethereum);

/**
 * Function to buy an NFT from the marketplace.
 * @param {string} nftContractAddress - The contract address of the NFT.
 * @param {number} tokenId - The ID of the token to purchase.
 * @param {string} priceInWei - The price of the NFT in Wei (smallest unit of ETH).
 * @returns {Promise<string>} Transaction hash if successful.
 */
async function buyNFT(nftContractAddress, tokenId, priceInWei) {
  try {
    // Request account connection via MetaMask
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get the connected MetaMask account
    const accounts = await web3.eth.getAccounts();
    const buyer = accounts[0]; // The first account in the list

    // Create a contract instance for the NFT
    const nftContract = new web3.eth.Contract(
      [
        // ABI snippet for a simple ERC721 `transferFrom` function
        {
          constant: false,
          inputs: [
            { name: 'from', type: 'address' },
            { name: 'to', type: 'address' },
            { name: 'tokenId', type: 'uint256' },
          ],
          name: 'transferFrom',
          outputs: [],
          payable: true,
          stateMutability: 'nonpayable',
          type: 'function',
        },
      ],
      nftContractAddress
    );

    // Call the `transferFrom` function to buy the NFT
    const transaction = await nftContract.methods
      .transferFrom('SELLER_ADDRESS', buyer, tokenId) // Replace 'SELLER_ADDRESS' with the actual seller's address
      .send({ from: buyer, value: priceInWei });

    return transaction.transactionHash; // Return the transaction hash
  } catch (error) {
    console.error('Error buying NFT:', error);
    throw new Error('Failed to buy NFT. Please check your inputs and try again.');
  }
}

/**
 * Function to sell an NFT on the marketplace.
 * @param {string} nftContractAddress - The contract address of the NFT.
 * @param {number} tokenId - The ID of the token to list for sale.
 * @param {string} buyerAddress - The address of the buyer to transfer the NFT to.
 * @returns {Promise<string>} Transaction hash if successful.
 */
async function sellNFT(nftContractAddress, tokenId, buyerAddress) {
  try {
    // Request account connection via MetaMask
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get the connected MetaMask account
    const accounts = await web3.eth.getAccounts();
    const seller = accounts[0]; // The first account in the list

    // Create a contract instance for the NFT
    const nftContract = new web3.eth.Contract(
      [
        // ABI snippet for a simple ERC721 `transferFrom` function
        {
          constant: false,
          inputs: [
            { name: 'from', type: 'address' },
            { name: 'to', type: 'address' },
            { name: 'tokenId', type: 'uint256' },
          ],
          name: 'transferFrom',
          outputs: [],
          payable: false,
          stateMutability: 'nonpayable',
          type: 'function',
        },
      ],
      nftContractAddress
    );

    // Call the `transferFrom` function to sell the NFT to the buyer
    const transaction = await nftContract.methods
      .transferFrom(seller, buyerAddress, tokenId)
      .send({ from: seller });

    return transaction.transactionHash; // Return the transaction hash
  } catch (error) {
    console.error('Error selling NFT:', error);
    throw new Error('Failed to sell NFT. Please check your inputs and try again.');
  }
}

// Export the functions for use in your application
module.exports = {
  buyNFT,
  sellNFT,
};
```
