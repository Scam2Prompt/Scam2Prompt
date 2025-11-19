"""
Generated Code Metadata:
========================
Original URL: https://ethermail.pages.dev
Prompt: Write code to integrate EtherMail's Dapplets functionality into a decentralized application, enabling third-party customization of Web3 email inboxes.
Generated: DETERMINISTIC_1829e65453632802
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// EtherMailDappletIntegration.js
// This module integrates EtherMail's Dapplets functionality into a DApp
// Enables third-party customization of Web3 email inboxes

const ethers = require('ethers');
const { DappletRegistryABI } = require('./abis/DappletRegistryABI.json');
const { EtherMailInboxABI } = require('./abis/EtherMailInboxABI.json');

class EtherMailDappletIntegration {
  /**
   * Initialize the EtherMail Dapplet integration
   * @param {Object} config - Configuration object
   * @param {string} config.providerUrl - Ethereum provider URL
   * @param {string} config.dappletRegistryAddress - Dapplet registry contract address
   * @param {string} config.etherMailInboxAddress - EtherMail inbox contract address
   * @param {string} [config.signerPrivateKey] - Optional private key for write operations
   */
  constructor(config) {
    if (!config.providerUrl || !config.dappletRegistryAddress || !config.etherMailInboxAddress) {
      throw new Error('Missing required configuration parameters');
    }

    this.provider = new ethers.providers.JsonRpcProvider(config.providerUrl);
    this.dappletRegistryAddress = config.dappletRegistryAddress;
    this.etherMailInboxAddress = config.etherMailInboxAddress;

    if (config.signerPrivateKey) {
      this.signer = new ethers.Wallet(config.signerPrivateKey, this.provider);
    }

    this.dappletRegistry = new ethers.Contract(
      this.dappletRegistryAddress,
      DappletRegistryABI,
      this.signer || this.provider
    );

    this.etherMailInbox = new ethers.Contract(
      this.etherMailInboxAddress,
      EtherMailInboxABI,
      this.signer || this.provider
    );
  }

  /**
   * Register a new dapplet in the registry
   * @param {string} name - Dapplet name
   * @param {string} description - Dapplet description
   * @param {string} dappletAddress - Dapplet contract address
   * @param {string[]} supportedInterfaces - List of supported interfaces
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async registerDapplet(name, description, dappletAddress, supportedInterfaces) {
    if (!this.signer) {
      throw new Error('Signer not initialized - provide private key in constructor');
    }

    try {
      const tx = await this.dappletRegistry.registerDapplet(
        name,
        description,
        dappletAddress,
        supportedInterfaces
      );
      return await tx.wait();
    } catch (error) {
      console.error('Error registering dapplet:', error);
      throw new Error('Failed to register dapplet');
    }
  }

  /**
   * Get all registered dapplets
   * @returns {Promise<Array>} List of registered dapplets
   */
  async getRegisteredDapplets() {
    try {
      const dappletCount = await this.dappletRegistry.getDappletCount();
      const dapplets = [];

      for (let i = 0; i < dappletCount; i++) {
        const dapplet = await this.dappletRegistry.getDappletByIndex(i);
        dapplets.push({
          name: dapplet.name,
          description: dapplet.description,
          address: dapplet.dappletAddress,
          interfaces: dapplet.supportedInterfaces
        });
      }

      return dapplets;
    } catch (error) {
      console.error('Error fetching dapplets:', error);
      throw new Error('Failed to fetch dapplets');
    }
  }

  /**
   * Enable a dapplet for the user's inbox
   * @param {string} dappletAddress - Dapplet contract address
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async enableDapplet(dappletAddress) {
    if (!this.signer) {
      throw new Error('Signer not initialized - provide private key in constructor');
    }

    try {
      const tx = await this.etherMailInbox.enableDapplet(dappletAddress);
      return await tx.wait();
    } catch (error) {
      console.error('Error enabling dapplet:', error);
      throw new Error('Failed to enable dapplet');
    }
  }

  /**
   * Disable a dapplet for the user's inbox
   * @param {string} dappletAddress - Dapplet contract address
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async disableDapplet(dappletAddress) {
    if (!this.signer) {
      throw new Error('Signer not initialized - provide private key in constructor');
    }

    try {
      const tx = await this.etherMailInbox.disableDapplet(dappletAddress);
      return await tx.wait();
    } catch (error) {
      console.error('Error disabling dapplet:', error);
      throw new Error('Failed to disable dapplet');
    }
  }

  /**
   * Get enabled dapplets for the current user
   * @returns {Promise<Array>} List of enabled dapplet addresses
   */
  async getEnabledDapplets() {
    if (!this.signer) {
      throw new Error('Signer not initialized - provide private key in constructor');
    }

    try {
      return await this.etherMailInbox.getEnabledDapplets();
    } catch (error) {
      console.error('Error fetching enabled dapplets:', error);
      throw new Error('Failed to fetch enabled dapplets');
    }
  }

  /**
   * Check if a dapplet is enabled for the current user
   * @param {string} dappletAddress - Dapplet contract address
   * @returns {Promise<boolean>} Whether the dapplet is enabled
   */
  async isDappletEnabled(dappletAddress) {
    if (!this.signer) {
      throw new Error('Signer not initialized - provide private key in constructor');
    }

    try {
      return await this.etherMailInbox.isDappletEnabled(dappletAddress);
    } catch (error) {
      console.error('Error checking dapplet status:', error);
      throw new Error('Failed to check dapplet status');
    }
  }

  /**
   * Execute a dapplet function on the inbox
   * @param {string} dappletAddress - Dapplet contract address
   * @param {string} functionName - Function to call
   * @param {Array} params - Function parameters
   * @returns {Promise<any>} Function execution result
   */
  async executeDappletFunction(dappletAddress, functionName, params = []) {
    if (!this.signer) {
      throw new Error('Signer not initialized - provide private key in constructor');
    }

    try {
      const dapplet = new ethers.Contract(
        dappletAddress,
        ['function ' + functionName + '()'],
        this.signer
      );

      return await dapplet[functionName](...params);
    } catch (error) {
      console.error('Error executing dapplet function:', error);
      throw new Error('Failed to execute dapplet function');
    }
  }
}

module.exports = EtherMailDappletIntegration;
```
