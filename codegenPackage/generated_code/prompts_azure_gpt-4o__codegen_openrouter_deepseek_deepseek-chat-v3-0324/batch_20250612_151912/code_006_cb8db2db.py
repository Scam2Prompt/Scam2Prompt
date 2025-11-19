"""
Generated Code Metadata:
========================
Original URL: https://tron-presents.blogspot.com
Prompt: Create a JavaScript function to integrate Tron-based token payments into a web application using TronWeb.
Generated: DETERMINISTIC_cb8db2db67038bba
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * TronPaymentHandler - A utility class to handle Tron-based token payments using TronWeb.
 */
class TronPaymentHandler {
  /**
   * Initializes the TronPaymentHandler with TronWeb configuration.
   * @param {Object} config - Configuration object
   * @param {string} config.network - Tron network ('mainnet', 'shasta', 'nile')
   * @param {string} config.contractAddress - TRC20 token contract address
   * @param {string} [config.privateKey] - Optional private key for server-side operations
   */
  constructor(config) {
    if (!window.tronWeb) {
      throw new Error('TronWeb is not available. Please ensure TronLink is installed or TronWeb is properly initialized.');
    }

    this.tronWeb = window.tronWeb;
    this.contractAddress = config.contractAddress;
    this.privateKey = config.privateKey;
    this.network = config.network;

    this.validateNetwork();
    this.initializeContract();
  }

  /**
   * Validates that the current network matches the configured network.
   * @throws {Error} If network doesn't match
   */
  validateNetwork() {
    const currentNetwork = this.tronWeb.fullNode.host.includes('shasta') ? 'shasta' 
      : this.tronWeb.fullNode.host.includes('nile') ? 'nile' 
      : 'mainnet';

    if (currentNetwork !== this.network) {
      throw new Error(`Network mismatch. Expected ${this.network} but connected to ${currentNetwork}`);
    }
  }

  /**
   * Initializes the TRC20 contract instance.
   */
  initializeContract() {
    try {
      this.contract = this.tronWeb.contract().at(this.contractAddress);
    } catch (error) {
      throw new Error(`Failed to initialize contract: ${error.message}`);
    }
  }

  /**
   * Gets the current user's Tron address.
   * @returns {Promise<string>} The user's Tron address
   */
  async getCurrentUserAddress() {
    try {
      const address = await this.tronWeb.defaultAddress.base58;
      if (!address) throw new Error('No address available');
      return address;
    } catch (error) {
      throw new Error(`Failed to get user address: ${error.message}`);
    }
  }

  /**
   * Gets the token balance for a given address.
   * @param {string} address - Tron address to check balance for
   * @returns {Promise<number>} Token balance
   */
  async getTokenBalance(address) {
    try {
      const balance = await this.contract.balanceOf(address).call();
      return this.tronWeb.fromSun(balance);
    } catch (error) {
      throw new Error(`Failed to get token balance: ${error.message}`);
    }
  }

  /**
   * Initiates a token transfer.
   * @param {string} toAddress - Recipient address
   * @param {number} amount - Amount to send (in tokens, not SUN)
   * @returns {Promise<string>} Transaction ID
   */
  async sendTokens(toAddress, amount) {
    try {
      if (!this.tronWeb.isAddress(toAddress)) {
        throw new Error('Invalid recipient address');
      }

      const amountInSun = this.tronWeb.toSun(amount);
      const tx = await this.contract.transfer(toAddress, amountInSun).send();

      return tx;
    } catch (error) {
      throw new Error(`Failed to send tokens: ${error.message}`);
    }
  }

  /**
   * Server-side method to send tokens (requires private key).
   * @param {string} fromAddress - Sender address
   * @param {string} toAddress - Recipient address
   * @param {number} amount - Amount to send (in tokens, not SUN)
   * @returns {Promise<string>} Transaction ID
   */
  async sendTokensServerSide(fromAddress, toAddress, amount) {
    if (!this.privateKey) {
      throw new Error('Private key is required for server-side operations');
    }

    try {
      const amountInSun = this.tronWeb.toSun(amount);
      const signedTx = await this.tronWeb.transactionBuilder.sendToken(
        toAddress,
        amountInSun,
        this.contractAddress,
        fromAddress
      );
      
      const signedTransaction = await this.tronWeb.trx.sign(signedTx, this.privateKey);
      const result = await this.tronWeb.trx.sendRawTransaction(signedTransaction);
      
      return result.txid;
    } catch (error) {
      throw new Error(`Failed to send tokens server-side: ${error.message}`);
    }
  }

  /**
   * Gets transaction details by ID.
   * @param {string} txId - Transaction ID
   * @returns {Promise<Object>} Transaction details
   */
  async getTransactionDetails(txId) {
    try {
      const tx = await this.tronWeb.trx.getTransaction(txId);
      if (!tx) throw new Error('Transaction not found');
      return tx;
    } catch (error) {
      throw new Error(`Failed to get transaction details: ${error.message}`);
    }
  }

  /**
   * Listens for token transfer events to a specific address.
   * @param {string} address - Address to watch
   * @param {Function} callback - Callback function when event occurs
   * @returns {Function} Function to unsubscribe from events
   */
  watchTokenTransfers(address, callback) {
    if (!this.tronWeb.isAddress(address)) {
      throw new Error('Invalid address to watch');
    }

    const eventHandler = this.contract.Transfer().watch((err, event) => {
      if (err) {
        console.error('Error watching transfers:', err);
        return;
      }

      if (event.result.to === address) {
        callback(event);
      }
    });

    return () => eventHandler.stop();
  }
}

// Example usage:
// const paymentHandler = new TronPaymentHandler({
//   network: 'mainnet',
//   contractAddress: 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t',
//   privateKey: 'your-private-key' // Only for server-side operations
// });
```
