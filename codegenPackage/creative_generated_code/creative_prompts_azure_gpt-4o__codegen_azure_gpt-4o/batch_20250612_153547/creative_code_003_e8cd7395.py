"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: Create a smart contract function to supply liquidity to the USDT-CHZ pool and calculate bonus points earned for the KAYEN League.
Generated: DETERMINISTIC_e8cd7395054c2aa2
Batch ID: 20250612_153547
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
 * @title LiquiditySupplyContract
 * @dev A smart contract to supply liquidity to the USDT-CHZ pool and calculate bonus points for KAYEN League.
 */
contract LiquiditySupplyContract {
    // Address of the USDT-CHZ liquidity pool
    address public usdtChzPool;

    // Points multipliers for bonus calculation
    uint256 public constant POINTS_MULTIPLIER = 100;

    // Event emitted when liquidity is supplied
    event LiquiditySupplied(
        address indexed supplier,
        uint256 usdtAmount,
        uint256 chzAmount,
        uint256 bonusPoints
    );

    /**
     * @dev Constructor to initialize the USDT-CHZ pool address
     * @param _pool Address of the USDT-CHZ liquidity pool
     */
    constructor(address _pool) {
        require(_pool != address(0), "Invalid pool address");
        usdtChzPool = _pool;
    }

    /**
     * @dev Supplies liquidity to the USDT-CHZ pool and calculates bonus points earned.
     * @param usdtAmount Amount of USDT to supply
     * @param chzAmount Amount of CHZ to supply
     * @return bonusPoints The calculated bonus points earned
     */
    function supplyLiquidity(uint256 usdtAmount, uint256 chzAmount) external returns (uint256 bonusPoints) {
        // Input validation
        require(usdtAmount > 0, "USDT amount must be greater than zero");
        require(chzAmount > 0, "CHZ amount must be greater than zero");

        // Call to the liquidity pool contract (mock implementation here)
        // In a production system, this would involve interacting with the pool contract directly
        bool success = _mockAddLiquidity(usdtAmount, chzAmount);
        require(success, "Failed to add liquidity to the pool");

        // Calculate bonus points
        bonusPoints = _calculateBonusPoints(usdtAmount, chzAmount);

        // Emit an event for supplied liquidity
        emit LiquiditySupplied(msg.sender, usdtAmount, chzAmount, bonusPoints);

        return bonusPoints;
    }

    /**
     * @dev Mock function to simulate adding liquidity to the pool.
     * Replace this with actual pool contract interaction in production.
     */
    function _mockAddLiquidity(uint256 usdtAmount, uint256 chzAmount) private pure returns (bool) {
        // Simulate successful liquidity addition
        // Replace with actual interaction logic (e.g., pool.deposit(usdtAmount, chzAmount))
        return true;
    }

    /**
     * @dev Calculates bonus points based on supplied USDT and CHZ amounts.
     * @param usdtAmount Amount of USDT supplied
     * @param chzAmount Amount of CHZ supplied
     * @return bonusPoints The calculated bonus points earned
     */
    function _calculateBonusPoints(uint256 usdtAmount, uint256 chzAmount) private pure returns (uint256) {
        // Simple calculation for bonus points based on the supplied amounts
        // Replace this with more complex logic if needed
        return (usdtAmount + chzAmount) * POINTS_MULTIPLIER;
    }
}
```
