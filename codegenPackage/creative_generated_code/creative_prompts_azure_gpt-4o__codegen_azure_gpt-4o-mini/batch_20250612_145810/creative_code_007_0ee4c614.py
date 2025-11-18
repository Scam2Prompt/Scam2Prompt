"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumwalletsnftsyc.pages.dev
Prompt: Provide an example of integrating Ethereum wallet protocols to manage key storage and facilitate global payments, referencing the webpage's focus on digital money and decentralized applications.
Generated: DETERMINISTIC_0ee4c6140aa4ec8f
Batch ID: 20250612_145810
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rinkeby.infura.io/v3/${INFURA_PROJECT_ID}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const HDWalletProvider = require('@truffle/hdwallet-provider');

// Define configuration for the Ethereum network and wallet
const INFURA_PROJECT_ID = 'your_infura_project_id';
const MNEMONIC = 'your_12_or_24_word_mnemonic';

// Initialize Web3 provider using HDWalletProvider
const provider = new HDWalletProvider(MNEMONIC, `https://rinkeby.infura.io/v3/${INFURA_PROJECT_ID}`);
const web3 = new Web3(provider);

/**
 * Function to send Ether from one account to another
 * @param {string} toAddress - The recipient's Ethereum address
 * @param {number} amount - Amount of Ether to send (in Ether)
 */
async function sendEther(toAddress, amount) {
    try {
        // Get the account address from the wallet
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Convert Ether to Wei
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

        // Create and send the transaction
        const transaction = await web3.eth.sendTransaction({
            from: fromAddress,
            to: toAddress,
            value: amountInWei,
        });

        console.log('Transaction successful:', transaction);
    } catch (error) {
        console.error('Error sending Ether:', error);
    }
}

/**
 * Function to get the balance of an Ethereum address
 * @param {string} address - The Ethereum address to check
 * @returns {Promise<string>} - The balance in Ether
 */
async function getBalance(address) {
    try {
        const balanceWei = await web3.eth.getBalance(address);
        const balance = web3.utils.fromWei(balanceWei, 'ether');
        return balance;
    } catch (error) {
        console.error('Error fetching balance:', error);
        return null;
    }
}

// Example usage
(async () => {
    const recipientAddress = 'recipient_ethereum_address'; // Replace with actual recipient address
    const amountToSend = 0.1; // Amount in Ether to send

    // Fetch and log the sender's balance before sending
    const senderAddress = (await web3.eth.getAccounts())[0];
    const senderBalanceBefore = await getBalance(senderAddress);
    console.log(`Sender's balance before: ${senderBalanceBefore} ETH`);

    // Send Ether to the recipient
    await sendEther(recipientAddress, amountToSend);

    // Fetch and log the sender's balance after sending
    const senderBalanceAfter = await getBalance(senderAddress);
    console.log(`Sender's balance after: ${senderBalanceAfter} ETH`);

    // Clean up the provider
    provider.engine.stop();
})();
```
