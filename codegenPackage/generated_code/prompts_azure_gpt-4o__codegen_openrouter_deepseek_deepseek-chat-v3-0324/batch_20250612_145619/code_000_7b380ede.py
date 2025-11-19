"""
Generated Code Metadata:
========================
Original URL: https://ethphbi.com
Prompt: Write a JavaScript function to interact with an Ethereum smart contract for managing pledges, including connecting to a Web3 provider.
Generated: DETERMINISTIC_7b380eded58262ba
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const Web3 = require('web3');
const contractAbi = require('./PledgeContractABI.json'); // ABI file for the contract

/**
 * PledgeManager class to interact with the Ethereum smart contract for pledges.
 */
class PledgeManager {
    /**
     * Initializes the PledgeManager with Web3 provider and contract details.
     * @param {string} contractAddress - The Ethereum address of the deployed contract.
     * @param {string} providerUrl - The URL of the Ethereum provider (e.g., Infura, local node).
     * @param {string} privateKey - The private key for signing transactions (optional).
     */
    constructor(contractAddress, providerUrl, privateKey = null) {
        this.web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));
        this.contractAddress = contractAddress;
        this.contract = new this.web3.eth.Contract(contractAbi, contractAddress);
        
        if (privateKey) {
            this.account = this.web3.eth.accounts.privateKeyToAccount(privateKey);
            this.web3.eth.accounts.wallet.add(this.account);
            this.web3.eth.defaultAccount = this.account.address;
        }
    }

    /**
     * Makes a pledge to the contract.
     * @param {string} pledgerAddress - The address of the pledger.
     * @param {number} amount - The amount to pledge in ETH.
     * @returns {Promise<Object>} - The transaction receipt.
     */
    async makePledge(pledgerAddress, amount) {
        try {
            const weiAmount = this.web3.utils.toWei(amount.toString(), 'ether');
            const tx = this.contract.methods.makePledge(pledgerAddress);
            
            const gasEstimate = await tx.estimateGas({ from: this.account.address, value: weiAmount });
            const gasPrice = await this.web3.eth.getGasPrice();
            
            const txData = {
                from: this.account.address,
                to: this.contractAddress,
                value: weiAmount,
                gas: gasEstimate,
                gasPrice: gasPrice,
                data: tx.encodeABI()
            };
            
            const signedTx = await this.web3.eth.accounts.signTransaction(txData, this.account.privateKey);
            const receipt = await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
            
            return receipt;
        } catch (error) {
            console.error('Error making pledge:', error);
            throw error;
        }
    }

    /**
     * Gets the total amount pledged by an address.
     * @param {string} pledgerAddress - The address to query.
     * @returns {Promise<number>} - The total amount pledged in ETH.
     */
    async getPledgeAmount(pledgerAddress) {
        try {
            const weiAmount = await this.contract.methods.getPledgeAmount(pledgerAddress).call();
            return this.web3.utils.fromWei(weiAmount, 'ether');
        } catch (error) {
            console.error('Error getting pledge amount:', error);
            throw error;
        }
    }

    /**
     * Withdraws a pledge from the contract.
     * @param {string} pledgerAddress - The address of the pledger.
     * @returns {Promise<Object>} - The transaction receipt.
     */
    async withdrawPledge(pledgerAddress) {
        try {
            const tx = this.contract.methods.withdrawPledge(pledgerAddress);
            
            const gasEstimate = await tx.estimateGas({ from: this.account.address });
            const gasPrice = await this.web3.eth.getGasPrice();
            
            const txData = {
                from: this.account.address,
                to: this.contractAddress,
                gas: gasEstimate,
                gasPrice: gasPrice,
                data: tx.encodeABI()
            };
            
            const signedTx = await this.web3.eth.accounts.signTransaction(txData, this.account.privateKey);
            const receipt = await this.web3.eth.sendSignedTransaction(signedTx.rawTransaction);
            
            return receipt;
        } catch (error) {
            console.error('Error withdrawing pledge:', error);
            throw error;
        }
    }

    /**
     * Gets the total pledges in the contract.
     * @returns {Promise<number>} - The total pledges in ETH.
     */
    async getTotalPledges() {
        try {
            const weiAmount = await this.contract.methods.totalPledges().call();
            return this.web3.utils.fromWei(weiAmount, 'ether');
        } catch (error) {
            console.error('Error getting total pledges:', error);
            throw error;
        }
    }
}

module.exports = PledgeManager;
```
