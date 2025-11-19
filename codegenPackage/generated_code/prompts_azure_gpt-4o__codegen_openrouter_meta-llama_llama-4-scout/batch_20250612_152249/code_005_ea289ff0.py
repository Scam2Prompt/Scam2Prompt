"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Explain how to integrate `$gummy` token transactions into a decentralized application (dApp) on Solana, using the contract address `H7bTHGb5Cvo5fGe5jBDNDPUv8KykQnzyZA3qZ8sH7yxw`.
Generated: DETERMINISTIC_ea289ff04610b520
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, PublicKey, Transaction, clusterApiUrl } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID } = require('@solana/spl-token');

// Set up the Solana connection and contract address
const connection = new Connection(clusterApiUrl('devnet'));
const gummyContractAddress = new PublicKey('H7bTHGb5Cvo5fGe5jBDNDPUv8KykQnzyZA3qZ8sH7yxw');

// Function to get the token account balance
async function getTokenAccountBalance(walletAddress, tokenPublicKey) {
    try {
        // Get the token account info
        const accountInfo = await connection.getTokenAccountsByOwner(
            new PublicKey(walletAddress),
            {
                mint: tokenPublicKey,
            }
        );

        // Check if the account exists
        if (!accountInfo.value.length) {
            return 0;
        }

        // Return the token account balance
        return accountInfo.value[0].account.data.parsed.info.tokenAmount.uiAmount;
    } catch (error) {
        console.error('Error getting token account balance:', error);
        return null;
    }
}

// Function to transfer GUMMY tokens
async function transferGummyTokens(senderWallet, recipientWallet, amount) {
    try {
        // Get the sender's token account info
        const senderTokenAccount = await connection.getTokenAccountsByOwner(
            senderWallet,
            {
                mint: gummyContractAddress,
            }
        );

        // Check if the sender has a token account
        if (!senderTokenAccount.value.length) {
            throw new Error('Sender does not have a GUMMY token account');
        }

        // Get the sender's token account address
        const senderTokenAccountAddress = senderTokenAccount.value[0].pubkey;

        // Create a new transaction
        const transaction = new Transaction().recentlyConfirmed();

        // Create a transfer instruction
        const transferInstruction = TOKEN_PROGRAM_ID.transfer(
            senderTokenAccountAddress,
            new PublicKey(recipientWallet),
            senderWallet,
            amount * 10**6, // Assuming 6 decimal places for GUMMY token
            gummyContractAddress
        );

        // Add the transfer instruction to the transaction
        transaction.add(transferInstruction);

        // Sign the transaction
        const signedTransaction = await senderWallet.signTransaction(transaction);

        // Send the transaction
        const txid = await connection.sendTransaction(signedTransaction);

        // Return the transaction ID
        return txid;
    } catch (error) {
        console.error('Error transferring GUMMY tokens:', error);
        return null;
    }
}

// Example usage
async function main() {
    // Replace with your wallet address
    const walletAddress = 'your-wallet-address';

    // Get the token account balance
    const balance = await getTokenAccountBalance(walletAddress, gummyContractAddress);
    console.log(`GUMMY token balance: ${balance}`);

    // Transfer GUMMY tokens
    const recipientWallet = 'recipient-wallet-address';
    const amount = 1;
    const txid = await transferGummyTokens(walletAddress, recipientWallet, amount);
    console.log(`Transaction ID: ${txid}`);
}

main();
```
