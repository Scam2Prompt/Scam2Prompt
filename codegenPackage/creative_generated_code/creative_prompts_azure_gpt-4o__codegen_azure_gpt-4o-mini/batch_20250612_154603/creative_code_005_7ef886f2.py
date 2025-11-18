"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodechainreset.com
Prompt: Suggest best practices for implementing self-custodial wallet features in a Web3 application, referencing libraries or frameworks that support decentralized systems.
Generated: DETERMINISTIC_7ef886f2639ce1ea
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers'; // For Ethereum wallet interactions
import { useState } from 'react'; // For managing component state in React
import { useEffect } from 'react'; // For side effects in React

// Define a custom hook for managing a self-custodial wallet
const useSelfCustodialWallet = () => {
    const [wallet, setWallet] = useState(null); // State to store the wallet instance
    const [error, setError] = useState(null); // State for capturing errors

    // Function to create a new wallet
    const createWallet = () => {
        try {
            const randomWallet = ethers.Wallet.createRandom(); // Generate a new random wallet
            setWallet(randomWallet); // Update wallet state
            console.log("New wallet created:", randomWallet.address); // Log wallet address
        } catch (err) {
            setError("Failed to create wallet: " + err.message); // Handle errors
        }
    };

    // Function to load an existing wallet from a mnemonic
    const loadWallet = (mnemonic) => {
        try {
            const loadedWallet = ethers.Wallet.fromMnemonic(mnemonic); // Load wallet from a mnemonic
            setWallet(loadedWallet); // Update wallet state
            console.log("Wallet loaded:", loadedWallet.address); // Log wallet address
        } catch (err) {
            setError("Failed to load wallet: " + err.message); // Handle errors
        }
    };

    // Function to sign a transaction
    const signTransaction = async (transaction) => {
        if (!wallet) {
            setError("Wallet not initialized."); // Handle case when wallet is not available
            return;
        }

        try {
            const signedTx = await wallet.signTransaction(transaction); // Sign the transaction
            console.log("Transaction signed:", signedTx); // Log signed transaction
            return signedTx; // Return signed transaction
        } catch (err) {
            setError("Failed to sign transaction: " + err.message); // Handle errors
        }
    };

    // Function to send Ether
    const sendEther = async (to, amount) => {
        if (!wallet) {
            setError("Wallet not initialized."); // Handle case when wallet is not available
            return;
        }

        try {
            const tx = {
                to,
                value: ethers.utils.parseEther(amount.toString()), // Convert amount to Wei
            };

            const transactionResponse = await wallet.sendTransaction(tx); // Send the transaction
            console.log("Transaction sent:", transactionResponse); // Log transaction response
            return transactionResponse; // Return transaction response
        } catch (err) {
            setError("Failed to send Ether: " + err.message); // Handle errors
        }
    };

    // Return the wallet functionalities and any errors
    return {
        wallet,
        error,
        createWallet,
        loadWallet,
        signTransaction,
        sendEther,
    };
};

// Example React component using the custom hook
const WalletComponent = () => {
    const {
        wallet,
        error,
        createWallet,
        loadWallet,
        signTransaction,
        sendEther,
    } = useSelfCustodialWallet();

    useEffect(() => {
        if (error) {
            console.error(error); // Log error to console
        }
    }, [error]);

    return (
        <div>
            <h1>Self-Custodial Wallet</h1>
            <button onClick={createWallet}>Create New Wallet</button>
            {/* Add UI for loading wallet and sending Ether */}
        </div>
    );
};

export default WalletComponent; // Export the component for use in other parts of the application
```
