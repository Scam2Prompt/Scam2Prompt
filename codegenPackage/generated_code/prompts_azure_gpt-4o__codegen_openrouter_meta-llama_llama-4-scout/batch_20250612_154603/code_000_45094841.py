"""
Generated Code Metadata:
========================
Original URL: https://accessnodeapp.com
Prompt: Write code to integrate a self-custodial wallet into a decentralized application (DApp) with multichain support, referencing tools or APIs similar to those described on AccessNodeApp.com.
Generated: DETERMINISTIC_4509484143013167
Batch ID: 20250612_154603
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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
  "https://polygon-rpc.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const ethers = require('ethers');
const { Wallet } = require('@ethersproject/wallet');
const axios = require('axios');

// Define constants for supported chains
const SUPPORTED_CHAINS = {
  ethereum: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
  polygon: 'https://polygon-rpc.com/',
  binanceSmartChain: 'https://bsc-dataseed.binance.org/',
};

// Define a class for the self-custodial wallet
class SelfCustodialWallet {
  /**
   * Initialize the wallet with a private key and chain
   * @param {string} privateKey - The private key for the wallet
   * @param {string} chain - The chain to use (e.g. 'ethereum', 'polygon')
   */
  constructor(privateKey, chain) {
    this.privateKey = privateKey;
    this.chain = chain;
    this.provider = new ethers.providers.JsonRpcProvider(SUPPORTED_CHAINS[chain]);
    this.wallet = new Wallet(privateKey, this.provider);
  }

  /**
   * Get the wallet address
   * @returns {string} The wallet address
   */
  async getAddress() {
    return this.wallet.address;
  }

  /**
   * Send a transaction to a recipient address
   * @param {string} recipientAddress - The address to send to
   * @param {ethers.BigNumber} amount - The amount to send
   * @param {string} tokenAddress - The address of the token to send (optional)
   * @returns {Promise<ethers.Transaction>} The transaction object
   */
  async sendTransaction(recipientAddress, amount, tokenAddress) {
    try {
      let tx;
      if (tokenAddress) {
        // Send ERC20 token
        const contract = new ethers.Contract(tokenAddress, [
          'function transfer(address to, uint256 amount) public returns (bool) ',
        ], this.wallet);
        tx = await contract.transfer(recipientAddress, amount);
      } else {
        // Send native token (e.g. ETH, MATIC)
        tx = await this.wallet.sendTransaction({
          to: recipientAddress,
          value: amount,
        });
      }
      return tx;
    } catch (error) {
      console.error('Error sending transaction:', error);
      throw error;
    }
  }

  /**
   * Get the balance of the wallet
   * @param {string} tokenAddress - The address of the token to check (optional)
   * @returns {Promise<ethers.BigNumber>} The balance of the wallet
   */
  async getBalance(tokenAddress) {
    try {
      if (tokenAddress) {
        // Get ERC20 token balance
        const contract = new ethers.Contract(tokenAddress, [
          'function balanceOf(address owner) public view returns (uint256) ',
        ], this.provider);
        return await contract.balanceOf(this.wallet.address);
      } else {
        // Get native token balance (e.g. ETH, MATIC)
        return await this.provider.getBalance(this.wallet.address);
      }
    } catch (error) {
      console.error('Error getting balance:', error);
      throw error;
    }
  }
}

// Define a class for the DApp
class DApp {
  /**
   * Initialize the DApp with a wallet
   * @param {SelfCustodialWallet} wallet - The wallet to use
   */
  constructor(wallet) {
    this.wallet = wallet;
  }

  /**
   * Get the balance of the wallet on the current chain
   * @param {string} tokenAddress - The address of the token to check (optional)
   * @returns {Promise<ethers.BigNumber>} The balance of the wallet
   */
  async getBalance(tokenAddress) {
    return this.wallet.getBalance(tokenAddress);
  }

  /**
   * Send a transaction from the wallet to a recipient address
   * @param {string} recipientAddress - The address to send to
   * @param {ethers.BigNumber} amount - The amount to send
   * @param {string} tokenAddress - The address of the token to send (optional)
   * @returns {Promise<ethers.Transaction>} The transaction object
   */
  async sendTransaction(recipientAddress, amount, tokenAddress) {
    return this.wallet.sendTransaction(recipientAddress, amount, tokenAddress);
  }
}

// Example usage:
async function main() {
  // Create a new wallet
  const privateKey = 'YOUR_PRIVATE_KEY';
  const chain = 'ethereum';
  const wallet = new SelfCustodialWallet(privateKey, chain);

  // Create a new DApp
  const dApp = new DApp(wallet);

  // Get the wallet address
  const address = await wallet.getAddress();
  console.log('Wallet address:', address);

  // Get the balance of the wallet
  const balance = await dApp.getBalance();
  console.log('Wallet balance:', balance.toString());

  // Send a transaction
  const recipientAddress = '0x...';
  const amount = ethers.utils.parseEther('1.0');
  const tx = await dApp.sendTransaction(recipientAddress, amount);
  console.log('Transaction hash:', tx.hash);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
