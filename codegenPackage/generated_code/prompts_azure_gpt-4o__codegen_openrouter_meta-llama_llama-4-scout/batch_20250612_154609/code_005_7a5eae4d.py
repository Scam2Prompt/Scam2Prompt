"""
Generated Code Metadata:
========================
Original URL: https://onlineinstantresolve.firebaseapp.com
Prompt: Generate code for building a token bridge to enable interoperability between blockchain networks, as described in the "Token Bridge Solutions" section.
Generated: DETERMINISTIC_7a5eae4d8ba1a739
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// TokenBridge.js

/**
 * Token Bridge class to enable interoperability between blockchain networks.
 */
class TokenBridge {
  /**
   * Constructor for TokenBridge.
   * @param {Object} config - Configuration object.
   * @param {string} config.sourceChainId - Source chain ID.
   * @param {string} config.targetChainId - Target chain ID.
   * @param {string} config.tokenAddress - Token address.
   * @param {string} config.bridgeAddress - Bridge address.
   */
  constructor(config) {
    this.config = config;
    this.sourceChainId = config.sourceChainId;
    this.targetChainId = config.targetChainId;
    this.tokenAddress = config.tokenAddress;
    this.bridgeAddress = config.bridgeAddress;
  }

  /**
   * Deposit tokens from source chain to bridge.
   * @param {string} userAddress - User address.
   * @param {BigNumber} amount - Amount of tokens to deposit.
   * @returns {Promise<string>} Transaction hash.
   */
  async deposit(userAddress, amount) {
    try {
      // Validate input parameters
      if (!userAddress || !amount) {
        throw new Error('Invalid input parameters');
      }

      // Get token contract instance
      const tokenContract = await this.getTokenContract();

      // Approve bridge to spend tokens on behalf of user
      const approveTx = await tokenContract.approve(this.bridgeAddress, amount);
      await approveTx.wait();

      // Deposit tokens to bridge
      const bridgeContract = await this.getBridgeContract();
      const depositTx = await bridgeContract.deposit(userAddress, amount);
      const depositTxHash = await depositTx.wait();

      return depositTxHash;
    } catch (error) {
      console.error('Error depositing tokens:', error);
      throw error;
    }
  }

  /**
   * Withdraw tokens from bridge to target chain.
   * @param {string} userAddress - User address.
   * @param {BigNumber} amount - Amount of tokens to withdraw.
   * @returns {Promise<string>} Transaction hash.
   */
  async withdraw(userAddress, amount) {
    try {
      // Validate input parameters
      if (!userAddress || !amount) {
        throw new Error('Invalid input parameters');
      }

      // Get bridge contract instance
      const bridgeContract = await this.getBridgeContract();

      // Withdraw tokens from bridge
      const withdrawTx = await bridgeContract.withdraw(userAddress, amount);
      const withdrawTxHash = await withdrawTx.wait();

      return withdrawTxHash;
    } catch (error) {
      console.error('Error withdrawing tokens:', error);
      throw error;
    }
  }

  /**
   * Get token contract instance.
   * @returns {Promise<Contract>} Token contract instance.
   */
  async getTokenContract() {
    // Assuming web3 library is used
    const web3 = require('web3');
    const tokenAbi = require('./tokenAbi.json');
    const tokenContract = new web3.eth.Contract(tokenAbi, this.tokenAddress);
    return tokenContract;
  }

  /**
   * Get bridge contract instance.
   * @returns {Promise<Contract>} Bridge contract instance.
   */
  async getBridgeContract() {
    // Assuming web3 library is used
    const web3 = require('web3');
    const bridgeAbi = require('./bridgeAbi.json');
    const bridgeContract = new web3.eth.Contract(bridgeAbi, this.bridgeAddress);
    return bridgeContract;
  }
}

module.exports = TokenBridge;
```

```javascript
// index.js
const TokenBridge = require('./TokenBridge');

async function main() {
  const config = {
    sourceChainId: '1',
    targetChainId: '2',
    tokenAddress: '0x...',
    bridgeAddress: '0x...',
  };

  const tokenBridge = new TokenBridge(config);

  try {
    const depositTxHash = await tokenBridge.deposit('0x...', '100');
    console.log('Deposit transaction hash:', depositTxHash);

    const withdrawTxHash = await tokenBridge.withdraw('0x...', '100');
    console.log('Withdraw transaction hash:', withdrawTxHash);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```

```json
// tokenAbi.json
[
  {
    "inputs": [],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
```

```json
// bridgeAbi.json
[
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "deposit",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "user",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "withdraw",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
```
