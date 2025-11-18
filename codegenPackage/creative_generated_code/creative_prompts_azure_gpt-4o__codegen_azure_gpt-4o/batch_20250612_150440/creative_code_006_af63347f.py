"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-uswallet.godaddysites.com
Prompt: Create a script to handle token transfers using MetaMask, referencing specific use cases or examples from the MetaMask Wallet website.
Generated: DETERMINISTIC_af63347fd518a5ff
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required library for interacting with Ethereum
const ethers = require('ethers');

// Function to transfer tokens using MetaMask
async function transferTokens({ contractAddress, recipientAddress, amount, tokenDecimals }) {
    try {
        // Check if MetaMask is installed
        if (!window.ethereum) {
            throw new Error("MetaMask is not installed. Please install it to proceed.");
        }

        // Request MetaMask to connect to the user's wallet
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create a new provider and signer from MetaMask
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // ABI for ERC20 token standard
        const ERC20_ABI = [
            "function transfer(address to, uint256 amount) public returns (bool)"
        ];

        // Connect to the ERC20 token contract
        const tokenContract = new ethers.Contract(contractAddress, ERC20_ABI, signer);

        // Convert the token amount to the correct decimal format
        const parsedAmount = ethers.utils.parseUnits(amount.toString(), tokenDecimals);

        // Initiate the transfer
        const transaction = await tokenContract.transfer(recipientAddress, parsedAmount);

        console.log("Transaction initiated, waiting for confirmation...");

        // Wait for the transaction to be mined
        const receipt = await transaction.wait();

        console.log("Transaction successful!", receipt);
        return receipt;
    } catch (error) {
        console.error("Error occurred during token transfer:", error.message);
        throw error;
    }
}

// Example usage of transferTokens function
(async () => {
    try {
        const transferDetails = {
            contractAddress: "0xYourTokenContractAddressHere", // Replace with your token contract address
            recipientAddress: "0xRecipientAddressHere",       // Replace with the recipient's address
            amount: "10",                                     // Replace with the token amount to transfer
            tokenDecimals: 18                                 // Replace with the token's decimal precision
        };

        const result = await transferTokens(transferDetails);
        console.log("Transfer completed successfully:", result);
    } catch (error) {
        console.error("Transfer failed:", error);
    }
})();
```

### Notes:
1. Replace `0xYourTokenContractAddressHere` and `0xRecipientAddressHere` with actual addresses.
2. Ensure the script is executed in a browser environment with MetaMask installed.
3. Run `npm install ethers` to install the `ethers` library if not already done.
