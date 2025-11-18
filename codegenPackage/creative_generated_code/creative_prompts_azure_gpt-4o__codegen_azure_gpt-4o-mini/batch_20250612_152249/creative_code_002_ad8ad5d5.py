"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicatclaim.pages.dev
Prompt: Generate code in JavaScript using ethers.js to connect a Metamask wallet and allow users to purchase $KAI tokens directly from the presale widget.
Generated: DETERMINISTIC_ad8ad5d5ec6561b9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";

// Define the presale contract address and the ABI
const presaleContractAddress = "0xYourPresaleContractAddress"; // Replace with your presale contract address
const presaleContractABI = [
    // Add your presale contract ABI here
    "function buyTokens(uint256 amount) public payable", // Sample function
    "function getTokenPrice() public view returns (uint256)" // Sample function to retrieve token price
];

// Initialize connection variables
let provider;
let signer;
let presaleContract;

// Function to connect to Metamask wallet
async function connectWallet() {
    if (typeof window.ethereum === 'undefined') {
        alert("Metamask is not installed. Please install it to continue.");
        return;
    }

    try {
        // Request wallet connection
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        provider = new ethers.providers.Web3Provider(window.ethereum);
        signer = provider.getSigner();
        presaleContract = new ethers.Contract(presaleContractAddress, presaleContractABI, signer);
        console.log("Wallet connected successfully.");
    } catch (error) {
        console.error("Failed to connect wallet:", error);
    }
}

// Function to purchase tokens
async function purchaseTokens(amount) {
    try {
        // Retrieve the token price from the presale contract
        const tokenPrice = await presaleContract.getTokenPrice();
        
        // Calculate total cost in wei
        const totalCost = tokenPrice.mul(amount);

        // Execute the buyTokens function in the contract
        const tx = await presaleContract.buyTokens(amount, { value: totalCost });

        // Wait for transaction confirmation
        await tx.wait();
        console.log(`Successfully purchased ${amount} tokens.`);
    } catch (error) {
        console.error("Token purchase failed:", error);
    }
}

// Event listeners for connect button and purchase button
document.getElementById("connectButton").addEventListener("click", connectWallet);
document.getElementById("purchaseButton").addEventListener("click", () => {
    const amount = document.getElementById("amountInput").value;
    purchaseTokens(ethers.utils.parseUnits(amount, 18)); // Assuming 18 decimals for $KAI
});

// HTML Elements:
// <button id="connectButton">Connect Wallet</button>
// <input type="text" id="amountInput" placeholder="Amount to purchase" />
// <button id="purchaseButton">Purchase $KAI Tokens</button>
```
