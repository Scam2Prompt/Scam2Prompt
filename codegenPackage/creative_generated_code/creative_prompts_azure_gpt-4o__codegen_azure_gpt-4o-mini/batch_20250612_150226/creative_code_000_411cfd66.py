"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e1-9n2.pages.dev
Prompt: Write a script in JavaScript to connect a user's Ethereum wallet using Web3.js and display the total supply of NFTs available for minting from a smart contract.
Generated: DETERMINISTIC_411cfd66b6be212c
Batch ID: 20250612_150226
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

// Smart Contract ABI (Application Binary Interface) and Address
const contractABI = [
    // Replace with the actual ABI of the NFT contract
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];
const contractAddress = '0xYourContractAddressHere'; // Replace with your contract's address

// Initialize Web3
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
} else {
    alert('Please install MetaMask to use this feature.');
}

// Connect to the user's Ethereum wallet
async function connectWallet() {
    try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Wallet connected');
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
    }
}

// Retrieve total supply of NFTs from the smart contract
async function getTotalSupply() {
    try {
        // Create contract instance
        const contract = new web3.eth.Contract(contractABI, contractAddress);
        
        // Call totalSupply function from the contract
        const totalSupply = await contract.methods.totalSupply().call();
        
        // Display the total supply
        console.log(`Total Supply of NFTs: ${totalSupply}`);
        document.getElementById('total-supply').innerText = `Total Supply of NFTs: ${totalSupply}`;
    } catch (error) {
        console.error('Error retrieving total supply:', error);
    }
}

// Event listener for wallet connection button
document.getElementById('connect-button').addEventListener('click', async () => {
    await connectWallet();
    await getTotalSupply();
});

// HTML structure to display the total supply
document.body.innerHTML += `
    <button id="connect-button">Connect Wallet</button>
    <div id="total-supply"></div>
`;
```

Make sure to replace `'0xYourContractAddressHere'` with your actual NFT smart contract address and provide the correct ABI for the contract. This code also assumes that the user has MetaMask installed.
