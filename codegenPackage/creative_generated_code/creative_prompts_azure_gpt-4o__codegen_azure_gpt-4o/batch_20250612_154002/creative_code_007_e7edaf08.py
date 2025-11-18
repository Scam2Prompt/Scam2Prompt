"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqqh.com
Prompt: Write code to integrate a DeFi application with Ethereum using JavaScript, ensuring compatibility with MetaMask.
Generated: DETERMINISTIC_e7edaf08ccb28ba1
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3'); // Web3.js for interacting with Ethereum
const contractABI = require('./contractABI.json'); // Import the ABI of the smart contract

// Define constants
const contractAddress = '0xYourContractAddressHere'; // Replace with your deployed contract's address

// Function to initialize web3 and connect to MetaMask
async function connectToMetaMask() {
    // Check if MetaMask is installed
    if (window.ethereum) {
        const web3 = new Web3(window.ethereum); // Initialize web3 with MetaMask provider
        try {
            // Request account access from MetaMask
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask connected successfully');
            return web3;
        } catch (error) {
            console.error('User rejected connection to MetaMask:', error);
            throw new Error('Unable to connect to MetaMask');
        }
    } else {
        console.error('MetaMask is not installed');
        throw new Error('MetaMask not detected');
    }
}

// Function to interact with the deployed smart contract
async function interactWithContract() {
    try {
        const web3 = await connectToMetaMask(); // Connect to MetaMask
        const accounts = await web3.eth.getAccounts(); // Get connected accounts
        const userAccount = accounts[0]; // Use the first account

        console.log('Connected account:', userAccount);

        // Instantiate the smart contract
        const contract = new web3.eth.Contract(contractABI, contractAddress);
        console.log('Smart contract instantiated');

        // Example: Call a read-only function from the smart contract
        const data = await contract.methods.yourReadOnlyFunction().call();
        console.log('Data from smart contract:', data);

        // Example: Send a transaction to the smart contract
        const tx = await contract.methods.yourWriteFunction('param1', 'param2').send({ 
            from: userAccount 
        });
        console.log('Transaction successful:', tx);
    } catch (error) {
        console.error('Error interacting with contract:', error);
    }
}

// Event listener for user interaction (example)
document.getElementById('connectButton').addEventListener('click', async () => {
    try {
        await interactWithContract();
    } catch (error) {
        console.error('Error:', error.message);
    }
});

// Ensure compatibility with MetaMask's chain and account changes
if (window.ethereum) {
    window.ethereum.on('accountsChanged', (accounts) => {
        console.log('Accounts changed:', accounts);
    });

    window.ethereum.on('chainChanged', (chainId) => {
        console.log('Chain changed to:', chainId);
    });
}
```

### Notes:
1. Replace `contractAddress` with your actual smart contract address.
2. Replace `yourReadOnlyFunction` and `yourWriteFunction` with the actual function names from your smart contract.
3. Install required dependencies (`npm install web3`) and ensure your project includes the smart contract's ABI (`contractABI.json`).
