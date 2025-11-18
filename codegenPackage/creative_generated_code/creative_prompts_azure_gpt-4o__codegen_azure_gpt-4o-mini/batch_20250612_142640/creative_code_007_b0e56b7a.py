"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Provide a code snippet for a Solidity contract that uses ParaSwap to safely integrate with external DeFi protocols, similar to Instadapp's approach.
Generated: DETERMINISTIC_b0e56b7a81c8c68b
Batch ID: 20250612_142640
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
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for ParaSwap's aggregator
interface IParaSwap {
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address recipient,
        uint256 deadline,
        bytes memory params
    ) external returns (uint256 amountOut);
}

// DeFiIntegration contract allows users to swap tokens through ParaSwap
contract DeFiIntegration is Ownable {
    using Address for address;

    // ParaSwap aggregator address
    IParaSwap public paraSwap;

    // Events for logging actions
    event TokensSwapped(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the ParaSwap address
    constructor(address _paraSwap) {
        require(_paraSwap.isContract(), "ParaSwap address must be a contract");
        paraSwap = IParaSwap(_paraSwap);
    }

    // Function to swap tokens via ParaSwap
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline,
        bytes memory params
    ) external {
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from the sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve ParaSwap to spend the tokens
        IERC20(tokenIn).approve(address(paraSwap), amountIn);

        // Perform the swap on ParaSwap
        uint256 amountOut = paraSwap.swap(tokenIn, tokenOut, amountIn, minAmountOut, msg.sender, deadline, params);

        // Emit event for the swap
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to update the ParaSwap address (only by owner)
    function updateParaSwapAddress(address newParaSwap) external onlyOwner {
        require(newParaSwap.isContract(), "New ParaSwap address must be a contract");
        paraSwap = IParaSwap(newParaSwap);
    }

    // Fallback function to receive ETH (if necessary)
    receive() external payable {}
}
```
