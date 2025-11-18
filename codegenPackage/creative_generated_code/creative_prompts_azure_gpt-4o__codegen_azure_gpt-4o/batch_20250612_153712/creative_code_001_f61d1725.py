"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmsetumsklogi.webflow.io
Prompt: Generate code to integrate a decentralized application (dApp) with Metamask, allowing users to connect their Ethereum wallet and sign transactions directly from the browser.
Generated: DETERMINISTIC_f61d1725e83864ce
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Filename: dapp-metamask-integration.js

// Function to check if MetaMask is installed
async function checkMetaMaskInstallation() {
    if (typeof window.ethereum !== 'undefined') {
        console.log("MetaMask is installed!");
        return true;
    } else {
        console.error("MetaMask is not installed. Please install MetaMask to continue.");
        return false;
    }
}

// Function to connect the user's wallet to the dApp
async function connectWallet() {
    try {
        // Request user's wallet connection
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Wallet connected:", accounts[0]);
        return accounts[0]; // Returning the first connected account
    } catch (error) {
        console.error("Failed to connect wallet:", error.message);
        throw new Error("Wallet connection failed.");
    }
}

// Function to sign a transaction using MetaMask
async function signTransaction(transactionParameters) {
    try {
        // Request the user to sign a transaction
        const signedTransactionHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        console.log("Transaction signed successfully:", signedTransactionHash);
        return signedTransactionHash;
    } catch (error) {
        console.error("Failed to sign transaction:", error.message);
        throw new Error("Transaction signing failed.");
    }
}

// Example usage: Check MetaMask, connect wallet, and sign a transaction
(async () => {
    if (await checkMetaMaskInstallation()) {
        try {
            const userWallet = await connectWallet();

            // Example transaction parameters
            const transactionParameters = {
                from: userWallet, // Sender's wallet address
                to: "0xRecipientWalletAddressHere", // Replace with the recipient's wallet address
                value: "0x29a2241af62c0000", // Amount to send (in wei, hex-encoded). Example: 0.1 ETH
                gas: "0x5208", // Gas limit (in hex). Example: 21000
            };

            const signedTransaction = await signTransaction(transactionParameters);
            console.log("Signed transaction:", signedTransaction);
        } catch (error) {
            console.error("Error occurred:", error.message);
        }
    }
})();
```

### Notes:
- Replace `"0xRecipientWalletAddressHere"` with the actual recipient's wallet address in the transaction parameters.
- Ensure the transaction values like `value` and `gas` are formatted correctly (hex-encoded).
