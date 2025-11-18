"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orchidprotocols.com
Prompt: Write a JavaScript function to fund an Orchid account with ERC-20 tokens and send nanopayments for decentralized services.
Generated: DETERMINISTIC_431df7a9ffb84844
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to fund an Orchid account with ERC-20 tokens and send nanopayments for decentralized services.
 * 
 * @param {string} walletAddress - The wallet address of the Orchid account to fund.
 * @param {string} tokenContractAddress - The ERC-20 token contract address.
 * @param {string} senderPrivateKey - The private key of the sender's wallet for signing transactions.
 * @param {number} amount - The amount of tokens to send (in the smallest unit, e.g., wei).
 * @param {object} web3 - An instance of the Web3 library connected to an Ethereum provider.
 * @returns {Promise<string>} - Returns the transaction hash upon successful funding.
 * @throws {Error} - Throws an error if funding fails.
 */
async function fundOrchidAccount(walletAddress, tokenContractAddress, senderPrivateKey, amount, web3) {
    // Check input validity
    if (!web3.utils.isAddress(walletAddress)) {
        throw new Error("Invalid wallet address.");
    }
    if (!web3.utils.isAddress(tokenContractAddress)) {
        throw new Error("Invalid token contract address.");
    }
    if (!web3.utils.isHexStrict(senderPrivateKey) || senderPrivateKey.length !== 66) {
        throw new Error("Invalid private key.");
    }
    if (amount <= 0) {
        throw new Error("Amount must be greater than zero.");
    }

    // Create a contract instance for the ERC-20 token
    const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenContractAddress);

    try {
        // Get the nonce for the sender's account
        const nonce = await web3.eth.getTransactionCount(web3.eth.accounts.privateKeyToAccount(senderPrivateKey).address);

        // Create the transaction object
        const transaction = {
            to: tokenContractAddress,
            data: tokenContract.methods.transfer(walletAddress, amount).encodeABI(),
            gas: 200000, // Set a reasonable gas limit
            nonce: nonce,
            chainId: 1 // Mainnet chain ID (change as necessary)
        };

        // Sign the transaction with the sender's private key
        const signedTx = await web3.eth.accounts.signTransaction(transaction, senderPrivateKey);

        // Send the signed transaction
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

        // Return the transaction hash
        return receipt.transactionHash;

    } catch (error) {
        // Handle and rethrow errors for further diagnostics
        console.error("Error funding Orchid account:", error);
        throw new Error("Funding failed. Please review the error for details.");
    }
}

// Example ERC20 ABI (simplified for demonstration purposes)
const ERC20_ABI = [
    // Only including the transfer method for this example
    {
        "constant": false,
        "inputs": [
            { "name": "_to", "type": "address" },
            { "name": "_value", "type": "uint256" }
        ],
        "name": "transfer",
        "outputs": [{ "name": "", "type": "bool" }],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];
```
