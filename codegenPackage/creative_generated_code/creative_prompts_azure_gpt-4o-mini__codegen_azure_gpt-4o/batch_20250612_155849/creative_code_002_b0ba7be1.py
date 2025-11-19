"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockappsnode.com
Prompt: Can you provide code examples for integrating multichain functionality in a DApp based on the guidelines from blockappsnode.com?
Generated: DETERMINISTIC_b0ba7be15ee3c3dd
Batch ID: 20250612_155849
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/<INFURA_PROJECT_ID>": {
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
const ethers = require('ethers');

// Configuration for Multichain Integration
const chains = {
  ethereum: {
    rpcUrl: 'https://mainnet.infura.io/v3/<INFURA_PROJECT_ID>',
    chainId: 1,
    name: 'Ethereum Mainnet',
  },
  polygon: {
    rpcUrl: 'https://polygon-rpc.com/',
    chainId: 137,
    name: 'Polygon Mainnet',
  },
  binanceSmartChain: {
    rpcUrl: 'https://bsc-dataseed.binance.org/',
    chainId: 56,
    name: 'Binance Smart Chain Mainnet',
  },
};

// Initialize a connection to each chain
const web3Instances = {};
Object.keys(chains).forEach((chainKey) => {
  const chain = chains[chainKey];
  web3Instances[chainKey] = new Web3(new Web3.providers.HttpProvider(chain.rpcUrl));
});

// Function to fetch account balance across chains
async function getBalanceAcrossChains(address) {
  try {
    const balances = {};
    for (const chainKey of Object.keys(web3Instances)) {
      const web3 = web3Instances[chainKey];
      const chainInfo = chains[chainKey];

      // Fetch the balance (converted to Ether) for the given address
      const balanceWei = await web3.eth.getBalance(address);
      balances[chainInfo.name] = web3.utils.fromWei(balanceWei, 'ether');
    }
    return balances;
  } catch (error) {
    console.error('Error fetching balances:', error);
    throw new Error('Failed to fetch balance across chains');
  }
}

// Function to send a transaction on a specified chain
async function sendTransaction(chainKey, privateKey, toAddress, valueInEther) {
  try {
    const web3 = web3Instances[chainKey];
    const chainInfo = chains[chainKey];
    const account = web3.eth.accounts.privateKeyToAccount(privateKey);

    // Set up the transaction object
    const tx = {
      from: account.address,
      to: toAddress,
      value: web3.utils.toWei(valueInEther, 'ether'),
      gas: 21000, // Standard gas limit for a simple transfer
      chainId: chainInfo.chainId,
    };

    // Sign the transaction with the private key
    const signedTx = await account.signTransaction(tx);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Transaction sent successfully:', receipt.transactionHash);

    return receipt;
  } catch (error) {
    console.error('Error sending transaction:', error);
    throw new Error('Failed to send transaction');
  }
}

// Example usage
(async () => {
  const testAddress = '0xYourWalletAddressHere';
  const privateKey = '0xYourPrivateKeyHere';
  const recipientAddress = '0xRecipientAddressHere';
  const valueToSend = '0.01'; // 0.01 Ether

  try {
    // Get balance across chains for the test address
    const balances = await getBalanceAcrossChains(testAddress);
    console.log('Balances:', balances);

    // Send a transaction on Ethereum mainnet
    const receipt = await sendTransaction('ethereum', privateKey, recipientAddress, valueToSend);
    console.log('Transaction receipt:', receipt);
  } catch (error) {
    console.error('Error in example usage:', error.message);
  }
})();
```

Make sure to replace placeholders like `<INFURA_PROJECT_ID>`, `0xYourWalletAddressHere`, `0xYourPrivateKeyHere`, and `0xRecipientAddressHere` with actual values.
