"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-wallet.ru
Prompt: Write a script to automate the process of exporting transaction history from a MetaMask wallet using its API or browser extension features.
Generated: DETERMINISTIC_c1962aa7060e4260
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Script to export transaction history from a MetaMask wallet.
 * Note: MetaMask does not provide an official API to directly export transaction history.
 * This script interacts with Ethereum blockchain using Web3.js to fetch transactions.
 * MetaMask needs to be installed and the user must grant access to the connected wallet.
 */

// Import Web3.js
const Web3 = require('web3');

// Initialize Web3 instance using MetaMask's injected provider
if (typeof window.ethereum !== 'undefined') {
  const web3 = new Web3(window.ethereum);

  (async () => {
    try {
      // Request account access from user
      await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Get the wallet address of the user
      const accounts = await web3.eth.getAccounts();
      const walletAddress = accounts[0];
      console.log(`Connected wallet: ${walletAddress}`);

      // Fetch transaction history for the wallet
      const fetchTransactionHistory = async (address, startBlock = 0, endBlock = 'latest') => {
        const currentBlock = await web3.eth.getBlockNumber();
        const endBlockNumber = endBlock === 'latest' ? currentBlock : endBlock;
        const transactions = [];

        console.log(`Fetching transactions for ${address} from block ${startBlock} to ${endBlockNumber}...`);

        for (let i = startBlock; i <= endBlockNumber; i++) {
          const block = await web3.eth.getBlock(i, true); // Fetch block details with transactions

          if (block && block.transactions) {
            block.transactions.forEach((tx) => {
              if (tx.from === address || tx.to === address) {
                transactions.push(tx);
              }
            });
          }
        }

        return transactions;
      };

      // Set the block range for transaction search (adjust as needed)
      const startBlock = 0; // Start from beginning of the blockchain
      const endBlock = 'latest'; // Up to the most recent block

      const transactions = await fetchTransactionHistory(walletAddress, startBlock, endBlock);

      // Export transaction history to a JSON file
      const fs = require('fs');
      const fileName = `transaction_history_${walletAddress}.json`;

      fs.writeFileSync(fileName, JSON.stringify(transactions, null, 2));

      console.log(`Transaction history exported successfully to ${fileName}`);
    } catch (error) {
      console.error(`Error: ${error.message}`);
    }
  })();
} else {
  console.error('MetaMask is not installed. Please install MetaMask and try again.');
}
```

### Notes:
1. This script assumes you have MetaMask installed in your browser and that you are running it in a Node.js environment or a web app capable of interacting with MetaMask.
2. Install dependencies using `npm install web3` and `npm install fs` before running the script.
3. Browser-based script execution may require bundling tools such as `webpack`.
4. Adjust the block range (`startBlock` and `endBlock`) for transaction search based on your requirements.
5. Ensure the user manually connects their MetaMask wallet before running this script.
