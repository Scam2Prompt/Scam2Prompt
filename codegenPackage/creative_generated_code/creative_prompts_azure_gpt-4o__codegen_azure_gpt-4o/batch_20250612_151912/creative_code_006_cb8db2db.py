"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-presents.blogspot.com
Prompt: Create a JavaScript function to integrate Tron-based token payments into a web application using TronWeb.
Generated: DETERMINISTIC_cb8db2db67038bba
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.trongrid.io": {
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
// Import TronWeb library
const TronWeb = require('tronweb');

/**
 * Initializes TronWeb instance with credentials.
 * @param {string} fullNode - URL of the full node.
 * @param {string} solidityNode - URL of the solidity node.
 * @param {string} eventServer - URL of the event server.
 * @param {string} privateKey - Wallet private key for signing transactions.
 * @returns {TronWeb} - Instance of TronWeb.
 */
function initializeTronWeb(fullNode, solidityNode, eventServer, privateKey) {
  if (!fullNode || !solidityNode || !eventServer || !privateKey) {
    throw new Error('All parameters are required to initialize TronWeb.');
  }

  return new TronWeb(fullNode, solidityNode, eventServer, privateKey);
}

/**
 * Sends TRC-20 token payment from sender to recipient.
 * @param {TronWeb} tronWeb - TronWeb instance.
 * @param {string} tokenContractAddress - TRC-20 token contract address.
 * @param {string} senderAddress - Sender's Tron address.
 * @param {string} recipientAddress - Recipient's Tron address.
 * @param {number} amount - Amount of tokens to send (in smallest unit of the token).
 * @returns {Promise<string>} - Transaction ID (txID) on success.
 */
async function sendTokenPayment(tronWeb, tokenContractAddress, senderAddress, recipientAddress, amount) {
  if (!tronWeb || !tokenContractAddress || !senderAddress || !recipientAddress || !amount) {
    throw new Error('All parameters are required to send token payment.');
  }

  try {
    // Ensure recipient address is in valid format
    const validRecipientAddress = tronWeb.address.toHex(recipientAddress);

    // Interact with TRC-20 smart contract
    const contractInstance = await tronWeb.contract().at(tokenContractAddress);

    // Trigger the transfer method
    const transaction = await contractInstance.transfer(validRecipientAddress, amount).send({
      from: senderAddress,
    });

    // Return transaction ID
    return transaction;
  } catch (error) {
    console.error('Error occurred while sending token payment:', error);
    throw new Error('Failed to send token payment.');
  }
}

/**
 * Example usage of TronWeb and sendTokenPayment.
 */
(async () => {
  try {
    // Configuration
    const fullNode = 'https://api.trongrid.io';
    const solidityNode = 'https://api.trongrid.io';
    const eventServer = 'https://api.trongrid.io';
    const privateKey = 'your-private-key-here'; // Replace with your wallet's private key

    const tokenContractAddress = 'your-token-contract-address-here'; // Replace with TRC-20 token contract address
    const senderAddress = 'your-sender-address-here'; // Replace with your Tron address
    const recipientAddress = 'recipient-address-here'; // Replace with recipient Tron address
    const amount = 1000; // Replace with token amount to send (in smallest unit)

    // Initialize TronWeb instance
    const tronWeb = initializeTronWeb(fullNode, solidityNode, eventServer, privateKey);

    // Send token payment
    const txID = await sendTokenPayment(tronWeb, tokenContractAddress, senderAddress, recipientAddress, amount);
    console.log('Payment successful. Transaction ID:', txID);
  } catch (error) {
    console.error('Error during payment process:', error);
  }
})();
```
