"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda-io.web.app
Prompt: Generate code in JavaScript to connect a user's MetaMask wallet to a decentralized application, allowing real-time token balance updates similar to the $MEDA ecosystem.
Generated: DETERMINISTIC_b89c30fa8ced0478
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';

// Global variables
let web3;
let userAccount;

// Function to initialize Web3 and connect MetaMask
async function initWeb3() {
    // Check if the browser has MetaMask installed
    if (window.ethereum) {
        // Create a Web3 instance
        web3 = new Web3(window.ethereum);
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Set the user's account
            userAccount = (await web3.eth.getAccounts())[0];
            console.log(`Connected account: ${userAccount}`);
        } catch (error) {
            console.error('User denied account access or there was an error:', error);
            alert('Please allow access to your MetaMask account.');
        }
    } else {
        alert('MetaMask is not installed. Please install it to use this application.');
    }
}

// Function to get the token balance
async function getTokenBalance(tokenAddress) {
    const contractABI = [
        // Minimal ABI to get the balance of an ERC20 token
        {
            "constant": true,
            "inputs": [{ "name": "_owner", "type": "address" }],
            "name": "balanceOf",
            "outputs": [{ "name": "balance", "type": "uint256" }],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ];
    
    // Create a token contract instance
    const tokenContract = new web3.eth.Contract(contractABI, tokenAddress);
    
    try {
        // Call the balanceOf function
        const balance = await tokenContract.methods.balanceOf(userAccount).call();
        // Convert the balance from Wei to Ether (assuming the token has 18 decimals)
        const balanceInEther = web3.utils.fromWei(balance, 'ether');
        console.log(`Token balance for ${userAccount}: ${balanceInEther}`);
        return balanceInEther;
    } catch (error) {
        console.error('Error fetching token balance:', error);
        alert('Error fetching token balance. Please try again later.');
    }
}

// Function to update balance in real-time
async function updateBalance(tokenAddress) {
    // Fetch the balance and update the UI accordingly
    const balance = await getTokenBalance(tokenAddress);
    document.getElementById('tokenBalance').innerText = `Balance: ${balance} Tokens`;
}

// Event listener for account changes
window.ethereum.on('accountsChanged', async (accounts) => {
    if (accounts.length > 0) {
        userAccount = accounts[0];
        console.log(`Account changed to: ${userAccount}`);
        // Update the balance whenever the account changes
        await updateBalance('<YOUR_TOKEN_ADDRESS_HERE>');
    } else {
        console.log('Please connect to MetaMask.');
    }
});

// Call the initWeb3 function to set everything up when the window loads
window.onload = async () => {
    await initWeb3();
    // Replace with your token address
    const tokenAddress = '<YOUR_TOKEN_ADDRESS_HERE>';
    await updateBalance(tokenAddress);
    
    // Set an interval to update the balance every 30 seconds
    setInterval(() => updateBalance(tokenAddress), 30000);
};
```

**Note:** Replace `<YOUR_TOKEN_ADDRESS_HERE>` with the actual token address you want to fetch the balance for.
