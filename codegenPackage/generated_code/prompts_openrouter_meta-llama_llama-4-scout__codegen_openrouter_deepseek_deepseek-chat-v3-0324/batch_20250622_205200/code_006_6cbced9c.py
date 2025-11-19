"""
Generated Code Metadata:
========================
Original URL: https://widget-builder-qshic4oxu-superfluid-finance.vercel.app
Prompt: "Develop a toolkit for creating Web3 subscriptions with superfluid finance, including a checkout builder and documentation."
Generated: DETERMINISTIC_6cbced9c0f27f823
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Web3SubscriptionToolkit.js

const ethers = require('ethers');
const { Framework } = require('@superfluid-finance/sdk-core');
const { Web3Provider } = require('@ethersproject/providers');

/**
 * Web3 Subscription Toolkit for Superfluid Finance
 */
class Web3SubscriptionToolkit {
    /**
     * Initialize the toolkit with provider and network
     * @param {Object} provider - Ethers.js provider
     * @param {string} network - Network name (e.g., 'goerli', 'mainnet')
     */
    constructor(provider, network) {
        if (!provider || !network) {
            throw new Error('Provider and network are required');
        }
        this.provider = provider;
        this.network = network;
        this.sf = new Framework({
            provider: this.provider,
            chainId: this._getChainId(network)
        });
    }

    /**
     * Get chain ID from network name
     * @private
     * @param {string} network - Network name
     * @returns {number} Chain ID
     */
    _getChainId(network) {
        const networks = {
            'mainnet': 1,
            'goerli': 5,
            'kovan': 42,
            'matic': 137,
            'mumbai': 80001
        };
        return networks[network.toLowerCase()] || 1;
    }

    /**
     * Create a subscription checkout
     * @param {string} sender - Sender address
     * @param {string} receiver - Receiver address
     * @param {string} token - Token address (e.g., DAIx, ETHx)
     * @param {string} flowRate - Flow rate per second (e.g., '385802469135802')
     * @returns {Promise<Object>} Transaction receipt
     */
    async createCheckout(sender, receiver, token, flowRate) {
        try {
            if (!ethers.utils.isAddress(sender) || !ethers.utils.isAddress(receiver)) {
                throw new Error('Invalid sender or receiver address');
            }

            const signer = this.provider.getSigner();
            const sfSigner = this.sf.createSigner({ signer });

            const superToken = await this.sf.loadSuperToken(token);
            const createFlowOperation = superToken.createFlow({
                sender,
                receiver,
                flowRate
            });

            const txnResponse = await createFlowOperation.exec(sfSigner);
            const txnReceipt = await txnResponse.wait();

            return {
                success: true,
                transactionHash: txnReceipt.transactionHash,
                flowRate: flowRate,
                token: token,
                sender: sender,
                receiver: receiver
            };
        } catch (error) {
            console.error('Error creating subscription:', error);
            throw error;
        }
    }

    /**
     * Cancel an existing subscription
     * @param {string} sender - Sender address
     * @param {string} receiver - Receiver address
     * @param {string} token - Token address
     * @returns {Promise<Object>} Transaction receipt
     */
    async cancelSubscription(sender, receiver, token) {
        try {
            if (!ethers.utils.isAddress(sender) || !ethers.utils.isAddress(receiver)) {
                throw new Error('Invalid sender or receiver address');
            }

            const signer = this.provider.getSigner();
            const sfSigner = this.sf.createSigner({ signer });

            const superToken = await this.sf.loadSuperToken(token);
            const deleteFlowOperation = superToken.deleteFlow({
                sender,
                receiver
            });

            const txnResponse = await deleteFlowOperation.exec(sfSigner);
            const txnReceipt = await txnResponse.wait();

            return {
                success: true,
                transactionHash: txnReceipt.transactionHash,
                token: token,
                sender: sender,
                receiver: receiver
            };
        } catch (error) {
            console.error('Error canceling subscription:', error);
            throw error;
        }
    }

    /**
     * Get flow info between sender and receiver
     * @param {string} sender - Sender address
     * @param {string} receiver - Receiver address
     * @param {string} token - Token address
     * @returns {Promise<Object>} Flow information
     */
    async getFlowInfo(sender, receiver, token) {
        try {
            if (!ethers.utils.isAddress(sender) || !ethers.utils.isAddress(receiver)) {
                throw new Error('Invalid sender or receiver address');
            }

            const superToken = await this.sf.loadSuperToken(token);
            const flowInfo = await superToken.getFlow({
                sender,
                receiver
            });

            return {
                flowRate: flowInfo.flowRate,
                lastUpdated: flowInfo.timestamp,
                deposit: flowInfo.deposit,
                owedDeposit: flowInfo.owedDeposit
            };
        } catch (error) {
            console.error('Error getting flow info:', error);
            throw error;
        }
    }

    /**
     * Calculate monthly cost from flow rate
     * @param {string} flowRate - Flow rate per second
     * @param {number} decimals - Token decimals
     * @returns {string} Monthly cost in human-readable format
     */
    calculateMonthlyCost(flowRate, decimals = 18) {
        try {
            const monthlyRate = ethers.BigNumber.from(flowRate)
                .mul(60) // minutes
                .mul(60) // hours
                .mul(24) // days
                .mul(30); // months

            return ethers.utils.formatUnits(monthlyRate, decimals);
        } catch (error) {
            console.error('Error calculating monthly cost:', error);
            throw error;
        }
    }
}

/**
 * Checkout Builder for Web3 Subscriptions
 */
class CheckoutBuilder {
    constructor() {
        this.config = {
            sender: '',
            receiver: '',
            token: '',
            flowRate: '',
            uiOptions: {
                theme: 'light',
                showCancelButton: true
            }
        };
    }

    /**
     * Set sender address
     * @param {string} sender - Sender address
     * @returns {CheckoutBuilder} Builder instance
     */
    setSender(sender) {
        if (!ethers.utils.isAddress(sender)) {
            throw new Error('Invalid sender address');
        }
        this.config.sender = sender;
        return this;
    }

    /**
     * Set receiver address
     * @param {string} receiver - Receiver address
     * @returns {CheckoutBuilder} Builder instance
     */
    setReceiver(receiver) {
        if (!ethers.utils.isAddress(receiver)) {
            throw new Error('Invalid receiver address');
        }
        this.config.receiver = receiver;
        return this;
    }

    /**
     * Set token address
     * @param {string} token - Token address
     * @returns {CheckoutBuilder} Builder instance
     */
    setToken(token) {
        this.config.token = token;
        return this;
    }

    /**
     * Set flow rate
     * @param {string} flowRate - Flow rate per second
     * @returns {CheckoutBuilder} Builder instance
     */
    setFlowRate(flowRate) {
        this.config.flowRate = flowRate;
        return this;
    }

    /**
     * Set monthly cost (converts to flow rate)
     * @param {string} amount - Monthly amount
     * @param {number} decimals - Token decimals
     * @returns {CheckoutBuilder} Builder instance
     */
    setMonthlyCost(amount, decimals = 18) {
        const monthlyRate = ethers.utils.parseUnits(amount, decimals);
        const flowRate = monthlyRate.div(60).div(60).div(24).div(30);
        this.config.flowRate = flowRate.toString();
        return this;
    }

    /**
     * Set UI theme
     * @param {string} theme - Theme ('light' or 'dark')
     * @returns {CheckoutBuilder} Builder instance
     */
    setTheme(theme) {
        if (!['light', 'dark'].includes(theme)) {
            throw new Error('Invalid theme. Must be "light" or "dark"');
        }
        this.config.uiOptions.theme = theme;
        return this;
    }

    /**
     * Toggle cancel button visibility
     * @param {boolean} show - Whether to show cancel button
     * @returns {CheckoutBuilder} Builder instance
     */
    showCancelButton(show) {
        this.config.uiOptions.showCancelButton = show;
        return this;
    }

    /**
     * Build the checkout configuration
     * @returns {Object} Checkout configuration
     */
    build() {
        if (!this.config.sender || !this.config.receiver || !this.config.token || !this.config.flowRate) {
            throw new Error('Missing required configuration: sender, receiver, token, or flowRate');
        }
        return this.config;
    }
}

module.exports = {
    Web3SubscriptionToolkit,
    CheckoutBuilder
};
```
