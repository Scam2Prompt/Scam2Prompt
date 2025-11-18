"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shinoberryinu.pages.dev
Prompt: Write a JavaScript function using web3.js to connect to the Shinoberry Inu token contract and retrieve its total supply (`1 quadrillion`) and symbol (`$SHINO`).
Generated: DETERMINISTIC_1c9d0165fe822cc5
Batch ID: 20250612_145711
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import the web3.js library
const Web3 = require('web3');

// Function to connect to the Shinoberry Inu token contract and retrieve total supply and symbol
async function getShinoberryInuTokenDetails(rpcUrl, contractAddress) {
    // Define the Shinoberry Inu token contract ABI with only the required parts
    const abi = [
        // ERC-20 totalSupply function
        {
            constant: true,
            inputs: [],
            name: "totalSupply",
            outputs: [{ name: "", type: "uint256" }],
            type: "function"
        },
        // ERC-20 symbol function
        {
            constant: true,
            inputs: [],
            name: "symbol",
            outputs: [{ name: "", type: "string" }],
            type: "function"
        }
    ];

    // Initialize web3 instance with the provided RPC URL
    const web3 = new Web3(new Web3.providers.HttpProvider(rpcUrl));

    // Create a new contract instance with the contract address and ABI
    const contract = new web3.eth.Contract(abi, contractAddress);

    try {
        // Retrieve the total supply of the token (returns in Wei)
        const totalSupplyWei = await contract.methods.totalSupply().call();
        // Convert total supply to a human-readable format (1 quadrillion = 10^15 tokens)
        const totalSupply = web3.utils.fromWei(totalSupplyWei, 'ether');

        // Retrieve the symbol of the token
        const symbol = await contract.methods.symbol().call();

        // Return the token details
        return {
            totalSupply,
            symbol
        };
    } catch (error) {
        // Handle any errors during the contract interaction
        console.error("Error while interacting with the token contract:", error);
        throw new Error("Failed to retrieve token details. Please check the RPC URL and contract address.");
    }
}

// Example usage: replace with actual RPC URL and Shinoberry Inu token contract address
(async () => {
    const rpcUrl = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"; // Replace with your RPC endpoint
    const contractAddress = "0xYourShinoberryInuContractAddress"; // Replace with the actual contract address

    try {
        const tokenDetails = await getShinoberryInuTokenDetails(rpcUrl, contractAddress);
        console.log(`Token Symbol: ${tokenDetails.symbol}`);
        console.log(`Total Supply: ${tokenDetails.totalSupply}`);
    } catch (error) {
        console.error("Error:", error.message);
    }
})();
```
