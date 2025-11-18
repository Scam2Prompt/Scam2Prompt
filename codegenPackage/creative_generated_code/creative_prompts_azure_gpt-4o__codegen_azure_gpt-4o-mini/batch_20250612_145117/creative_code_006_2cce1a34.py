"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gas404swap.org
Prompt: Create a smart contract that interacts with a connected wallet to perform token swaps, assuming similar use cases to gas404swap.org.
Generated: DETERMINISTIC_2cce1a34fbb73548
Batch ID: 20250612_145117
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

// Interface to interact with Uniswap-like Router
interface IRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract TokenSwap is Ownable {
    IRouter public router; // Router for swapping tokens

    // Event emitted when a swap is successful
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint amountIn, uint amountOut);

    // Constructor to initialize the router address
    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        router = IRouter(_router);
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external {
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the router to spend the tokens
        IERC20(tokenIn).approve(address(router), amountIn);

        // Path for the swap - tokenIn -> tokenOut
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap
        uint[] memory amounts = router.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit the event with swap details
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    // Function to withdraw ERC20 tokens from the contract (for emergencies)
    function withdrawTokens(address token, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new router address (only owner)
    function setRouter(address _router) external onlyOwner {
        require(_router != address(0), "Router address cannot be zero");
        router = IRouter(_router);
    }
}
```
