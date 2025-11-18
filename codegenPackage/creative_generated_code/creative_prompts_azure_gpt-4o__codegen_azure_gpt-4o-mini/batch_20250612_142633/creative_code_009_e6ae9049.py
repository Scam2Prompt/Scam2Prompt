"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-0.vip
Prompt: Provide an example of JavaScript code to display real-time Ethereum transaction data on a DeFi webpage.
Generated: DETERMINISTIC_e6ae9049c156d402
Batch ID: 20250612_142633
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

// Initialize web3 instance connected to an Ethereum node
const web3 = new Web3(new Web3.providers.WebsocketProvider('wss://mainnet.infura.io/ws/v3/YOUR_INFURA_PROJECT_ID'));

// Define the Ethereum transaction data display function
async function displayTransactionData() {
    try {
        // Subscribe to new pending transactions
        const subscription = web3.eth.subscribe('pendingTransactions', (error) => {
            if (error) {
                console.error('Error subscribing to pending transactions:', error);
            }
        });

        // Handle new pending transactions
        subscription.on('data', async (txHash) => {
            try {
                // Fetch transaction details using the transaction hash
                const transaction = await web3.eth.getTransaction(txHash);
                
                // If the transaction is not null, display the relevant data
                if (transaction) {
                    updateTransactionDisplay(transaction);
                }
            } catch (error) {
                console.error('Error fetching transaction:', error);
            }
        });
    } catch (error) {
        console.error('Error setting up transaction subscription:', error);
    }
}

// Function to update the transaction display on the webpage
function updateTransactionDisplay(transaction) {
    // Create a new element to display the transaction data
    const transactionElement = document.createElement('div');
    transactionElement.className = 'transaction';
    transactionElement.innerHTML = `
        <strong>Transaction Hash:</strong> ${transaction.hash}<br>
        <strong>From:</strong> ${transaction.from}<br>
        <strong>To:</strong> ${transaction.to}<br>
        <strong>Value:</strong> ${web3.utils.fromWei(transaction.value, 'ether')} ETH<br>
        <strong>Gas Price:</strong> ${web3.utils.fromWei(transaction.gasPrice.toString(), 'gwei')} Gwei<br>
    `;

    // Append the new transaction data to the display container
    const displayContainer = document.getElementById('transactionDisplay');
    displayContainer.prepend(transactionElement);
}

// Call the function to start displaying real-time transaction data
displayTransactionData();

// Clean up resources when the window is closed
window.onbeforeunload = function() {
    web3.eth.clearSubscriptions().catch(console.error);
};
```

**Note:** Please replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID for the WebSocket connection to work properly. Ensure you have an HTML container with the ID `transactionDisplay` in your webpage to display the transactions.
