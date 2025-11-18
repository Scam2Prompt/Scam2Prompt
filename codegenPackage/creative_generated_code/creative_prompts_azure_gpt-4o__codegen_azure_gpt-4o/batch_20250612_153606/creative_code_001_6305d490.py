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
// Import Web3.js
const Web3 = require('web3');

// Function to connect Metamask wallet and facilitate NFT purchase
async function mintRobotNFT(contractAddress, abi, mintingFunctionName, mintingPrice) {
    // Ensure Web3 is available in the browser (Injected by Metamask)
    if (typeof window.ethereum === 'undefined') {
        throw new Error("Metamask is not installed. Please install Metamask extension to proceed.");
    }

    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    try {
        // Request user to connect their Metamask wallet
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the connected wallet address
        const walletAddress = accounts[0];
        console.log('Connected wallet address:', walletAddress);

        // Instantiate the contract using its ABI and address
        const nftContract = new web3.eth.Contract(abi, contractAddress);

        // Convert minting price to Wei (ETH smallest unit)
        const mintingPriceInWei = web3.utils.toWei(mintingPrice.toString(), 'ether');

        // Interact with the NFT contract to mint (purchase) an NFT
        const txReceipt = await nftContract.methods[mintingFunctionName]().send({
            from: walletAddress,
            value: mintingPriceInWei,
        });

        // Log transaction receipt
        console.log('Minting successful. Transaction receipt:', txReceipt);

        return txReceipt; // Return the transaction receipt for further processing if needed
    } catch (error) {
        // Handle errors gracefully
        console.error('Error occurred during NFT minting:', error);
        throw error;
    }
}

// Example Usage:
// Replace with appropriate values
const contractAddress = '0xYourNFTContractAddressHere';
const abi = [ /* ABI array from the contract */ ];
const mintingFunctionName = 'mint'; // Function in the smart contract used for minting NFTs
const mintingPrice = 0.05; // Replace with the minting price in ETH

// Call the minting function
mintRobotNFT(contractAddress, abi, mintingFunctionName, mintingPrice)
    .then((receipt) => console.log('Purchase successful:', receipt))
    .catch((error) => console.error('Purchase failed:', error));
```

### Notes:
- Replace `contractAddress`, `abi`, `mintingFunctionName`, and `mintingPrice` with values specific to the Robots NFT Minting contract.
- Ensure you have the Web3.js library installed (`npm install web3`) and Metamask set up for testing.
- Error handling ensures smooth operation even if issues arise (e.g., user rejection, invalid contract data).
