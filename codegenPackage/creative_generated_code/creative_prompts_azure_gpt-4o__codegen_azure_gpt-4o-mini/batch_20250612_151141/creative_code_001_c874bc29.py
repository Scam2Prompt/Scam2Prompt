"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neirocoin.pages.dev
Prompt: Create a step-by-step guide in JavaScript for connecting a MetaMask wallet to a decentralized exchange (DEX) like Uniswap, as described on the NEIRO webpage.
Generated: DETERMINISTIC_c874bc29d32bf17a
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3'; // Web3.js library for interacting with the Ethereum blockchain

// Initialize a Web3 instance
let web3;

// Function to check if MetaMask is installed
const isMetaMaskInstalled = () => {
    return typeof window.ethereum !== 'undefined';
};

// Function to connect to MetaMask
const connectMetaMask = async () => {
    if (!isMetaMaskInstalled()) {
        alert('Please install MetaMask to use this feature.');
        return;
    }
    
    try {
        // Request account access if needed
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        // Set Web3 provider
        web3 = new Web3(window.ethereum);
        console.log('Connected to MetaMask account:', accounts[0]);
        
        return accounts[0]; // Return the connected account
    } catch (error) {
        console.error('Error connecting to MetaMask:', error);
        alert('Failed to connect to MetaMask. Please try again.');
    }
};

// Function to fetch the DEX contract and interact with it
const interactWithDEX = async (account) => {
    if (!account) {
        console.error('No account provided. Please connect your MetaMask wallet first.');
        return;
    }

    // Example of Uniswap V2 Router contract address (on Ethereum Mainnet)
    const uniswapV2RouterAddress = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6';
    
    // ABI for the Uniswap V2 Router (simplified for demonstration)
    const uniswapV2RouterABI = [
        // Add relevant ABI methods you intend to use
        {
            "constant": true,
            "inputs": [],
            "name": "getAmountsOut",
            "outputs": [
                {
                    "name": "",
                    "type": "uint256[]"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ];

    // Create a contract instance
    const uniswapContract = new web3.eth.Contract(uniswapV2RouterABI, uniswapV2RouterAddress);

    try {
        // Example interaction: Fetching output amounts for a swap (you must pass parameters)
        const amounts = await uniswapContract.methods.getAmountsOut(/*inputAmount, path*/).call();
        console.log('Output amounts for the swap:', amounts);
    } catch (error) {
        console.error('Error interacting with the DEX:', error);
    }
};

// Event listener for the connect button
document.getElementById('connectButton').addEventListener('click', async () => {
    const account = await connectMetaMask();
    await interactWithDEX(account);
});

// Function to ensure that the user is kept aware of network changes
window.ethereum.on('chainChanged', (chainId) => {
    console.log('Network changed to:', chainId);
    // Optionally, you can re-connect or update UI based on the new network
});

// Function to handle account changes
window.ethereum.on('accountsChanged', (accounts) => {
    console.log('Accounts changed:', accounts);
    if (accounts.length === 0) {
        alert('Please connect to MetaMask.');
    } else {
        // Optionally, re-initialize or update the UI with the new account
        interactWithDEX(accounts[0]);
    }
});
```
