"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Create a script to verify the BOI Coin presale smart contract on Etherscan using Hardhat or Truffle.
Generated: DETERMINISTIC_1c264b20f50c2fea
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require("hardhat");
const { run } = require("hardhat");

async function verifyBOICoinPresale() {
  try {
    // Get the deployed contract address (replace with your actual contract address)
    const contractAddress = "0x123..."; // Replace with your contract address
    
    // Get the contract factory
    const BOICoinPresale = await ethers.getContractFactory("BOICoinPresale");
    
    // Attach to the deployed contract
    const boiCoinPresale = await BOICoinPresale.attach(contractAddress);
    
    console.log("Verifying BOI Coin Presale contract on Etherscan...");
    
    // Verify the contract
    await run("verify:verify", {
      address: contractAddress,
      constructorArguments: [], // Add constructor arguments if any
    });
    
    console.log("BOI Coin Presale contract verified successfully!");
  } catch (error) {
    console.error("Error verifying BOI Coin Presale contract:", error.message);
    process.exit(1);
  }
}

// Execute the verification
verifyBOICoinPresale()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```
