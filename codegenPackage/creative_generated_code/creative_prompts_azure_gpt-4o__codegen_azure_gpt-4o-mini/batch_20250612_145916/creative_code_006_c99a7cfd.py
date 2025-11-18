"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator.pages.dev
Prompt: Create a token deployment script in Solidity that mirrors the functionality of Tokens Creator, including support for multiple networks like BNB Smart Chain TestNet and Avalanche.
Generated: DETERMINISTIC_c99a7cfd88fc070d
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 contract and Ownable for access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token contract that inherits from ERC20 and Ownable
contract CustomToken is ERC20, Ownable {
    // Constructor to initialize the token with name and symbol
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Function to mint new tokens, only accessible by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to burn tokens, only accessible by the owner
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}

// Deployment script for the CustomToken contract
// This script should be executed in a JavaScript environment like Hardhat or Truffle
async function main() {
    // Get the contract factory
    const Token = await ethers.getContractFactory("CustomToken");

    // Define token parameters
    const name = "My Custom Token";
    const symbol = "MCT";
    const initialSupply = 1000000; // 1 million tokens

    // Deploy the contract
    const token = await Token.deploy(name, symbol, initialSupply);
    
    // Wait for the deployment to be confirmed
    await token.deployed();

    console.log("Token deployed to:", token.address);
}

// Error handling for the deployment script
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

Make sure to set up a development environment with Hardhat or Truffle to deploy this contract on the BNB Smart Chain TestNet or Avalanche. Also, ensure you have the necessary configurations in place for the network you intend to deploy to, including provider URLs and wallet private keys.
