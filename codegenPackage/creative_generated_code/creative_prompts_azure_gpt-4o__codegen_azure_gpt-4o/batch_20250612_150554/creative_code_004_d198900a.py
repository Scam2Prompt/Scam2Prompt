"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arteratoken.lucaageadesign.com
Prompt: Create a JavaScript function using ethers.js to interact with the Artera Token contract and display the token balance of a connected MetaMask wallet.
Generated: DETERMINISTIC_d198900aa2689eeb
Batch ID: 20250612_150554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library
const { ethers } = require('ethers');

// Function to get the Artera Token balance of a connected MetaMask wallet
async function getArteraTokenBalance(contractAddress, walletAddress, provider) {
    try {
        // ABI for ERC-20 Token (minimum needed to access balanceOf and decimals)
        const erc20Abi = [
            // balanceOf function
            "function balanceOf(address owner) view returns (uint256)",
            // decimals function
            "function decimals() view returns (uint8)"
        ];

        // Connect to the Artera Token contract
        const contract = new ethers.Contract(contractAddress, erc20Abi, provider);

        // Fetch the token balance of the wallet
        const rawBalance = await contract.balanceOf(walletAddress);

        // Get the token decimals
        const decimals = await contract.decimals();

        // Format the balance (convert from raw value to human-readable)
        const formattedBalance = ethers.utils.formatUnits(rawBalance, decimals);

        // Return the formatted balance
        return formattedBalance;
    } catch (error) {
        // Handle and log any errors
        console.error("Failed to fetch token balance:", error);
        throw new Error("Unable to fetch token balance. Please check the contract address, wallet address, or provider.");
    }
}

// Example usage
(async () => {
    try {
        // Replace with Artera Token contract address
        const contractAddress = "0xYourArteraTokenContractAddress";

        // Replace with user's wallet address (connected via MetaMask)
        const walletAddress = "0xUserMetaMaskWalletAddress";

        // Connect to Ethereum provider (MetaMask injected provider)
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Request account access if necessary
        await provider.send("eth_requestAccounts", []);

        // Get the balance
        const balance = await getArteraTokenBalance(contractAddress, walletAddress, provider);

        // Display the balance
        console.log(`Token Balance: ${balance}`);
    } catch (error) {
        console.error("Error:", error.message);
    }
})();
```
