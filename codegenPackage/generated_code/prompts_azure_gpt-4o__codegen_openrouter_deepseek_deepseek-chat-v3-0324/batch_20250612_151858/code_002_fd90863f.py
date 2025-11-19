"""
Generated Code Metadata:
========================
Original URL: https://launchpad.seedify.de
Prompt: Generate code to interact with a launchpad's smart contract using Web3.js, including functions for token purchase and user balance retrieval.
Generated: DETERMINISTIC_fd90863f1a3bc7e7
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const Web3 = require('web3');
const { abi } = require('./LaunchpadABI.json'); // Replace with actual ABI path

class LaunchpadInteraction {
    /**
     * Initializes the LaunchpadInteraction class with Web3 provider and contract details.
     * @param {string} providerUrl - The Web3 provider URL (e.g., Infura, Alchemy)
     * @param {string} contractAddress - The smart contract address
     * @param {string} privateKey - The private key for transactions (optional for read-only)
     */
    constructor(providerUrl, contractAddress, privateKey = null) {
        this.web3 = new Web3(providerUrl);
        this.contractAddress = contractAddress;
        this.contract = new this.web3.eth.Contract(abi, contractAddress);
        
        if (privateKey) {
            this.account = this.web3.eth.accounts.privateKeyToAccount(privateKey);
            this.web3.eth.accounts.wallet.add(this.account);
            this.web3.eth.defaultAccount = this.account.address;
        }
    }

    /**
     * Gets the token balance of a specific address.
     * @param {string} address - The address to check balance for
     * @returns {Promise<string>} The token balance in wei
     */
    async getTokenBalance(address) {
        try {
            const balance = await this.contract.methods.balanceOf(address).call();
            return this.web3.utils.fromWei(balance, 'ether');
        } catch (error) {
            console.error('Error getting token balance:', error);
            throw error;
        }
    }

    /**
     * Gets the native currency (ETH/BNB/etc) balance of a specific address.
     * @param {string} address - The address to check balance for
     * @returns {Promise<string>} The balance in wei
     */
    async getNativeBalance(address) {
        try {
            const balance = await this.web3.eth.getBalance(address);
            return this.web3.utils.fromWei(balance, 'ether');
        } catch (error) {
            console.error('Error getting native balance:', error);
            throw error;
        }
    }

    /**
     * Purchases tokens from the launchpad.
     * @param {string} amount - The amount of native currency to spend (in ether)
     * @returns {Promise<object>} The transaction receipt
     */
    async purchaseTokens(amount) {
        if (!this.account) {
            throw new Error('Private key not provided. Cannot send transactions.');
        }

        try {
            const weiAmount = this.web3.utils.toWei(amount, 'ether');
            const gasEstimate = await this.contract.methods.buyTokens().estimateGas({
                from: this.account.address,
                value: weiAmount
            });

            const tx = {
                from: this.account.address,
                to: this.contractAddress,
                value: weiAmount,
                gas: gasEstimate,
                data: this.contract.methods.buyTokens().encodeABI()
            };

            const signedTx = await this.web3.eth.accounts.signTransaction(
                tx,
                this.account.privateKey
            );

            const receipt = await this.web3.eth.sendSignedTransaction(
                signedTx.rawTransaction
            );

            return receipt;
        } catch (error) {
            console.error('Error purchasing tokens:', error);
            throw error;
        }
    }

    /**
     * Gets the current token price from the contract.
     * @returns {Promise<string>} The token price in native currency
     */
    async getTokenPrice() {
        try {
            const price = await this.contract.methods.tokenPrice().call();
            return this.web3.utils.fromWei(price, 'ether');
        } catch (error) {
            console.error('Error getting token price:', error);
            throw error;
        }
    }

    /**
     * Checks if the launchpad sale is active.
     * @returns {Promise<boolean>} True if sale is active, false otherwise
     */
    async isSaleActive() {
        try {
            return await this.contract.methods.saleActive().call();
        } catch (error) {
            console.error('Error checking sale status:', error);
            throw error;
        }
    }
}

module.exports = LaunchpadInteraction;
```
