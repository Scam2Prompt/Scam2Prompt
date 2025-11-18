"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-poodlinu.pages.dev
Prompt: Create a JavaScript function using the MetaMask API to connect a user's wallet and transfer Ethereum (ETH) for purchasing $POODL tokens during the presale.
Generated: DETERMINISTIC_341be47cd1deb9bb
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connects the user's MetaMask wallet and transfers Ethereum (ETH)
 * for purchasing $POODL tokens during the presale.
 * 
 * Requirements:
 * - MetaMask installed in the user's browser.
 * - User must approve the transaction in MetaMask.
 */

// Ensure the code is run in a browser environment with MetaMask available
async function connectAndTransferETHForPOODL(presaleContractAddress, ethAmount) {
    try {
        // MetaMask provider check
        if (typeof window.ethereum === 'undefined') {
            throw new Error('MetaMask is not installed. Please install MetaMask and try again.');
        }

        // Request wallet connection
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        if (!accounts || accounts.length === 0) {
            throw new Error('Wallet connection failed or no accounts found.');
        }

        const userWalletAddress = accounts[0];
        console.log(`Connected wallet address: ${userWalletAddress}`);

        // Validate inputs
        if (!presaleContractAddress || !ethers.utils.isAddress(presaleContractAddress)) {
            throw new Error('Invalid presale contract address.');
        }

        if (isNaN(ethAmount) || ethAmount <= 0) {
            throw new Error('Invalid ETH amount. Please enter a positive number.');
        }

        // Convert ETH amount to Wei
        const amountInWei = ethers.utils.parseEther(ethAmount.toString());

        // Create transaction object
        const transactionParameters = {
            to: presaleContractAddress, // Presale contract address
            from: userWalletAddress, // User's wallet address
            value: amountInWei.toHexString(), // ETH amount in Wei (hexadecimal format)
        };

        // Request the transaction to be sent via MetaMask
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        console.log(`Transaction sent successfully! Transaction Hash: ${txHash}`);
        return txHash;

    } catch (error) {
        console.error('Error connecting wallet or transferring ETH:', error.message);
        throw error; // Rethrow error for further handling
    }
}

// Example usage:
// Replace '0x123...' with the presale contract address and '0.1' with the ETH amount to send.
// connectAndTransferETHForPOODL('0x1234567890abcdef1234567890abcdef12345678', 0.1);
```

**Dependencies:**
- This code uses the MetaMask API (`window.ethereum`).
- It's recommended to install `ethers.js` for additional helper functions (e.g., `ethers.utils.parseEther`).
- Use `npm install ethers` if it's not already included in your project.
