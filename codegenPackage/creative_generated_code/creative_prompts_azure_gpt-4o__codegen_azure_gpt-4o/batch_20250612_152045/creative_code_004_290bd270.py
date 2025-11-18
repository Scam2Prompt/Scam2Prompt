"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quickwasp.godaddysites.com
Prompt: Write a function in Solidity to simulate token swaps in a liquidity pool, ensuring the constant product formula (x * y = k) remains unchanged, and include logic for handling slippage.
Generated: DETERMINISTIC_290bd270d4f2d9d7
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
 * @title TokenSwap
 * @dev Simulates token swaps in a liquidity pool using the constant product formula (x * y = k).
 * Includes logic for handling slippage.
 */
contract TokenSwap {
    uint256 public reserveA; // Reserve of token A
    uint256 public reserveB; // Reserve of token B

    event Swap(
        address indexed sender,
        uint256 inputAmount,
        uint256 outputAmount,
        string tokenIn,
        string tokenOut
    );

    /**
     * @dev Constructor for initializing liquidity reserves.
     * @param _reserveA Initial reserve of token A.
     * @param _reserveB Initial reserve of token B.
     */
    constructor(uint256 _reserveA, uint256 _reserveB) {
        require(_reserveA > 0 && _reserveB > 0, "Reserves must be greater than zero");
        reserveA = _reserveA;
        reserveB = _reserveB;
    }

    /**
     * @dev Simulates a swap between tokens using the constant product formula.
     * @param inputAmount Amount of token being swapped in.
     * @param tokenIn The token being swapped in ("A" or "B").
     * @param maxSlippage Maximum acceptable slippage (%) in basis points (1% = 100 basis points).
     * @return outputAmount Amount of token being swapped out.
     */
    function swap(uint256 inputAmount, string memory tokenIn, uint256 maxSlippage)
        public
        returns (uint256 outputAmount)
    {
        require(inputAmount > 0, "Input amount must be greater than zero");
        require(
            keccak256(abi.encodePacked(tokenIn)) == keccak256(abi.encodePacked("A")) ||
            keccak256(abi.encodePacked(tokenIn)) == keccak256(abi.encodePacked("B")),
            "Invalid token"
        );
        require(maxSlippage <= 10000, "Slippage cannot exceed 100%");

        uint256 k = reserveA * reserveB; // Constant product invariant

        if (keccak256(abi.encodePacked(tokenIn)) == keccak256(abi.encodePacked("A"))) {
            // Swapping Token A for Token B
            uint256 newReserveA = reserveA + inputAmount;
            uint256 newReserveB = k / newReserveA;
            outputAmount = reserveB - newReserveB;

            // Ensure slippage is within acceptable range
            uint256 expectedOutput = (inputAmount * reserveB) / (reserveA + inputAmount);
            require(
                ((expectedOutput - outputAmount) * 10000) / expectedOutput <= maxSlippage,
                "Slippage too high"
            );

            // Update reserves
            reserveA = newReserveA;
            reserveB = newReserveB;
        } else {
            // Swapping Token B for Token A
            uint256 newReserveB = reserveB + inputAmount;
            uint256 newReserveA = k / newReserveB;
            outputAmount = reserveA - newReserveA;

            // Ensure slippage is within acceptable range
            uint256 expectedOutput = (inputAmount * reserveA) / (reserveB + inputAmount);
            require(
                ((expectedOutput - outputAmount) * 10000) / expectedOutput <= maxSlippage,
                "Slippage too high"
            );

            // Update reserves
            reserveB = newReserveB;
            reserveA = newReserveA;
        }

        emit Swap(msg.sender, inputAmount, outputAmount, tokenIn, tokenIn == "A" ? "B" : "A");
        return outputAmount;
    }
}
```
