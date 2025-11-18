"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Create a function in JavaScript using the Web3.js library to connect a Metamask wallet and facilitate the purchase of NFTs, referencing the minting process outlined on the Robots NFT Minting website.
Generated: DETERMINISTIC_6305d490edf2e85f
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
import Web3 from 'web3';

// Initialize the Web3 instance
let web3;

// Function to connect to MetaMask and facilitate NFT purchase
async function connectAndPurchaseNFT(contractAddress, tokenId, mintingPrice) {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install it to use this feature.');
        }

        // Create a new instance of Web3 using MetaMask's provider
        web3 = new Web3(window.ethereum);

        // Request account access from the user
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Create a contract instance
        const contractABI = [/* Add your contract ABI here */];
        const contract = new web3.eth.Contract(contractABI, contractAddress);

        // Convert minting price to Wei
        const mintingPriceInWei = web3.utils.toWei(mintingPrice.toString(), 'ether');

        // Call the mint function of the NFT contract
        const tx = await contract.methods.mintNFT(userAddress, tokenId).send({
            from: userAddress,
            value: mintingPriceInWei,
        });

        // Log transaction details
        console.log('Transaction successful:', tx);
        alert('NFT purchased successfully!');
    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred:', error.message);
        alert('Error: ' + error.message);
    }
}

// Example usage
// connectAndPurchaseNFT('0xYourContractAddressHere', '1', '0.05');
```
