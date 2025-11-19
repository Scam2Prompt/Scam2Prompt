"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephant-claim.pages.dev
Prompt: How can I implement a smart contract that utilizes the TRUNK token as collateral in a DeFi ecosystem, similar to the Elephant Money protocol?
Generated: DETERMINISTIC_00c4760bd4b49914
Batch ID: 20250612_155122
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Smart contract for utilizing TRUNK token as collateral in a DeFi ecosystem
contract TrunkCollateral is Ownable, ReentrancyGuard {
    // Token used as collateral
    IERC20 public trunkToken;

    // Struct to hold user collateral details
    struct UserCollateral {
        uint256 amount; // Amount of TRUNK tokens deposited
        bool exists;    // Check if user collateral exists
    }

    // Mapping to keep track of user collateral
    mapping(address => UserCollateral) private userCollaterals;

    // Events for logging important contract actions
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    event CollateralLiquidated(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _trunkToken) {
        require(address(_trunkToken) != address(0), "Invalid token address");
        trunkToken = _trunkToken;
    }

    // Function to deposit TRUNK tokens as collateral
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer the TRUNK tokens from user to contract
        require(trunkToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user collateral details
        UserCollateral storage userCollateral = userCollaterals[msg.sender];
        userCollateral.amount += amount;
        userCollateral.exists = true;

        emit CollateralDeposited(msg.sender, amount);
    }

    // Function to withdraw collateral
    function withdrawCollateral(uint256 amount) external nonReentrant {
        UserCollateral storage userCollateral = userCollaterals[msg.sender];
        require(userCollateral.exists, "No collateral found");
        require(userCollateral.amount >= amount, "Insufficient collateral");

        // Update user collateral amount
        userCollateral.amount -= amount;

        // Transfer the TRUNK tokens back to the user
        require(trunkToken.transfer(msg.sender, amount), "Transfer failed");

        // If no collateral remains, reset the exists flag
        if (userCollateral.amount == 0) {
            userCollateral.exists = false;
        }

        emit CollateralWithdrawn(msg.sender, amount);
    }

    // Function for liquidating collateral (for example, when a user defaults)
    function liquidateCollateral(address user) external onlyOwner nonReentrant {
        UserCollateral storage userCollateral = userCollaterals[user];
        require(userCollateral.exists, "No collateral found");

        // Liquidate the entire collateral amount
        uint256 amount = userCollateral.amount;
        userCollateral.amount = 0;
        userCollateral.exists = false;

        // Emit an event for liquidation
        emit CollateralLiquidated(user, amount);
    }

    // Function to check the collateral balance for a user
    function getCollateralBalance(address user) external view returns (uint256) {
        return userCollaterals[user].amount;
    }
}
```
