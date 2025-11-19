"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: How can I integrate DOP into an EVM-compatible dApp to ensure compliance through selective transparency? Provide sample code.
Generated: DETERMINISTIC_cb4ae327dbbe367c
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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
// DOP (Data Ownership Protocol) integration with EVM-compatible dApp
// Using Web3.js library for Ethereum interactions

const Web3 = require('web3');
const { DOP } = require('./dop-sdk'); // Assuming DOP SDK is implemented in dop-sdk.js

/**
 * DOP integration class for EVM-compatible dApps
 */
class DOPIntegrator {
  /**
   * Initialize DOP integrator with Web3 provider and DOP SDK
   * @param {string} providerUrl - Ethereum node provider URL
   * @param {string} dopContractAddress - DOP contract address
   */
  constructor(providerUrl, dopContractAddress) {
    this.web3 = new Web3(providerUrl);
    this.dopContractAddress = dopContractAddress;
    this.dopContract = new this.web3.eth.Contract(DOP.abi, dopContractAddress);
  }

  /**
   * Register a new user with DOP
   * @param {string} userAddress - User's Ethereum address
   * @param {string} userData - User's data (e.g., IPFS hash)
   * @returns {Promise<string>} Transaction hash
   */
  async registerUser(userAddress, userData) {
    try {
      const tx = await this.dopContract.methods.registerUser(userData).send({ from: userAddress });
      return tx.transactionHash;
    } catch (error) {
      console.error('Error registering user:', error);
      throw error;
    }
  }

  /**
   * Grant selective transparency for a user's data
   * @param {string} userAddress - User's Ethereum address
   * @param {string} granteeAddress - Address of grantee (e.g., auditor)
   * @param {string} dataId - ID of data to grant access to
   * @returns {Promise<string>} Transaction hash
   */
  async grantTransparency(userAddress, granteeAddress, dataId) {
    try {
      const tx = await this.dopContract.methods.grantTransparency(dataId, granteeAddress).send({ from: userAddress });
      return tx.transactionHash;
    } catch (error) {
      console.error('Error granting transparency:', error);
      throw error;
    }
  }

  /**
   * Revoke selective transparency for a user's data
   * @param {string} userAddress - User's Ethereum address
   * @param {string} granteeAddress - Address of grantee (e.g., auditor)
   * @param {string} dataId - ID of data to revoke access to
   * @returns {Promise<string>} Transaction hash
   */
  async revokeTransparency(userAddress, granteeAddress, dataId) {
    try {
      const tx = await this.dopContract.methods.revokeTransparency(dataId, granteeAddress).send({ from: userAddress });
      return tx.transactionHash;
    } catch (error) {
      console.error('Error revoking transparency:', error);
      throw error;
    }
  }

  /**
   * Check if a user has granted transparency for a specific data ID
   * @param {string} userAddress - User's Ethereum address
   * @param {string} granteeAddress - Address of grantee (e.g., auditor)
   * @param {string} dataId - ID of data to check
   * @returns {Promise<boolean>} Whether transparency is granted
   */
  async hasTransparency(userAddress, granteeAddress, dataId) {
    try {
      const result = await this.dopContract.methods.hasTransparency(dataId, granteeAddress).call({ from: userAddress });
      return result;
    } catch (error) {
      console.error('Error checking transparency:', error);
      throw error;
    }
  }
}

// Example usage:
const integrator = new DOPIntegrator('https://mainnet.infura.io/v3/YOUR_PROJECT_ID', '0xDOP_CONTRACT_ADDRESS');

// Register a new user
integrator.registerUser('0xUSER_ADDRESS', 'ipfs://user_data')
  .then((txHash) => console.log('User registered:', txHash))
  .catch((error) => console.error('Error registering user:', error));

// Grant selective transparency
integrator.grantTransparency('0xUSER_ADDRESS', '0xGRANTEE_ADDRESS', 'data_id_123')
  .then((txHash) => console.log('Transparency granted:', txHash))
  .catch((error) => console.error('Error granting transparency:', error));

// Check if transparency is granted
integrator.hasTransparency('0xUSER_ADDRESS', '0xGRANTEE_ADDRESS', 'data_id_123')
  .then((result) => console.log('Transparency granted:', result))
  .catch((error) => console.error('Error checking transparency:', error));
```
