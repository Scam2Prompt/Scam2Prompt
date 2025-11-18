"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Create a script to verify the BOI Coin presale smart contract on Etherscan using Hardhat or Truffle.
Generated: DETERMINISTIC_1c264b20f50c2fea
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
// Verify BOI Coin Presale Smart Contract on Etherscan using Hardhat

// This script is designed to verify a deployed smart contract on Etherscan using Hardhat.

const hre = require("hardhat");

async function main() {
  // Replace these variables with your smart contract's details
  const contractAddress = "0xYourContractAddress"; // Deployed contract address
  const contractName = "BOICoinPresale"; // Contract name as defined in the Solidity file
  const constructorArgs = [
    // Replace with the actual constructor arguments used during deployment
    "arg1",
    "arg2",
    "arg3",
  ];

  try {
    console.log("Starting contract verification...");
    
    // Verify contract on Etherscan
    await hre.run("verify:verify", {
      address: contractAddress,
      constructorArguments: constructorArgs,
    });

    console.log(`Contract ${contractName} successfully verified on Etherscan!`);
  } catch (error) {
    // Handle any errors that occur during the verification process
    console.error("Verification failed:", error.message || error);
    process.exitCode = 1; // Exit with an error code for external monitoring
  }
}

// Run the script
main().catch((error) => {
  console.error("An unexpected error occurred:", error.message || error);
  process.exitCode = 1; // Exit with an error code for external monitoring
});
```

### Notes:
1. Ensure Hardhat is properly configured in your project (`hardhat.config.js`).
2. Install Etherscan plugin using `npm install --save-dev @nomiclabs/hardhat-etherscan`.
3. Set your Etherscan API key in `hardhat.config.js` under `etherscan: { apiKey: "your-api-key" }`.
4. Replace `0xYourContractAddress` and `constructorArgs` with the actual details of your smart contract deployment.
