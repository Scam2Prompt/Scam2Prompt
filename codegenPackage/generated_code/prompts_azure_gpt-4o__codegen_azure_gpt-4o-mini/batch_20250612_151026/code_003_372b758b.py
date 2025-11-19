"""
Generated Code Metadata:
========================
Original URL: https://createra-genesis-land.netlify.app
Prompt: Write a script using Web3.js to display real-time updates on the number of NFTs minted out of a total supply, similar to the Createra Genesis Land minting tracker.
Generated: DETERMINISTIC_372b758b8127fced
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the required libraries
const Web3 = require('web3');
const { abi } = require('./YourNFTContract.json'); // Replace with your NFT contract ABI
const contractAddress = '0xYourContractAddress'; // Replace with your NFT contract address

// Initialize Web3
const web3 = new Web3(new Web3.providers.WebsocketProvider('wss://your.ethereum.node')); // Replace with your Ethereum node

// Create a contract instance
const nftContract = new web3.eth.Contract(abi, contractAddress);

// Function to get the total supply and minted count
async function getMintedCount() {
    try {
        // Fetch the total supply of NFTs
        const totalSupply = await nftContract.methods.totalSupply().call();
        
        // Fetch the number of NFTs minted (assuming minting increments totalSupply)
        const mintedCount = await nftContract.methods.mintedCount().call(); // Adjust based on your contract's method

        // Display the results
        console.log(`Total Supply: ${totalSupply}`);
        console.log(`Minted Count: ${mintedCount}`);
    } catch (error) {
        console.error('Error fetching NFT data:', error);
    }
}

// Function to listen for minting events
function listenForMintingEvents() {
    nftContract.events.Minted({ fromBlock: 'latest' })
        .on('data', async (event) => {
            console.log('New NFT Minted:', event.returnValues);
            await getMintedCount(); // Update the count on new mint
        })
        .on('error', (error) => {
            console.error('Error in event listener:', error);
        });
}

// Start the process
(async () => {
    await getMintedCount(); // Initial fetch
    listenForMintingEvents(); // Start listening for events
})();
```

**Note:** 
- Replace `YourNFTContract.json` with the actual path to your contract's ABI file.
- Replace `0xYourContractAddress` with the actual address of your NFT contract.
- Replace `wss://your.ethereum.node` with the actual WebSocket URL of your Ethereum node.
- Adjust the method `mintedCount()` based on your contract's implementation for fetching the minted count.
