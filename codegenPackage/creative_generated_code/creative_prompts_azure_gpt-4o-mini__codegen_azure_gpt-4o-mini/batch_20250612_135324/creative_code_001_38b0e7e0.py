"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskloghin.gitbook.io
Prompt: Write a code snippet that demonstrates how to interact with a decentralized application (DApp) using MetaMask.
Generated: DETERMINISTIC_38b0e7e086490248
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';

// Check if MetaMask is installed in the browser
if (typeof window.ethereum === 'undefined') {
    alert('Please install MetaMask to use this DApp.');
} else {
    // Create a new instance of Web3 using MetaMask's provider
    const web3 = new Web3(window.ethereum);

    // Asynchronous function to initialize the DApp
    const initDApp = async () => {
        try {
            // Request account access from the user
            await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Get the user's Ethereum account address
            const accounts = await web3.eth.getAccounts();
            const userAddress = accounts[0];
            console.log(`Connected account: ${userAddress}`);

            // Example of getting the current Ethereum network ID
            const networkId = await web3.eth.net.getId();
            console.log(`Connected to network ID: ${networkId}`);
        } catch (error) {
            // Handle errors related to account access and other issues
            console.error('Error connecting to MetaMask:', error);
            alert('Error connecting to MetaMask. Check the console for details.');
        }
    };

    // Call the initDApp function when the window loads
    window.onload = initDApp;

    // Example function to send Ether
    const sendEther = async (toAddress, amount) => {
        try {
            // Ensure the amount is in Wei (1 Ether = 10^18 Wei)
            const weiAmount = web3.utils.toWei(amount.toString(), 'ether');

            // Send the transaction
            const transactionHash = await web3.eth.sendTransaction({
                from: (await web3.eth.getAccounts())[0], // Get the user's address
                to: toAddress,
                value: weiAmount,
            });

            console.log(`Transaction successful with hash: ${transactionHash.transactionHash}`);
        } catch (error) {
            // Handle errors related to the transaction
            console.error('Error sending Ether:', error);
            alert('Error sending Ether. Check the console for details.');
        }
    };

    // Example usage of sendEther function
    // Uncomment the following line to test sending Ether (replace with a valid address and amount)
    // sendEther('0xRecipientAddressHere', 0.01);
}
```
