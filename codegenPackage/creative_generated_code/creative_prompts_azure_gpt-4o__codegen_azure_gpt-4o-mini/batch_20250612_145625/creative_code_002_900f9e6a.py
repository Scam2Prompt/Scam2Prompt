"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btceftoken.pages.dev
Prompt: Develop a JavaScript function using ethers.js to connect a wallet and facilitate the purchase of BTCETF tokens during the presale phase, ensuring compatibility with ETH, USDT, and BNB payments.
Generated: DETERMINISTIC_900f9e6ac37cc4aa
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
const { ethers } = require("ethers");

// Define a function to connect to a wallet and purchase BTCETF tokens
async function purchaseBTCEFTokens(paymentToken, amount) {
    // Check if the paymentToken is valid
    const validTokens = ["ETH", "USDT", "BNB"];
    if (!validTokens.includes(paymentToken)) {
        throw new Error("Invalid payment token. Please use ETH, USDT, or BNB.");
    }

    // Connect to the Ethereum network
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    
    // Request wallet connection
    await provider.send("eth_requestAccounts", []);
    
    // Get signer object for transactions
    const signer = provider.getSigner();
    
    // Define contract details (replace with actual contract address and ABI)
    const contractAddress = "0xYourContractAddress"; // Placeholder address
    const contractABI = [ 
        // Replace with actual contract ABI
        "function purchaseTokens(uint256 amount, address paymentToken) public"
    ];
    
    // Create contract instance
    const contract = new ethers.Contract(contractAddress, contractABI, signer);
    
    // Convert amount to wei (if necessary) and execute purchase
    try {
        const amountInWei = ethers.utils.parseUnits(amount.toString(), 18); // Assuming 18 decimals
        const tx = await contract.purchaseTokens(amountInWei, paymentToken);
        
        // Wait for transaction to be mined
        await tx.wait();
        
        console.log(`Successfully purchased ${amount} BTCETF tokens with ${paymentToken}!`);
    } catch (error) {
        console.error("Transaction failed:", error);
        throw new Error("Transaction failed. Please check the console for details.");
    }
}

// Example usage
// Call the purchase function when needed with the desired parameters
// purchaseBTCEFTokens("ETH", 1);
```

**Note:** Replace `"0xYourContractAddress"` and the contract ABI with the actual values for the BTCETF token contract before executing the code.
