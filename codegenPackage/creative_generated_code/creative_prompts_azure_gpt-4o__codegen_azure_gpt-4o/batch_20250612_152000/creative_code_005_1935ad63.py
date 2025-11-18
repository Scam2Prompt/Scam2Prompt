"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Provide step-by-step code examples for deploying a decentralized finance (DeFi) application on Metis Layer 2 using AAVE.
Generated: DETERMINISTIC_1935ad6321693a06
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title DeFi Lending and Borrowing on Metis Layer 2 with AAVE
 * @dev This contract demonstrates deploying a simple DeFi application integrated with AAVE on Metis Layer 2.
 */

// Import required interfaces from AAVE
import "@aave/core-v3/contracts/interfaces/IPool.sol";
import "@aave/core-v3/contracts/interfaces/IPoolAddressesProvider.sol";

contract DeFiOnMetis {
    // State variables
    IPoolAddressesProvider public immutable addressesProvider;
    IPool public immutable lendingPool;

    constructor(address _addressesProvider) {
        // Initialize the AAVE PoolAddressesProvider
        addressesProvider = IPoolAddressesProvider(_addressesProvider);

        // Fetch the LendingPool address from the provider
        lendingPool = IPool(addressesProvider.getPool());
    }

    /**
     * @dev Deposit ERC20 tokens into AAVE's LendingPool.
     * @param asset The address of the ERC20 token to deposit.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(address asset, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Approve the LendingPool to spend user's tokens
        IERC20(asset).approve(address(lendingPool), amount);

        // Deposit the token into AAVE LendingPool
        lendingPool.deposit(asset, amount, msg.sender, 0);
    }

    /**
     * @dev Withdraw ERC20 tokens from AAVE's LendingPool.
     * @param asset The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Withdraw the token from AAVE LendingPool
        lendingPool.withdraw(asset, amount, msg.sender);
    }

    /**
     * @dev Borrow ERC20 tokens from AAVE's LendingPool.
     * @param asset The address of the ERC20 token to borrow.
     * @param amount The amount of tokens to borrow.
     * @param interestRateMode The interest rate mode (1 for stable, 2 for variable).
     */
    function borrow(address asset, uint256 amount, uint256 interestRateMode) external {
        require(amount > 0, "Borrow amount must be greater than zero");
        require(interestRateMode == 1 || interestRateMode == 2, "Invalid interest rate mode");

        // Borrow the token from AAVE LendingPool
        lendingPool.borrow(asset, amount, interestRateMode, 0, msg.sender);
    }

    /**
     * @dev Repay borrowed tokens to AAVE's LendingPool.
     * @param asset The address of the ERC20 token to repay.
     * @param amount The amount of tokens to repay.
     * @param interestRateMode The interest rate mode (1 for stable, 2 for variable).
     */
    function repay(address asset, uint256 amount, uint256 interestRateMode) external {
        require(amount > 0, "Repay amount must be greater than zero");
        require(interestRateMode == 1 || interestRateMode == 2, "Invalid interest rate mode");

        // Approve the LendingPool to spend user's tokens
        IERC20(asset).approve(address(lendingPool), amount);

        // Repay the borrowed amount to AAVE LendingPool
        lendingPool.repay(asset, amount, interestRateMode, msg.sender);
    }
}
```

### Deployment Script (Node.js/Hardhat)
```javascript
// Import required libraries
const { ethers } = require("hardhat");

async function main() {
  // Fetch available accounts
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contract with account:", deployer.address);

  // Replace with the correct PoolAddressesProvider address for Metis Layer 2
  const poolAddressesProvider = "0xYourPoolAddressesProviderAddress";

  // Deploy the contract
  const DeFiOnMetis = await ethers.getContractFactory("DeFiOnMetis");
  const defiContract = await DeFiOnMetis.deploy(poolAddressesProvider);

  await defiContract.deployed();

  console.log("Contract deployed to:", defiContract.address);
}

// Handle errors and execute the deployment script
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

### ERC20 Token Approval Script (Node.js/Hardhat)
```javascript
const { ethers } = require("hardhat");

async function approveToken(tokenAddress, spenderAddress, amount) {
  const [owner] = await ethers.getSigners();
  
  // Connect to the ERC20 contract
  const ERC20 = await ethers.getContractAt("IERC20", tokenAddress, owner);
  
  // Approve the spender to use tokens
  const tx = await ERC20.approve(spenderAddress, amount);
  
  await tx.wait();
  
  console.log(`Approved spender ${spenderAddress} to spend ${amount} tokens from ${owner.address}`);
}

// Example usage
approveToken(
  "0xYourERC20TokenAddress",    // Token address
  "0xYourContractAddress",     // Spender address (e.g., LendingPool)
  ethers.utils.parseEther("100") // Amount to approve (100 tokens)
).catch(console.error);
```

### Notes:
- Replace `"0xYourPoolAddressesProviderAddress"`, `"0xYourERC20TokenAddress"`, and `"0xYourContractAddress"` with actual addresses specific to Metis Layer 2 and AAVE.
- Ensure the ERC20 token contract adheres to the standard interface (`IERC20`).
- Include proper permissions and testing before deploying in production environments.
