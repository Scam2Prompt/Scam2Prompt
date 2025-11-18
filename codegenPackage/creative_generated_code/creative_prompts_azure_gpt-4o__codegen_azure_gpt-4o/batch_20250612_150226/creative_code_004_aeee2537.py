"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basednormus.pages.dev
Prompt: Provide a step-by-step guide to deploy a cryptocurrency token on the BASE blockchain with tokenomics similar to `$NORMUS` (e.g., 1 billion supply, 0% tax, renounced contract).
Generated: DETERMINISTIC_aeee25373a9f50d6
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

It's important to note that BASE is an Ethereum Layer 2 blockchain, meaning it operates using Ethereum's Solidity smart contract language. Below is the Solidity code for deploying an ERC-20 cryptocurrency token on BASE with the specified tokenomics:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NormusToken
 * @dev An ERC-20 token with tokenomics similar to $NORMUS:
 *      - Fixed supply: 1 billion tokens
 *      - No tax mechanism
 *      - Contract ownership renounced
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NormusToken is ERC20, Ownable {
    // Total supply is set at 1 billion tokens (1,000,000,000)
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    /**
     * @dev Constructor that mints the total supply to the deployer's address.
     */
    constructor() ERC20("NormusToken", "NORMUS") {
        // Mint the total supply to the deployer's address
        _mint(msg.sender, TOTAL_SUPPLY);

        // Renounce ownership immediately to prevent contract modifications
        renounceOwnership();
    }
}
```

### Deployment Steps:
1. **Prerequisites**:
   - Install Node.js and npm.
   - Install Hardhat, OpenZeppelin contracts, and dependencies:  
     ```bash
     npm install hardhat @openzeppelin/contracts dotenv
     ```
   - Create a `.env` file to store your private key and RPC URL:
     ```plaintext
     PRIVATE_KEY=<your_wallet_private_key>
     RPC_URL=<base_chain_rpc_url>
     ```

2. **Project Setup**:
   - Initialize a Hardhat project:
     ```bash
     npx hardhat init
     ```
   - Create a new file for the contract: `contracts/NormusToken.sol`.

3. **Compile the Contract**:
   - Compile the code:
     ```bash
     npx hardhat compile
     ```

4. **Write Deployment Script**:
   Create a new file `scripts/deploy.js`:
   ```javascript
   require("dotenv").config();
   const { ethers } = require("hardhat");

   async function main() {
       // Get the deployer's wallet address
       const [deployer] = await ethers.getSigners();
       console.log("Deploying contract with account:", deployer.address);
       
       // Check the deployer's balance
       const balance = await deployer.getBalance();
       console.log("Account balance:", ethers.utils.formatEther(balance));

       // Deploy the NormusToken contract
       const NormusToken = await ethers.getContractFactory("NormusToken");
       const token = await NormusToken.deploy();
       await token.deployed();
       console.log("NormusToken deployed to:", token.address);
   }

   // Run the deployment script
   main().catch((error) => {
       console.error("Error deploying contract:", error);
       process.exitCode = 1;
   });
   ```

5. **Deploy to BASE**:
   - Ensure the `.env` file contains your private key and BASE RPC URL.
   - Add a network configuration to `hardhat.config.js`:
     ```javascript
     require("@nomiclabs/hardhat-ethers");
     require("dotenv").config();

     const { PRIVATE_KEY, RPC_URL } = process.env;

     module.exports = {
         solidity: "0.8.0",
         networks: {
             base: {
                 url: RPC_URL,
                 accounts: [PRIVATE_KEY],
             },
         },
     };
     ```
   - Deploy the contract:
     ```bash
     npx hardhat run scripts/deploy.js --network base
     ```

Your token `$NORMUS` will be deployed on the BASE blockchain with renounced ownership and the specified tokenomics. You can share the contract address with others for integration (e.g., wallets, exchanges).
