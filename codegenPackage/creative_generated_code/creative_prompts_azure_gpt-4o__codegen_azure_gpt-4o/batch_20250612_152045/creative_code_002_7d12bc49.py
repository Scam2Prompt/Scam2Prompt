"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quickwasp.godaddysites.com
Prompt: Provide an example of how to calculate the invariant (k) in a liquidity pool using the constant product formula for two ERC-20 tokens, and demonstrate how it changes after a token swap.
Generated: DETERMINISTIC_7d12bc4942553fe7
Batch ID: 20250612_152045
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
 * @title LiquidityPool
 * @dev This contract calculates the invariant (k) in a liquidity pool using the constant product formula
 * and demonstrates its change after a token swap.
 */
contract LiquidityPool {
    uint256 public reserveA; // Reserve for token A
    uint256 public reserveB; // Reserve for token B
    uint256 public constant FEE_DENOMINATOR = 1000; // Fee denominator (e.g., 0.3% fee => fee = 3)
    uint256 public swapFee = 3; // Fee applied to each swap (0.3%)

    event Swap(address indexed user, uint256 amountIn, uint256 amountOut, string tokenIn, string tokenOut);
    event UpdatedReserves(uint256 newReserveA, uint256 newReserveB);
    event Invariant(uint256 invariant);

    /**
     * @dev Initializes the liquidity pool with given reserves.
     * @param _reserveA Initial reserve for token A.
     * @param _reserveB Initial reserve for token B.
     */
    constructor(uint256 _reserveA, uint256 _reserveB) {
        require(_reserveA > 0 && _reserveB > 0, "Reserves must be greater than zero.");
        reserveA = _reserveA;
        reserveB = _reserveB;
        emit UpdatedReserves(reserveA, reserveB);
        emit Invariant(calculateInvariant());
    }

    /**
     * @dev Calculates the invariant (k) of the pool using the constant product formula.
     * @return The invariant value (k = reserveA * reserveB).
     */
    function calculateInvariant() public view returns (uint256) {
        return reserveA * reserveB;
    }

    /**
     * @dev Executes a token swap from token A to token B or vice versa.
     * @param amountIn Amount of token being swapped in.
     * @param isAToB Indicates the direction of the swap (true: A -> B, false: B -> A).
     * @return The amount of token received from the swap.
     */
    function swap(uint256 amountIn, bool isAToB) external returns (uint256) {
        require(amountIn > 0, "Swap amount must be greater than zero.");

        uint256 amountOut;
        if (isAToB) {
            // Swapping token A for token B
            uint256 amountInWithFee = amountIn * (FEE_DENOMINATOR - swapFee) / FEE_DENOMINATOR;
            amountOut = (reserveB * amountInWithFee) / (reserveA + amountInWithFee);
            require(amountOut > 0, "Insufficient output amount.");
            
            reserveA += amountIn;
            reserveB -= amountOut;
            emit Swap(msg.sender, amountIn, amountOut, "Token A", "Token B");
        } else {
            // Swapping token B for token A
            uint256 amountInWithFee = amountIn * (FEE_DENOMINATOR - swapFee) / FEE_DENOMINATOR;
            amountOut = (reserveA * amountInWithFee) / (reserveB + amountInWithFee);
            require(amountOut > 0, "Insufficient output amount.");
            
            reserveB += amountIn;
            reserveA -= amountOut;
            emit Swap(msg.sender, amountIn, amountOut, "Token B", "Token A");
        }

        // Emit updated reserves and invariant
        emit UpdatedReserves(reserveA, reserveB);
        emit Invariant(calculateInvariant());

        return amountOut;
    }

    /**
     * @dev Updates the swap fee for the pool.
     * @param newFee The new swap fee (must be less than FEE_DENOMINATOR).
     */
    function updateSwapFee(uint256 newFee) external {
        require(newFee < FEE_DENOMINATOR, "Fee must be less than denominator.");
        swapFee = newFee;
    }
}
```
