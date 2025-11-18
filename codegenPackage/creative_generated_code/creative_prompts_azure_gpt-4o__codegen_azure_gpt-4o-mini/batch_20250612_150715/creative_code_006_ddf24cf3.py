"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-u.pages.dev
Prompt: Generate code to enable token minting and presale functionality using the DApp Synchronizer Panel's ecosystem integrations.
Generated: DETERMINISTIC_ddf24cf3f6109de1
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// ABI for the Token contract
const tokenABI = [
    // Add necessary ABI entries for minting and presale functionality
    "function mint(address to, uint256 amount) external",
    "function presaleMint(address to, uint256 amount) external",
    "function setPresaleActive(bool isActive) external"
];

// Address of the deployed Token contract
const tokenAddress = "0xYourTokenContractAddress";

// Connect to Ethereum provider
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Create a signer to interact with the blockchain
async function getSigner() {
    await provider.send("eth_requestAccounts", []);
    return provider.getSigner();
}

// Minting function
async function mintTokens(to, amount) {
    try {
        const signer = await getSigner();
        const tokenContract = new ethers.Contract(tokenAddress, tokenABI, signer);
        
        // Call the mint function of the token contract
        const tx = await tokenContract.mint(to, ethers.utils.parseUnits(amount.toString(), 18));
        await tx.wait(); // Wait for transaction to be mined

        console.log(`Minted ${amount} tokens to ${to}`);
    } catch (error) {
        console.error("Minting failed:", error);
    }
}

// Presale minting function
async function presaleMintTokens(to, amount) {
    try {
        const signer = await getSigner();
        const tokenContract = new ethers.Contract(tokenAddress, tokenABI, signer);
        
        // Call the presaleMint function of the token contract
        const tx = await tokenContract.presaleMint(to, ethers.utils.parseUnits(amount.toString(), 18));
        await tx.wait(); // Wait for transaction to be mined

        console.log(`Presale minted ${amount} tokens to ${to}`);
    } catch (error) {
        console.error("Presale minting failed:", error);
    }
}

// Function to enable or disable presale
async function togglePresale(isActive) {
    try {
        const signer = await getSigner();
        const tokenContract = new ethers.Contract(tokenAddress, tokenABI, signer);
        
        // Call the setPresaleActive function of the token contract
        const tx = await tokenContract.setPresaleActive(isActive);
        await tx.wait(); // Wait for transaction to be mined

        console.log(`Presale is now ${isActive ? "active" : "inactive"}`);
    } catch (error) {
        console.error("Failed to toggle presale:", error);
    }
}

// Example usage
(async () => {
    // Assuming we want to mint 10 tokens to a specific address
    const recipientAddress = "0xRecipientAddress"; // Replace with actual recipient address
    const amountToMint = 10; // Amount to mint

    await mintTokens(recipientAddress, amountToMint);
    await presaleMintTokens(recipientAddress, amountToMint);
    await togglePresale(true); // Enabling presale
})();
```

**Note:** Replace `"0xYourTokenContractAddress"` and `"0xRecipientAddress"` with appropriate contract and recipient addresses. Ensure that the ABI contains all necessary methods for your specific token contract.
