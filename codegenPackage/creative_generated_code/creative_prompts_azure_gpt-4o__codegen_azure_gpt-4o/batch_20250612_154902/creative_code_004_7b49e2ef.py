"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.paws-community.xyz
Prompt: Write a JavaScript function to integrate Rainbow Wallet with a decentralized application (dApp) for token transfers.
Generated: DETERMINISTIC_7b49e2ef720f4c6e
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Integrates Rainbow Wallet with a dApp to facilitate token transfers.
 * This function uses the ethers.js library to interact with the Ethereum blockchain.
 * 
 * Requirements:
 * - The user must have Rainbow Wallet installed and set up.
 * - The dApp must specify the token contract address, recipient address, and token amount.
 * 
 * @param {string} tokenContractAddress - The address of the ERC-20 token contract.
 * @param {string} recipientAddress - The recipient's wallet address.
 * @param {string} amount - The amount of tokens to transfer (in string format to handle decimals).
 * @returns {Promise<void>} Resolves if the transaction succeeds, rejects if it fails.
 */
async function integrateRainbowWalletForTokenTransfer(tokenContractAddress, recipientAddress, amount) {
    try {
        // Check if the browser has Ethereum provider (Rainbow Wallet)
        if (typeof window.ethereum === 'undefined') {
            throw new Error('Rainbow Wallet is not detected. Please install or open Rainbow Wallet.');
        }

        // Request account access from the user
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send('eth_requestAccounts', []);

        // Get the signer (the user interacting with the dApp)
        const signer = provider.getSigner();

        // Validate addresses and parameters
        if (!ethers.utils.isAddress(tokenContractAddress)) {
            throw new Error('Invalid token contract address.');
        }
        if (!ethers.utils.isAddress(recipientAddress)) {
            throw new Error('Invalid recipient address.');
        }
        if (isNaN(amount) || parseFloat(amount) <= 0) {
            throw new Error('Invalid token amount.');
        }

        // Create an instance of the ERC-20 token contract
        const tokenABI = [
            // Minimal ERC-20 ABI to interact with the `transfer` function
            "function transfer(address to, uint256 amount) public returns (bool)"
        ];
        const tokenContract = new ethers.Contract(tokenContractAddress, tokenABI, signer);

        // Convert the token amount to BigNumber format (considering 18 decimals for ERC-20 tokens)
        const decimals = 18; // Adjust decimals based on the token
        const tokenAmount = ethers.utils.parseUnits(amount, decimals);

        // Execute the token transfer
        const tx = await tokenContract.transfer(recipientAddress, tokenAmount);

        console.log('Transaction sent. Waiting for confirmation...');
        
        // Wait for the transaction to be mined
        await tx.wait();

        console.log('Transaction confirmed! Tokens transferred successfully.');
    } catch (error) {
        // Handle and log errors
        console.error(error.message);
        alert(`Error: ${error.message}`);
    }
}
```
