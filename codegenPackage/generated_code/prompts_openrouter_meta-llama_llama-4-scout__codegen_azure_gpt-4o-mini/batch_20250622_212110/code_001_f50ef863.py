"""
Generated Code Metadata:
========================
Original URL: https://oddfellowsnft.com
Prompt: How can I enable JavaScript to access the SSOF NFT app, and what are the key features of the application?
Generated: DETERMINISTIC_f50ef863c5490eab
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3'; // For interacting with the Ethereum blockchain
import { SSOF_NFT_ABI, SSOF_NFT_ADDRESS } from './config'; // Import ABI and contract address

// Initialize Web3
let web3;

// Function to initialize Web3 and check for Ethereum provider
async function initWeb3() {
    if (window.ethereum) {
        // Use MetaMask's provider
        web3 = new Web3(window.ethereum);
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Ethereum account connected');
        } catch (error) {
            console.error('User denied account access', error);
        }
    } else {
        console.error('No Ethereum provider detected. Install MetaMask.');
    }
}

// Function to interact with the SSOF NFT contract
async function getNFTDetails(tokenId) {
    try {
        // Create contract instance
        const contract = new web3.eth.Contract(SSOF_NFT_ABI, SSOF_NFT_ADDRESS);
        
        // Fetch NFT details
        const nftDetails = await contract.methods.getNFTDetails(tokenId).call();
        console.log('NFT Details:', nftDetails);
        return nftDetails;
    } catch (error) {
        console.error('Error fetching NFT details:', error);
    }
}

// Function to mint a new NFT
async function mintNFT(tokenURI) {
    try {
        const accounts = await web3.eth.getAccounts();
        const contract = new web3.eth.Contract(SSOF_NFT_ABI, SSOF_NFT_ADDRESS);
        
        // Mint the NFT
        const transaction = await contract.methods.mintNFT(accounts[0], tokenURI).send({ from: accounts[0] });
        console.log('NFT Minted:', transaction);
    } catch (error) {
        console.error('Error minting NFT:', error);
    }
}

// Function to enable JavaScript access to the SSOF NFT app
async function enableSSOFApp() {
    await initWeb3();
    // Additional setup can be done here
}

// Key features of the SSOF NFT application
const keyFeatures = [
    'User-friendly interface for minting and managing NFTs',
    'Integration with Ethereum blockchain for secure transactions',
    'Ability to view and trade NFTs on a marketplace',
    'Support for multiple NFT standards (ERC721, ERC1155)',
    'Real-time updates on NFT ownership and transaction history'
];

// Execute the application
enableSSOFApp().then(() => {
    console.log('SSOF NFT app is ready to use');
});

// Export functions for external use
export { getNFTDetails, mintNFT };
```
