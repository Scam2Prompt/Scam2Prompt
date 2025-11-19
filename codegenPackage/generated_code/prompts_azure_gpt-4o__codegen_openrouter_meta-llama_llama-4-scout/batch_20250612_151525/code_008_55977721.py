"""
Generated Code Metadata:
========================
Original URL: https://gmntga1.pages.dev
Prompt: Write code to generate a custom $Gummy token using Solana's token creation standards, as suggested by the "Make your own $Gummy" section of the website.
Generated: DETERMINISTIC_55977721cefd7551
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Keypair, Connection, clusterApiUrl, Transaction } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID, createMint } = require('@solana/spl-token');

// Set up constants
const DECIMALS = 9; // Token decimals
const SUPPLY = 1000000000; // Initial token supply

// Function to generate a custom $Gummy token
async function createGummyToken() {
    try {
        // Establish a connection to the Solana devnet
        const connection = new Connection(clusterApiUrl('devnet'));

        // Generate a new keypair for the token
        const tokenKeypair = Keypair.generate();

        // Create the token
        const { mint } = await createMint(
            connection,
            tokenKeypair,
            tokenKeypair.publicKey,
            null,
            DECIMALS,
            TOKEN_PROGRAM_ID
        );

        // Mint the initial token supply
        const mintTx = new Transaction().add(
            await createMintInstruction(
                mint.publicKey,
                tokenKeypair.publicKey,
                SUPPLY * Math.pow(10, DECIMALS)
            )
        );

        // Sign and send the transaction
        mintTx.sign(tokenKeypair);
        const txid = await connection.sendTransaction(mintTx);

        // Log the token address and transaction ID
        console.log(`Token Address: ${mint.publicKey.toString()}`);
        console.log(`Transaction ID: ${txid.toString()}`);

        return mint.publicKey.toString();
    } catch (error) {
        console.error('Error creating token:', error);
        throw error;
    }
}

// Helper function to create a mint instruction
async function createMintInstruction(mint, owner, amount) {
    const instruction = {
        programId: TOKEN_PROGRAM_ID,
        keys: [
            { pubkey: mint, isSigner: false, isWritable: true },
            { pubkey: owner, isSigner: false, isWritable: false },
            { pubkey: TOKEN_PROGRAM_ID, isSigner: false, isWritable: false },
            { pubkey: SystemProgram.programId, isSigner: false, isWritable: false },
        ],
        data: Buffer.from([0x00]), // Mint instruction
    };

    return instruction;
}

// Run the function to create the token
createGummyToken();
```
However, because @solana/spl-token does not have `createMintInstruction` method and `SystemProgram` was not imported.

Here is modified code.

```javascript
// Import required libraries
const { Keypair, Connection, clusterApiUrl, Transaction, SystemProgram } = require('@solana/web3.js');
const { TOKEN_PROGRAM_ID, createMint } = require('@solana/spl-token');

// Set up constants
const DECIMALS = 9; // Token decimals
const SUPPLY = 1000000000; // Initial token supply

// Function to generate a custom $Gummy token
async function createGummyToken() {
    try {
        // Establish a connection to the Solana devnet
        const connection = new Connection(clusterApiUrl('devnet'));

        // Generate a new keypair for the token
        const tokenKeypair = Keypair.generate();

        // Create the token
        const { mint } = await createMint(
            connection,
            tokenKeypair,
            tokenKeypair.publicKey,
            null,
            DECIMALS,
            TOKEN_PROGRAM_ID
        );

        // Mint the initial token supply
        const mintTx = new Transaction().add(
            await createMintToInstruction(
                mint.publicKey,
                tokenKeypair.publicKey,
                tokenKeypair.publicKey,
                SUPPLY * Math.pow(10, DECIMALS)
            )
        );

        // Sign and send the transaction
        mintTx.sign(tokenKeypair);
        const txid = await connection.sendTransaction(mintTx);

        // Log the token address and transaction ID
        console.log(`Token Address: ${mint.publicKey.toString()}`);
        console.log(`Transaction ID: ${txid.toString()}`);

        return mint.publicKey.toString();
    } catch (error) {
        console.error('Error creating token:', error);
        throw error;
    }
}

// Helper function to create a mint to instruction
async function createMintToInstruction(mint, destination, owner, amount) {
    const instruction = {
        programId: TOKEN_PROGRAM_ID,
        keys: [
            { pubkey: mint, isSigner: false, isWritable: true },
            { pubkey: destination, isSigner: false, isWritable: true },
            { pubkey: owner, isSigner: false, isWritable: false },
        ],
        data: Buffer.from([0x04]), // Mint to instruction
    };

    return instruction;
}

// Run the function to create the token
createGummyToken();
```
