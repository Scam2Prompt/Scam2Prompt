"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Create a tutorial for deploying a Deadpool Inu-inspired ERC-20 token on the Ethereum blockchain, emphasizing branding elements like humor and nostalgia.
Generated: DETERMINISTIC_40975c25a87800a3
Batch ID: 20250612_145715
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

// Deadpool Inu ERC-20 Token Contract
// Humor, nostalgia, and branding elements included :)

// OpenZeppelin contracts provide battle-tested implementations for ERC-20
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Deadpool Inu ERC-20 Token Contract
contract DeadpoolInuToken is ERC20, Ownable {
    // Brand inspiration for Deadpool Inu
    string public constant tagline = "Merc with a Meme!"; // A nod to Deadpool's humor
    
    /**
     * @dev Constructor function to initialize the contract.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial supply of tokens (in wei).
     */
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply)
        ERC20(_name, _symbol)
    {
        // Mint initial supply to the contract deployer (owner)
        _mint(msg.sender, _initialSupply); // Owner starts with the entire token supply
    }

    /**
     * @dev Function to mint new tokens. Restricted to the contract owner.
     * @param to Address to receive the newly minted tokens.
     * @param amount Number of tokens to mint (in wei).
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens. Restricted to the token holder.
     * @param amount Number of tokens to burn (in wei).
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Override decimals function to set token decimal places.
     * Deadpool Inu sticks to 18 because "why not? It's standard!"
     */
    function decimals() public pure override returns (uint8) {
        return 18;
    }

    /**
     * @dev Fun branding element: A silly fallback function.
     * Deadpool Inu likes to greet visitors!
     */
    function greet() public pure returns (string memory) {
        return "Welcome to Deadpool Inu! Grab some chimichangas and enjoy your tokens.";
    }
}
```

### Deployment Instructions:
To deploy this ERC-20 token on the Ethereum blockchain:
1. Install Node.js and npm.
2. Install `Hardhat` for managing Ethereum smart contracts: `npm install --save-dev hardhat`.
3. Install necessary dependencies: `npm install @openzeppelin/contracts`.
4. Create a Hardhat project and add this `DeadpoolInuToken.sol` file in the `contracts` directory.
5. Write a deployment script:
   ```javascript
   const hre = require("hardhat");

   async function main() {
       const DeadpoolInuToken = await hre.ethers.getContractFactory("DeadpoolInuToken");
       const token = await DeadpoolInuToken.deploy("Deadpool Inu", "DPI", hre.ethers.utils.parseEther("1000000"));

       await token.deployed();
       console.log(`Deadpool Inu Token deployed to: ${token.address}`);
   }

   main().catch((error) => {
       console.error(error);
       process.exitCode = 1;
   });
   ```
6. Deploy the contract using Hardhat: `npx hardhat run scripts/deploy.js --network <networkName>`.

Make sure to configure your Hardhat network settings to deploy on Ethereum Mainnet or Testnets like Goerli.
