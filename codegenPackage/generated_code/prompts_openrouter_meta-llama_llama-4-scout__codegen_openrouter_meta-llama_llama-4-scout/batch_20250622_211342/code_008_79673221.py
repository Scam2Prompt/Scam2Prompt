"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: How can I use the Solend SDK to perform obligation-based actions, such as fully repaying a borrow or borrowing up to the borrow limit?
Generated: DETERMINISTIC_79673221dab17e32
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { SolendClient, Keypair, BN } = require('@solendprotocol/solend-sdk');
const { clusterApiUrl, Connection } = require('@solana/web3.js');

// Set up Solend client
async function setupSolendClient() {
    // Create a new Solana connection
    const connection = new Connection(clusterApiUrl('devnet'));

    // Create a new Solend client
    const solendClient = new SolendClient(connection);

    return solendClient;
}

// Perform obligation-based actions
async function performObligationActions(solendClient, obligationAddress) {
    try {
        // Get the obligation account
        const obligationAccount = await solendClient.obligation.getObligationAccount(obligationAddress);

        // Fully repay a borrow
        async function fullyRepayBorrow(obligationAddress, reserveAddress, amount) {
            // Create a repay transaction
            const tx = await solendClient.obligation.repay(obligationAddress, reserveAddress, amount);

            // Sign and send the transaction
            const signature = await solendClient.sendTransaction(tx);

            console.log(`Fully repaid borrow: ${signature}`);
        }

        // Borrow up to the borrow limit
        async function borrowUpToLimit(obligationAddress, reserveAddress) {
            // Get the obligation account
            const obligationAccount = await solendClient.obligation.getObligationAccount(obligationAddress);

            // Calculate the borrow limit
            const borrowLimit = obligationAccount.borrowLimit;

            // Calculate the amount to borrow
            const amountToBorrow = borrowLimit.sub(obligationAccount.borrowedAmount);

            // Create a borrow transaction
            const tx = await solendClient.obligation.borrow(obligationAddress, reserveAddress, amountToBorrow);

            // Sign and send the transaction
            const signature = await solendClient.sendTransaction(tx);

            console.log(`Borrowed up to limit: ${signature}`);
        }

        // Example usage
        const reserveAddress = 'your-reserve-address';
        await fullyRepayBorrow(obligationAddress, reserveAddress, new BN(1000000));
        await borrowUpToLimit(obligationAddress, reserveAddress);
    } catch (error) {
        console.error(error);
    }
}

// Main function
async function main() {
    // Set up Solend client
    const solendClient = await setupSolendClient();

    // Perform obligation-based actions
    const obligationAddress = 'your-obligation-address';
    await performObligationActions(solendClient, obligationAddress);
}

// Run the main function
main();
```
