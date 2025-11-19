"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmaskextensio.livejournal.com
Prompt: Can you explain the key features of the MetaMask wallet extension and how it interacts with Ethereum-based dApps?
Generated: DETERMINISTIC_141387b51aa99abd
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MetaMask Interaction Example
 * This script demonstrates how to interact with the MetaMask wallet extension 
 * for Ethereum-based decentralized applications (dApps).
 */

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install it to use this application.");
} else {
    // MetaMask is available
    const provider = window.ethereum;

    // Function to connect to MetaMask
    async function connectMetaMask() {
        try {
            // Request account access if needed
            const accounts = await provider.request({ method: 'eth_requestAccounts' });
            console.log("Connected account:", accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error("User denied account access or error occurred:", error);
        }
    }

    // Function to get account balance
    async function getAccountBalance(account) {
        try {
            const balance = await provider.request({
                method: 'eth_getBalance',
                params: [account, 'latest']
            });
            // Convert balance from Wei to Ether
            return parseFloat(window.web3.utils.fromWei(balance, 'ether')).toFixed(4);
        } catch (error) {
            console.error("Error fetching balance:", error);
        }
    }

    // Function to send Ether
    async function sendEther(fromAccount, toAccount, amount) {
        try {
            const transactionParameters = {
                to: toAccount, // Required: Destination address
                from: fromAccount, // Required: Source address
                value: window.web3.utils.toHex(window.web3.utils.toWei(amount.toString(), 'ether')), // Convert amount to Wei
            };

            // Send the transaction
            const txHash = await provider.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });
            console.log("Transaction successful with hash:", txHash);
        } catch (error) {
            console.error("Transaction failed:", error);
        }
    }

    // Main function to demonstrate usage
    async function main() {
        const account = await connectMetaMask();
        if (account) {
            const balance = await getAccountBalance(account);
            console.log(`Account balance: ${balance} ETH`);

            // Example usage: sending 0.01 ETH to another address
            const recipientAddress = '0xRecipientAddressHere'; // Change to a valid address
            await sendEther(account, recipientAddress, 0.01);
        }
    }

    // Execute the main function
    main();
}
```

Ensure you replace `'0xRecipientAddressHere'` with a valid Ethereum address for testing. Additionally, you should include the Web3 library in your project to utilize `window.web3.utils`.
