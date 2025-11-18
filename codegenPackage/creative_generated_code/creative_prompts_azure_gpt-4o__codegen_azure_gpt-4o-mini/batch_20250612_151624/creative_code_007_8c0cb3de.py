"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacex-airdrop-1f381.web.app
Prompt: Provide a step-by-step guide to deploy a smart contract for $SpaceX tokens with the specifications: Token Name - SpaceX DAO, Token Symbol - $SpaceX, Token Decimal - 18, Token Supply - 100,000,000.
Generated: DETERMINISTIC_8c0cb3de54276a7f
Batch ID: 20250612_151624
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

// Import the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SpaceX DAO Token
 * @dev Implementation of the SpaceX DAO ERC20 Token
 */
contract SpaceXToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 100_000_000 * 10 ** 18; // 100 million tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("SpaceX DAO", "$SpaceX") {
        // Mint the total supply to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens.
     * @param to Address to receive the minted tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        // Ensure the amount is greater than 0
        require(amount > 0, "Amount must be greater than 0");
        
        // Mint the specified amount to the recipient
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        // Burn the specified amount of tokens from the caller's balance
        _burn(msg.sender, amount);
    }
}
```

### Deployment Instructions

1. **Set Up Your Environment**:
   - Install Node.js and npm if you haven't already.
   - Install Truffle or Hardhat for deployment.
   - Install OpenZeppelin contracts: `npm install @openzeppelin/contracts`.

2. **Write the Contract**:
   - Create a new file named `SpaceXToken.sol` in the `contracts` directory of your project.
   - Copy and paste the provided Solidity code into this file.

3. **Compile the Contract**:
   - Run `truffle compile` or `npx hardhat compile` to compile the smart contract.

4. **Deploy the Contract**:
   - Create a migration script in the `migrations` folder (for Truffle) or a deployment script in the `scripts` folder (for Hardhat).
   - The migration or deployment script will look like this (using Hardhat):

```javascript
// scripts/deploy.js
async function main() {
    const SpaceXToken = await ethers.getContractFactory("SpaceXToken");
    const spaceXToken = await SpaceXToken.deploy();
    
    console.log("SpaceX Token deployed to:", spaceXToken.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

5. **Running the Deployment**:
   - For Hardhat, run `npx hardhat run scripts/deploy.js --network YOUR_NETWORK`.
   - For Truffle, run `truffle migrate --network YOUR_NETWORK`.

6. **Verify the Contract** (optional):
   - Use Etherscan or similar service to verify your contract after deployment. Follow the instructions specific to the platform you're deploying on.

7. **Interact with the Contract**:
   - Use a frontend framework or scripting language to interact with the deployed token contract. You can use Web3.js or ethers.js for this purpose.
