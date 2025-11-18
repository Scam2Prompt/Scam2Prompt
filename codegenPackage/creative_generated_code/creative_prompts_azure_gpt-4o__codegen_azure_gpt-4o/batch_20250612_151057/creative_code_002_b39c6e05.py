"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-cys.pages.dev
Prompt: Create a Solidity smart contract that distributes funds from the $ROOST presale according to the specified breakdown: 50% to liquidity pools and 50% for expenses, development, and distribution.
Generated: DETERMINISTIC_b39c6e05f4dfdc38
Batch ID: 20250612_151057
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

/**
 * @title ROOSTPresaleDistribution
 * @dev A smart contract to distribute funds from the $ROOST presale.
 * Funds are distributed as follows:
 * - 50% to liquidity pools
 * - 50% for expenses, development, and distribution
 */
contract ROOSTPresaleDistribution {
    // Address where funds for liquidity will be sent
    address public liquidityAddress;

    // Address where funds for expenses, development, and distribution will be sent
    address public expenseAddress;

    // Owner of the contract
    address public owner;

    // Event emitted when funds are distributed
    event FundsDistributed(uint256 liquidityAmount, uint256 expensesAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set up the initial addresses and ownership.
     * @param _liquidityAddress Address for liquidity pools.
     * @param _expenseAddress Address for expenses, development, and distribution.
     */
    constructor(address _liquidityAddress, address _expenseAddress) {
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_expenseAddress != address(0), "Expense address cannot be zero");

        liquidityAddress = _liquidityAddress;
        expenseAddress = _expenseAddress;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Function to distribute presale funds. Splits the funds 50/50.
     */
    function distributeFunds() external payable {
        require(msg.value > 0, "No funds sent for distribution");

        uint256 half = msg.value / 2;

        // Send 50% to the liquidity address
        (bool liquiditySuccess, ) = liquidityAddress.call{value: half}("");
        require(liquiditySuccess, "Failed to send funds to liquidity address");

        // Send 50% to the expense address
        (bool expenseSuccess, ) = expenseAddress.call{value: half}("");
        require(expenseSuccess, "Failed to send funds to expense address");

        emit FundsDistributed(half, half); // Emit the distribution event
    }

    /**
     * @dev Function to update the liquidity address. Restricted to the owner.
     * @param _newLiquidityAddress New address for liquidity pools.
     */
    function updateLiquidityAddress(address _newLiquidityAddress) external onlyOwner {
        require(_newLiquidityAddress != address(0), "Address cannot be zero");
        liquidityAddress = _newLiquidityAddress;
    }

    /**
     * @dev Function to update the expense address. Restricted to the owner.
     * @param _newExpenseAddress New address for expenses, development, and distribution.
     */
    function updateExpenseAddress(address _newExpenseAddress) external onlyOwner {
        require(_newExpenseAddress != address(0), "Address cannot be zero");
        expenseAddress = _newExpenseAddress;
    }

    /**
     * @dev Function to withdraw any remaining funds in the contract. Restricted to the owner.
     */
    function withdrawBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Failed to withdraw balance");
    }
}
```
