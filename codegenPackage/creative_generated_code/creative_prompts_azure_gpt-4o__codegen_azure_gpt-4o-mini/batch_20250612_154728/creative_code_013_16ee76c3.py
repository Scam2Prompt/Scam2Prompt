"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkswapfinance.gitbook.io
Prompt: Write a Solidity contract to integrate zkSwap Finance's Stableswap feature for stablecoin trading with minimal slippage.
Generated: DETERMINISTIC_16ee76c32e2fd8ef
Batch ID: 20250612_154728
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the zkSwap Stableswap functionality
interface IZkSwapStableswap {
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

/**
 * @title StablecoinSwap
 * @dev A contract to facilitate stablecoin trading using zkSwap's Stableswap feature.
 */
contract StablecoinSwap is Ownable {
    IZkSwapStableswap public zkSwapStableswap;

    // Event emitted when a swap is executed
    event SwapExecuted(
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        address indexed to
    );

    /**
     * @dev Sets the zkSwap Stableswap contract address.
     * @param _zkSwapStableswap Address of the zkSwap Stableswap contract.
     */
    constructor(address _zkSwapStableswap) {
        require(_zkSwapStableswap != address(0), "Invalid Stableswap address");
        zkSwapStableswap = IZkSwapStableswap(_zkSwapStableswap);
    }

    /**
     * @dev Swaps stablecoins using zkSwap's Stableswap feature.
     * @param tokenIn The address of the input token (stablecoin).
     * @param tokenOut The address of the output token (stablecoin).
     * @param amountIn The amount of input tokens to swap.
     * @param amountOutMin The minimum amount of output tokens to receive.
     * @param to The address to receive the output tokens.
     * @param deadline The time by which the swap must be completed.
     */
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(to != address(0), "Invalid recipient address");
        require(deadline >= block.timestamp, "Expired deadline");

        // Transfer the input tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the zkSwap Stableswap contract to spend the input tokens
        IERC20(tokenIn).approve(address(zkSwapStableswap), amountIn);

        // Execute the swap
        uint256 amountOut = zkSwapStableswap.swap(
            tokenIn,
            tokenOut,
            amountIn,
            amountOutMin,
            to,
            deadline
        );

        // Emit the swap event
        emit SwapExecuted(tokenIn, tokenOut, amountIn, amountOut, to);
    }

    /**
     * @dev Allows the owner to update the zkSwap Stableswap contract address.
     * @param _zkSwapStableswap New address for the zkSwap Stableswap contract.
     */
    function updateZkSwapStableswap(address _zkSwapStableswap) external onlyOwner {
        require(_zkSwapStableswap != address(0), "Invalid Stableswap address");
        zkSwapStableswap = IZkSwapStableswap(_zkSwapStableswap);
    }
}
```
