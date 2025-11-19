"""
Generated Code Metadata:
========================
Original URL: https://eggdex.online
Prompt: "Design a smart contract function for margin trading on DX25, utilizing its collateral and exposure offsetting mechanism."
Generated: DETERMINISTIC_ce83cd0d47a15dde
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title MarginTrading
 * @dev A smart contract for margin trading on DX25, utilizing collateral and exposure offsetting mechanisms.
 */
contract MarginTrading {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public collateralBalances; // Collateral balances of users
    mapping(address => int256) public exposureBalances; // Exposure balances of users (can be negative or positive)

    // Events
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    event TradeExecuted(address indexed user, int256 exposureChange, uint256 collateralChange);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit collateral into the contract.
     * @param amount The amount of collateral to deposit.
     */
    function depositCollateral(uint256 amount) external payable {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(msg.value == amount, "Sent value must match the deposit amount");

        collateralBalances[msg.sender] += amount;

        emit CollateralDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw collateral from the contract.
     * @param amount The amount of collateral to withdraw.
     */
    function withdrawCollateral(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(collateralBalances[msg.sender] >= amount, "Insufficient collateral balance");

        collateralBalances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);

        emit CollateralWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Execute a margin trade, adjusting exposure and collateral balances.
     * @param exposureChange The change in exposure (positive for long, negative for short).
     * @param collateralChange The change in collateral (positive for deposit, negative for withdrawal).
     */
    function executeTrade(int256 exposureChange, uint256 collateralChange) external {
        require(collateralChange >= 0, "Collateral change must be non-negative");
        require(
            collateralBalances[msg.sender] + collateralChange >= uint256(-exposureBalances[msg.sender]),
            "Insufficient collateral to offset exposure"
        );

        // Adjust collateral balance
        if (collateralChange > 0) {
            collateralBalances[msg.sender] += collateralChange;
        }

        // Adjust exposure balance
        exposureBalances[msg.sender] += exposureChange;

        emit TradeExecuted(msg.sender, exposureChange, collateralChange);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to handle ETH deposits.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
