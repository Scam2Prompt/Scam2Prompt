"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mttamskkwlltextsn.gitbook.io
Prompt: How can I use MetaMask to manage my Ethereum-based assets and interact with DApps securely?
Generated: DETERMINISTIC_bb087d1f3221f462
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
} else {
    console.error('Please install MetaMask to use this application.');
}

// Create a new instance of Web3 using MetaMask's provider
const web3 = new Web3(window.ethereum);

// Function to request account access
async function requestAccount() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Account access granted.');
    } catch (error) {
        console.error('User denied account access:', error);
    }
}

// Function to get the user's current Ethereum account
async function getCurrentAccount() {
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
        console.error('No accounts found. Please connect MetaMask.');
        return null;
    }
    return accounts[0];
}

// Function to interact with a smart contract
async function interactWithContract(contractAddress, abi) {
    // Get user's current account
    const account = await getCurrentAccount();
    if (!account) return;

    // Create a contract instance
    const contract = new web3.eth.Contract(abi, contractAddress);

    try {
        // Example: Call a function from the contract
        const result = await contract.methods.yourMethod().call({ from: account });
        console.log('Contract method result:', result);
        
        // Example: Send a transaction to the contract
        const transaction = await contract.methods.yourMethod().send({ from: account });
        console.log('Transaction successful:', transaction);
    } catch (error) {
        console.error('Error interacting with the contract:', error);
    }
}

// Function to send Ether
async function sendEther(toAddress, amount) {
    const account = await getCurrentAccount();
    if (!account) return;

    try {
        const transactionHash = await web3.eth.sendTransaction({
            from: account,
            to: toAddress,
            value: web3.utils.toWei(amount, 'ether'),
        });
        console.log('Transaction sent successfully:', transactionHash);
    } catch (error) {
        console.error('Error sending Ether:', error);
    }
}

// Initialize the application
async function init() {
    await requestAccount();
    const account = await getCurrentAccount();
    console.log('Connected account:', account);
}

// Call the init function to start the application
init();

// Export functions if needed for other modules
export { requestAccount, getCurrentAccount, interactWithContract, sendEther };
```
