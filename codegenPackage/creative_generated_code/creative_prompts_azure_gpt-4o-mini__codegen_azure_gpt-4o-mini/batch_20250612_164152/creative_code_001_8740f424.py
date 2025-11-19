"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Write a script to connect a wallet and mint a .linea username, including handling the pricing structure for different name lengths.
Generated: DETERMINISTIC_8740f424dd92d8d1
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const ethers = require('ethers');

// Constants for the minting process
const NAME_PRICE = {
    3: ethers.utils.parseEther("0.01"), // 3 characters: 0.01 ETH
    4: ethers.utils.parseEther("0.02"), // 4 characters: 0.02 ETH
    5: ethers.utils.parseEther("0.03"), // 5 characters: 0.03 ETH
    // Extend pricing for longer names if needed
};

// Smart contract address and ABI (simplified for minting)
const CONTRACT_ADDRESS = 'your_contract_address_here';
const CONTRACT_ABI = [
    // Minimal ABI for the mint function
    "function mint(string memory name) public payable"
];

// Function to connect wallet and mint a username
async function mintUsername(username) {
    try {
        // Check if username is valid
        const nameLength = username.length;
        if (nameLength < 3 || nameLength > 5) {
            throw new Error("Username must be between 3 and 5 characters.");
        }

        // Get price for the username length
        const price = NAME_PRICE[nameLength];
        if (!price) {
            throw new Error("Price not defined for this username length.");
        }

        // Connect to the Ethereum wallet using ethers.js
        if (!window.ethereum) {
            throw new Error("Ethereum wallet not found. Please install MetaMask.");
        }
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Create contract instance
        const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

        // Mint the username
        const tx = await contract.mint(username, { value: price });
        console.log("Transaction sent:", tx.hash);

        // Wait for the transaction to be confirmed
        const receipt = await tx.wait();
        console.log("Transaction confirmed:", receipt.transactionHash);

        return receipt;
    } catch (error) {
        console.error("Error minting username:", error.message);
        throw error; // Rethrow error for handling in higher context if needed
    }
}

// Example usage
(async () => {
    try {
        const username = "test"; // Replace with user input
        const receipt = await mintUsername(username);
        console.log("Username minted successfully:", receipt);
    } catch (error) {
        console.error("Minting failed:", error);
    }
})();
```
