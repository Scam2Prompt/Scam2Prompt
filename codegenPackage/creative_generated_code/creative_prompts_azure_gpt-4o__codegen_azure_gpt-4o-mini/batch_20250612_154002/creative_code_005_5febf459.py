"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-eth.com
Prompt: Create a script to deploy an ERC-20 token contract on the Ethereum network, ensuring compatibility with DeFi protocols mentioned on the ERC20-ETH website.
Generated: DETERMINISTIC_5febf45979651233
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the necessary libraries
const { ethers } = require("hardhat");

// Main function to deploy the ERC-20 token contract
async function main() {
    // Get the signer (account) to deploy the contract
    const [deployer] = await ethers.getSigners();

    console.log("Deploying contracts with the account:", deployer.address);

    // Define the parameters for the ERC-20 token
    const tokenName = "MyToken"; // The name of the token
    const tokenSymbol = "MTK";    // The symbol of the token
    const initialSupply = ethers.utils.parseUnits("1000000", 18); // Initial supply (1 million tokens)

    // Get the contract factory for the ERC-20 token
    const ERC20Token = await ethers.getContractFactory("ERC20Token");

    // Deploy the contract with the provided parameters
    const token = await ERC20Token.deploy(tokenName, tokenSymbol, initialSupply);

    // Wait for the contract to be deployed
    await token.deployed();

    console.log("ERC-20 Token deployed to:", token.address);
}

// Error handling for the main function
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error("Error deploying contract:", error);
        process.exit(1);
    });

// Solidity ERC-20 Token contract code (ERC20Token.sol)
// SPDX-License-Identifier: MIT
// pragma solidity ^0.8.0;

// import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// contract ERC20Token is ERC20 {
//     constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
//         _mint(msg.sender, initialSupply); // Mint the initial supply to the deployer
//     }
// }
```

Make sure to create a separate Solidity file named `ERC20Token.sol` in the same directory with the following code:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ERC20Token is ERC20 {
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        _mint(msg.sender, initialSupply); // Mint the initial supply to the deployer
    }
}
```

### Instructions to Run the Deployment Script:
1. Install Hardhat and OpenZeppelin contracts:
   ```bash
   npm install --save-dev hardhat @openzeppelin/contracts
   ```

2. Save the deployment script in a file named `deploy.js` within the `scripts` directory of your Hardhat project.

3. Save the Solidity contract in a file named `ERC20Token.sol` within the `contracts` directory.

4. Configure Hardhat to connect to your desired Ethereum network (e.g., mainnet, testnet).

5. Run the deployment script:
   ```bash
   npx hardhat run scripts/deploy.js --network yourNetworkName
   ``` 

Replace `yourNetworkName` with the appropriate network configuration in your Hardhat setup.
