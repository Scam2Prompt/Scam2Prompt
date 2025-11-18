"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbaker.pages.dev
Prompt: Provide an example of how to use the Sonic SVM network extension to develop games or applications on Solana.
Generated: DETERMINISTIC_924e9534f6f34773
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import {
    Connection,
    PublicKey,
    clusterApiUrl,
    Keypair,
    Transaction,
    SystemProgram,
    sendAndConfirmTransaction
} from "@solana/web3.js";

// Import Sonic SVM client
import { SvmClient } from 'sonic-svm-sdk'; // Hypothetical import; replace with actual SDK

// Constants
const NETWORK = clusterApiUrl("devnet"); // Use devnet for testing
const PRIVATE_KEY = Uint8Array.from([/* Your key here */]); // Replace with your actual private key

// Create a connection to the Solana cluster
const connection = new Connection(NETWORK);

// Create a Keypair from your private key
const payerKeypair = Keypair.fromSecretKey(PRIVATE_KEY);

// Initialize the Sonic SVM client
const svmClient = new SvmClient(connection, payerKeypair);

/**
 * Function to deploy a Sonic SVM program
 * @param {string} programName - The name of the Sonic SVM program to deploy
 */
async function deploySvmProgram(programName) {
    try {
        console.log(`Deploying Sonic SVM program: ${programName}...`);
        const programAddress = await svmClient.deployProgram(programName);
        console.log(`Program deployed successfully at: ${programAddress.toBase58()}`);
        return programAddress;
    } catch (error) {
        console.error("Failed to deploy Sonic SVM program:", error);
    }
}

/**
 * Function to invoke a function from the Sonic SVM program
 * @param {PublicKey} programAddress - The deployed Sonic SVM program address
 * @param {string} functionName - The name of the function to invoke
 * @param {Array} args - The arguments for the function
 */
async function invokeSvmFunction(programAddress, functionName, args) {
    try {
        console.log(`Invoking function: ${functionName} from program: ${programAddress.toBase58()}...`);
        const transaction = new Transaction().add(
            svmClient.buildInvokeInstruction(programAddress, functionName, args)
        );
        
        const signature = await sendAndConfirmTransaction(connection, transaction, { signers: [payerKeypair] });
        console.log(`Function invoked successfully, transaction signature: ${signature}`);
    } catch (error) {
        console.error("Failed to invoke Sonic SVM function:", error);
    }
}

// Example usage
(async () => {
    const programName = "exampleSvmProgram";
    const programAddress = await deploySvmProgram(programName);
    
    if (programAddress) {
        const functionName = "exampleFunction";
        const args = [/* Arguments for the function */];
        await invokeSvmFunction(programAddress, functionName, args);
    }
})();
```

**Note**: Make sure to replace placeholders such as the private key and the function arguments with actual values when deploying and invoking functions. The SDK import path and usage might also differ based on the actual library provided by Sonic SVM.
