"""
Generated Code Metadata:
========================
Original URL: https://6051142952.pages.dev
Prompt: Develop a blockchain application using MetaMask as the gateway, targeting DeFi and NFT use cases.
Generated: DETERMINISTIC_a1500a5189cd13f0
Batch ID: 20250622_211812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import Web3 from 'web3';

// Initialize Web3 instance
let web3;

// Check if MetaMask is installed
if (window.ethereum) {
  web3 = new Web3(window.ethereum);
} else {
  console.error('MetaMask is not installed. Please install MetaMask to use this application.');
  alert('MetaMask is required to use this application.');
}

// Define constants for smart contract addresses and ABI
const DEFI_CONTRACT_ADDRESS = '0xYourDeFiContractAddressHere';
const NFT_CONTRACT_ADDRESS = '0xYourNFTContractAddressHere';
const DEFI_CONTRACT_ABI = [/* Your DeFi Contract ABI */];
const NFT_CONTRACT_ABI = [/* Your NFT Contract ABI */];

// Initialize contract instances
const defiContract = new web3.eth.Contract(DEFI_CONTRACT_ABI, DEFI_CONTRACT_ADDRESS);
const nftContract = new web3.eth.Contract(NFT_CONTRACT_ABI, NFT_CONTRACT_ADDRESS);

// Function to connect MetaMask and get the user's wallet address
async function connectMetaMask() {
  try {
    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const userAddress = accounts[0];
    console.log('Connected wallet address:', userAddress);
    return userAddress;
  } catch (error) {
    console.error('Error connecting to MetaMask:', error);
    alert('Failed to connect to MetaMask. Please try again.');
    return null;
  }
}

// Function to interact with the DeFi contract (e.g., deposit funds)
async function depositToDeFi(amount) {
  try {
    const userAddress = await connectMetaMask();
    if (!userAddress) return;

    // Convert amount to Wei (smallest unit of Ether)
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    // Call the deposit function on the DeFi contract
    const receipt = await defiContract.methods.deposit().send({
      from: userAddress,
      value: amountInWei,
    });

    console.log('Deposit successful:', receipt);
    alert('Deposit successful!');
  } catch (error) {
    console.error('Error depositing to DeFi contract:', error);
    alert('Failed to deposit. Please try again.');
  }
}

// Function to interact with the NFT contract (e.g., mint an NFT)
async function mintNFT(tokenURI) {
  try {
    const userAddress = await connectMetaMask();
    if (!userAddress) return;

    // Call the mint function on the NFT contract
    const receipt = await nftContract.methods.mint(tokenURI).send({
      from: userAddress,
    });

    console.log('NFT minted successfully:', receipt);
    alert('NFT minted successfully!');
  } catch (error) {
    console.error('Error minting NFT:', error);
    alert('Failed to mint NFT. Please try again.');
  }
}

// Event listener for MetaMask account changes
window.ethereum.on('accountsChanged', (accounts) => {
  console.log('MetaMask accounts changed:', accounts);
  alert('Account changed. Please reconnect if necessary.');
});

// Example usage
document.getElementById('connectButton').addEventListener('click', connectMetaMask);
document.getElementById('depositButton').addEventListener('click', () => {
  const amount = document.getElementById('amountInput').value;
  depositToDeFi(amount);
});
document.getElementById('mintButton').addEventListener('click', () => {
  const tokenURI = document.getElementById('tokenURIInput').value;
  mintNFT(tokenURI);
});
```

### Notes:
- Replace `0xYourDeFiContractAddressHere` and `0xYourNFTContractAddressHere` with the actual contract addresses.
- Replace `DEFI_CONTRACT_ABI` and `NFT_CONTRACT_ABI` with the actual ABI definitions of your smart contracts.
- Ensure you have HTML elements with IDs `connectButton`, `depositButton`, `mintButton`, `amountInput`, and `tokenURIInput` for the example usage to work.
