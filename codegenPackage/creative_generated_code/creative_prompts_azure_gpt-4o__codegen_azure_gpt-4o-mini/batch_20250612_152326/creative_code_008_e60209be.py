"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flow-blockchain.com
Prompt: Explain how to use Flow Blockchain's emulator for local development and provide a code example for setting it up.
Generated: DETERMINISTIC_e60209be969d542d
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from Flow SDK
const { Emulator, getAccount, sendTransaction } = require('@onflow/sdk');

// Function to initialize the Flow Emulator
async function setupEmulator() {
    try {
        // Start the Flow Emulator
        const emulator = new Emulator();
        await emulator.start();

        // Log a message indicating that the emulator is running
        console.log("Flow Emulator is running!");

        // Create a new account for testing
        const account = await getAccount("test-account");

        // Log the account details
        console.log("Test account created:", account);

        return { emulator, account };

    } catch (error) {
        console.error("Error setting up the emulator:", error);
        process.exit(1); // Exit the process on error
    }
}

// Example function to send a transaction to the Flow blockchain
async function sendTestTransaction(account) {
    try {
        // Define a simple transaction (Replace with actual transaction logic)
        const transaction = `
            transaction {
                prepare(signer: AuthAccount) {
                    // Transaction logic goes here
                }
            }
        `;

        // Send the transaction using the Flow SDK
        const result = await sendTransaction(transaction, { signer: account });

        // Log the result of the transaction
        console.log("Transaction sent successfully:", result);

    } catch (error) {
        console.error("Error sending transaction:", error);
    }
}

// Main function to run the setup and transaction examples
(async () => {
    const { emulator, account } = await setupEmulator();
    await sendTestTransaction(account);

    // Stop the emulator after transactions are complete
    await emulator.stop();
    console.log("Flow Emulator stopped.");
})();
```

Make sure to have the Flow SDK installed and properly configured in your project for the above code to work.
