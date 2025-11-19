"""
Generated Code Metadata:
========================
Original URL: https://welcome-metamask-io-cdn.bravesites.com
Prompt: Create a function to connect a decentralized application (dApp) to MetaMask, enabling token swaps and transactions securely as described in the content.
Generated: DETERMINISTIC_03426560224b0e91
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');

/**
 * Connects a dApp to MetaMask and enables token swaps and transactions.
 * @returns {Object} An object containing the provider, signer, and account address.
 * @throws {Error} If MetaMask is not installed or connection fails.
 */
async function connectToMetaMask() {
    try {
        // Check if MetaMask is installed
        if (!window.ethereum) {
            throw new Error('MetaMask is not installed. Please install it to use this dApp.');
        }

        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please connect an account in MetaMask.');
        }

        // Create a provider and signer
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();

        return {
            provider,
            signer,
            address
        };
    } catch (error) {
        console.error('Error connecting to MetaMask:', error);
        throw error;
    }
}

/**
 * Executes a token swap transaction.
 * @param {Object} signer - The signer object from ethers.js.
 * @param {string} tokenIn - The address of the token to swap from.
 * @param {string} tokenOut - The address of the token to swap to.
 * @param {string} amountIn - The amount of tokenIn to swap.
 * @param {string} routerAddress - The address of the swap router contract.
 * @param {string} abi - The ABI of the swap router contract.
 * @returns {Object} The transaction receipt.
 * @throws {Error} If the transaction fails.
 */
async function executeTokenSwap(signer, tokenIn, tokenOut, amountIn, routerAddress, abi) {
    try {
        // Create a contract instance
        const routerContract = new ethers.Contract(routerAddress, abi, signer);

        // Approve token transfer if necessary (assuming ERC20 token)
        const tokenInContract = new ethers.Contract(tokenIn, [
            'function approve(address spender, uint256 amount) returns (bool)'
        ], signer);

        const approveTx = await tokenInContract.approve(routerAddress, amountIn);
        await approveTx.wait();

        // Execute the swap (example using Uniswap-like router)
        const swapTx = await routerContract.swapExactTokensForTokens(
            amountIn,
            0, // minimum amount out (set to 0 for simplicity, adjust in production)
            [tokenIn, tokenOut],
            await signer.getAddress(),
            Math.floor(Date.now() / 1000) + 60 * 20 // deadline 20 minutes from now
        );

        const receipt = await swapTx.wait();
        return receipt;
    } catch (error) {
        console.error('Error executing token swap:', error);
        throw error;
    }
}

/**
 * Sends a transaction.
 * @param {Object} signer - The signer object from ethers.js.
 * @param {string} to - The recipient address.
 * @param {string} value - The amount of ETH to send (in wei).
 * @returns {Object} The transaction receipt.
 * @throws {Error} If the transaction fails.
 */
async function sendTransaction(signer, to, value) {
    try {
        const tx = await signer.sendTransaction({
            to,
            value: ethers.utils.parseEther(value)
        });

        const receipt = await tx.wait();
        return receipt;
    } catch (error) {
        console.error('Error sending transaction:', error);
        throw error;
    }
}

// Export functions
module.exports = {
    connectToMetaMask,
    executeTokenSwap,
    sendTransaction
};
```
