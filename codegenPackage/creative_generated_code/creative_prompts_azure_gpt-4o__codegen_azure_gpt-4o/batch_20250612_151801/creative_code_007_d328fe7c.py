"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Write a Solidity smart contract function to manage the treasury's role in topping up the staking pool and liquidity pool for DigiToads.
Generated: DETERMINISTIC_d328fe7c15f2eaac
Batch ID: 20250612_151801
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
 * @title DigiToadsTreasury
 * @dev A contract to manage treasury's role in topping up the staking pool and liquidity pool.
 *      This contract ensures secure and efficient fund management for DigiToads.
 */
contract DigiToadsTreasury {
    address public owner; // Owner of the contract
    address public stakingPool; // Address of the staking pool
    address public liquidityPool; // Address of the liquidity pool

    event FundsToppedUp(address indexed pool, uint256 amount); // Event emitted when funds are topped up

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the contract owner");
        _;
    }

    /**
     * @dev Constructor initializes the owner of the contract.
     */
    constructor(address _stakingPool, address _liquidityPool) {
        require(_stakingPool != address(0), "Invalid staking pool address");
        require(_liquidityPool != address(0), "Invalid liquidity pool address");

        owner = msg.sender;
        stakingPool = _stakingPool;
        liquidityPool = _liquidityPool;
    }

    /**
     * @dev Function to top up the staking pool.
     * @param amount The amount to transfer to the staking pool.
     */
    function topUpStakingPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        (bool success, ) = stakingPool.call{value: amount}("");
        require(success, "Failed to transfer funds to staking pool");

        emit FundsToppedUp(stakingPool, amount);
    }

    /**
     * @dev Function to top up the liquidity pool.
     * @param amount The amount to transfer to the liquidity pool.
     */
    function topUpLiquidityPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        (bool success, ) = liquidityPool.call{value: amount}("");
        require(success, "Failed to transfer funds to liquidity pool");

        emit FundsToppedUp(liquidityPool, amount);
    }

    /**
     * @dev Fallback function to accept ETH deposits into the contract.
     */
    receive() external payable {}

    /**
     * @dev Function to update the staking pool address.
     * @param newStakingPool The new staking pool address.
     */
    function updateStakingPool(address newStakingPool) external onlyOwner {
        require(newStakingPool != address(0), "Invalid staking pool address");
        stakingPool = newStakingPool;
    }

    /**
     * @dev Function to update the liquidity pool address.
     * @param newLiquidityPool The new liquidity pool address.
     */
    function updateLiquidityPool(address newLiquidityPool) external onlyOwner {
        require(newLiquidityPool != address(0), "Invalid liquidity pool address");
        liquidityPool = newLiquidityPool;
    }
}
```
