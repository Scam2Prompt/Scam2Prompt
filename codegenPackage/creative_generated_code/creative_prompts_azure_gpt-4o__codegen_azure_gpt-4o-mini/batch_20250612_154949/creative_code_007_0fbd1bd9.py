"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltokenburner.com
Prompt: Create a Solana-based application that integrates SOLTOKENBURNER's wallet connection and token burning capabilities.
Generated: DETERMINISTIC_0fbd1bd9b1cbfa52
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { Connection, PublicKey, clusterApiUrl, Transaction, SystemProgram } from '@solana/web3.js';
import { useWallet } from '@solana/wallet-adapter-react';
import { TOKEN_PROGRAM_ID, Token } from '@solana/spl-token';
import { Button, Input } from '@material-ui/core';

// Define the SolanaBurner component
const SolanaBurner = () => {
    // State variables
    const [burnAmount, setBurnAmount] = useState(0);
    const [transactionStatus, setTransactionStatus] = useState('');
    
    // Access wallet connection
    const wallet = useWallet();
    
    // Check if the wallet is connected
    useEffect(() => {
        if (!wallet.connected) {
            setTransactionStatus('Please connect your wallet');
        }
    }, [wallet.connected]);

    // Function to handle token burning
    const handleBurnTokens = async () => {
        try {
            // Validate burn amount
            if (burnAmount <= 0) {
                throw new Error('Burn amount must be greater than 0');
            }

            // Establish connection to Solana cluster
            const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');
            
            // Create a transaction to burn tokens
            const transaction = new Transaction().add(
                Token.createBurnInstruction(
                    TOKEN_PROGRAM_ID,
                    new PublicKey('YOUR_TOKEN_MINT_ADDRESS'), // replace with your token mint address
                    wallet.publicKey,
                    wallet.publicKey,
                    [],
                    burnAmount
                )
            );

            // Sign and send the transaction
            const signature = await wallet.sendTransaction(transaction, connection);
            await connection.confirmTransaction(signature, 'processed');
            
            setTransactionStatus(`Tokens burned successfully! Transaction: ${signature}`);
        } catch (error) {
            console.error('Transaction Error:', error);
            setTransactionStatus(`Error: ${error.message}`);
        }
    };

    return (
        <div>
            <h1>Solana Token Burner</h1>
            <p>{transactionStatus}</p>
            <Input
                type="number"
                placeholder="Enter amount to burn"
                value={burnAmount}
                onChange={(e) => setBurnAmount(Number(e.target.value))}
            />
            <Button
                onClick={handleBurnTokens}
                disabled={!wallet.connected || burnAmount <= 0}
            >
                Burn Tokens
            </Button>
        </div>
    );
};

export default SolanaBurner;
```

### Notes:
- Replace `YOUR_TOKEN_MINT_ADDRESS` with the actual token mint address you intend to burn tokens from.
- Ensure that all necessary libraries (`@solana/web3.js`, `@solana/spl-token`, `@solana/wallet-adapter-react`, and `@material-ui/core`) are installed in your project before running this code.
- This code should be placed within a React application and assumes that the necessary wallet provider is integrated.
