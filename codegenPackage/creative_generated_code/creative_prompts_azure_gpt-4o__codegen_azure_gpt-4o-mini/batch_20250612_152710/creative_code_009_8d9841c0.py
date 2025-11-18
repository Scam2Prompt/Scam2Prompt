"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotxyz.pages.dev
Prompt: Create a JavaScript function using ethers.js to query the blockchain for the total amount of $LOOT burnt and calculate the percentage of the total supply that has been burned.
Generated: DETERMINISTIC_8d9841c061b80f12
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library
const { ethers } = require("ethers");

// Define the function to query the total $LOOT burnt and calculate the percentage burned
async function getLootBurnPercentage() {
    // Define the blockchain network and the contract address
    const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");
    const lootContractAddress = "0xf7E3E2D5B6b01B9D2D9Bf0cF509A3E04D22aCaa0"; // Replace with the actual $LOOT token contract address

    // Create a contract instance
    const lootContract = new ethers.Contract(
        lootContractAddress,
        [
            // ABI fragment to get totalSupply and balanceOf
            "function totalSupply() view returns (uint256)",
            "function balanceOf(address owner) view returns (uint256)"
        ],
        provider
    );

    try {
        // Get the total supply of $LOOT tokens
        const totalSupply = await lootContract.totalSupply();

        // Replace with the actual burn address
        const burnAddress = "0x0000000000000000000000000000000000000000"; // This is often the zero address or a designated burn address

        // Get the balance of the burn address
        const burntAmount = await lootContract.balanceOf(burnAddress);

        // Calculate the percentage of tokens burnt
        const burntPercentage = (burntAmount / totalSupply) * 100;

        // Log the results
        console.log(`Total $LOOT Burnt: ${ethers.utils.formatUnits(burntAmount, 18)} $LOOT`);
        console.log(`Percentage Burnt: ${burntPercentage.toFixed(2)}%`);
    } catch (error) {
        // Handle any errors that occur during the execution
        console.error("Error querying the blockchain:", error);
    }
}

// Call the function to execute
getLootBurnPercentage();
```

**Note:** Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID, and verify the correct contract address and burn address for the $LOOT token.
