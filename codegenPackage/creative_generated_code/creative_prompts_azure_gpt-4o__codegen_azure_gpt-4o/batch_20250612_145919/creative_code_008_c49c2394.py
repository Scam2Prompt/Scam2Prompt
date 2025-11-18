"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapx.ch
Prompt: Provide an example of using UniswapX to execute multi-hop swaps, and explain the advantages of this feature.
Generated: DETERMINISTIC_c49c239480a0ed05
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary Uniswap interfaces and libraries
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MultiHopSwap {
    IUniswapV2Router02 public immutable uniswapRouter;

    // Address of the Uniswap Router
    constructor(address _uniswapRouter) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    /**
     * @notice Executes a multi-hop swap on UniswapV2
     * @param amountIn Amount of the input token to swap
     * @param amountOutMin Minimum amount of the output token expected (slippage protection)
     * @param path Array of token addresses, representing the swap path
     * @param to Address to send the output tokens
     * @param deadline Unix timestamp by which the transaction must be completed
     */
    function multiHopSwap(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external {
        require(path.length >= 2, "Path must contain at least two tokens");
        require(IERC20(path[0]).balanceOf(msg.sender) >= amountIn, "Insufficient input token balance");
        
        // Transfer input tokens from the sender to this contract
        IERC20(path[0]).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve the Uniswap Router to spend the input tokens
        IERC20(path[0]).approve(address(uniswapRouter), amountIn);
        
        // Execute the swap
        try uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        ) returns (uint[] memory amounts) {
            // Swap successful, amounts array contains the input and output amounts per hop
        } catch {
            revert("Swap failed");
        }
    }
}
```
