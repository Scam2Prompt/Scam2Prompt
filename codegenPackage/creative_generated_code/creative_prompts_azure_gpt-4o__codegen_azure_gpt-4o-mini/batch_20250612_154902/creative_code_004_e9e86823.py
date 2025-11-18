"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://methasenlogiz.gitbook.io
Prompt: Explain how to use MetaMask's API to connect a web application to the Ethereum blockchain and perform basic transactions.
Generated: DETERMINISTIC_e9e86823c8cfd66b
Batch ID: 20250612_154902
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

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error('MetaMask is not installed. Please install MetaMask to use this application.');
} else {
    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    // Function to connect to MetaMask
    async function connectMetaMask() {
        try {
            // Request account access if needed
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Connected account:', accounts[0]);
            return accounts[0]; // Return the connected account
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
            throw new Error('Could not connect to MetaMask');
        }
    }

    // Function to send a transaction
    async function sendTransaction(to, value) {
        try {
            const accounts = await web3.eth.getAccounts();
            const from = accounts[0];

            // Prepare the transaction object
            const transactionParameters = {
                to: to, // The address to send Ether to
                from: from, // The account sending the Ether
                value: web3.utils.toHex(web3.utils.toWei(value.toString(), 'ether')), // Convert value to Wei
            };

            // Send the transaction
            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });

            console.log('Transaction sent! Hash:', txHash);
            return txHash; // Return transaction hash
        } catch (error) {
            console.error('Transaction failed:', error);
            throw new Error('Transaction could not be sent');
        }
    }

    // Example usage
    (async () => {
        const connectedAccount = await connectMetaMask();
        console.log(`Connected account: ${connectedAccount}`);

        // Send a transaction (example: sending 0.01 ETH to a specific address)
        try {
            const txHash = await sendTransaction('0xRecipientAddressHere', 0.01);
            console.log('Transaction Hash:', txHash);
        } catch (error) {
            console.error('Error sending transaction:', error);
        }
    })();
}
```

### Important Notes:
- Replace `'0xRecipientAddressHere'` with the actual Ethereum address you want to send Ether to.
- Ensure that you are running this code in a secure environment with a connected MetaMask wallet.
- This code assumes that the user has configured their MetaMask correctly and has sufficient Ether in their wallet for the transaction.
