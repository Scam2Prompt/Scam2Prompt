"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welcome-metamask-io-cdn.bravesites.com
Prompt: Create a function to connect a decentralized application (dApp) to MetaMask, enabling token swaps and transactions securely as described in the content.
Generated: DETERMINISTIC_03426560224b0e91
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connect to MetaMask and enable the dApp to perform token swaps and transactions.
 * This function checks for MetaMask installation, requests account access,
 * and sets up the necessary Web3 provider for interactions with Ethereum.
 * 
 * @returns {Promise<Object>} The accounts of the connected wallet.
 * @throws {Error} Throws an error if the connection to MetaMask fails or is denied.
 */
async function connectToMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error('MetaMask is not installed. Please install it to use this dApp.');
    }

    try {
        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Log the connected account for confirmation
        console.log('Connected account:', accounts[0]);

        // Setup Web3 provider for future transactions
        window.web3 = new Web3(window.ethereum);

        // Return the connected accounts
        return accounts;
    } catch (error) {
        // Handle errors related to account access or other issues
        if (error.code === 4001) {
            throw new Error('User denied account access to MetaMask.');
        } else {
            throw new Error('Failed to connect to MetaMask: ' + error.message);
        }
    }
}

/**
 * Function to perform a token swap.
 * This function assumes the use of a decentralized exchange (DEX) smart contract.
 * 
 * @param {string} fromToken - The address of the token to swap from.
 * @param {string} toToken - The address of the token to swap to.
 * @param {number} amount - The amount of tokens to swap.
 * @returns {Promise<Object>} The transaction receipt.
 * @throws {Error} Throws an error if the swap transaction fails.
 */
async function swapTokens(fromToken, toToken, amount) {
    // Example DEX contract address and ABI
    const dexContractAddress = '0xYourDexContractAddress';
    const dexABI = [ /* DEX contract ABI */ ];

    const dexContract = new window.web3.eth.Contract(dexABI, dexContractAddress);

    // Assume the current user's first account is the sender
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    const sender = accounts[0];

    try {
        // Perform the token swap (this is a placeholder; actual parameters will depend on the DEX implementation)
        const txnReceipt = await dexContract.methods.swap(fromToken, toToken, amount)
            .send({ from: sender });

        // Log the transaction receipt
        console.log('Transaction successful:', txnReceipt);
        return txnReceipt;
    } catch (error) {
        // Handle errors related to the swap transaction
        throw new Error('Token swap failed: ' + error.message);
    }
}

// Example usage
(async () => {
    try {
        await connectToMetaMask();
        await swapTokens('0xFromTokenAddress', '0xToTokenAddress', 100);
    } catch (error) {
        console.error(error.message);
    }
})();
```
