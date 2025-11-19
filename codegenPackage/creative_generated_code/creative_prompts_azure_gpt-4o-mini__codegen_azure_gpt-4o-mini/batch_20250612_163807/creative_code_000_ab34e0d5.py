"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botcodesrc.pages.dev
Prompt: Write a Solidity contract that implements a slippage bot for the 1inch exchange, referencing the provided code structure and libraries from Uniswap.
Generated: DETERMINISTIC_ab34e0d58c70acfc
Batch ID: 20250612_163807
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@1inch/1inch-exchange-v2/contracts/interfaces/IExchange.sol";

// Contract definition for SlippageBot
contract SlippageBot is Ownable {
    // Address of 1inch Router
    IExchange public oneInchRouter;

    // Event emitted when a swap occurs
    event SwapExecuted(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the 1inch exchange router address
    constructor(address _oneInchRouter) {
        require(_oneInchRouter != address(0), "Invalid router address");
        oneInchRouter = IExchange(_oneInchRouter);
    }

    // Function to execute a swap with slippage control
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        bytes calldata data
    ) external onlyOwner {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(minAmountOut > 0, "Minimum amount out must be greater than zero");

        // Transfer tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the 1inch router to spend the tokens
        IERC20(tokenIn).approve(address(oneInchRouter), amountIn);

        // Execute the swap on 1inch exchange
        (bool success, bytes memory returnData) = address(oneInchRouter).call(data);
        require(success, "Swap failed");

        // Decode returned data to get the amount received
        (uint256 amountOut) = abi.decode(returnData, (uint256));

        // Ensure the swap met the minimum amount out requirement
        require(amountOut >= minAmountOut, "Slippage exceeded");

        // Transfer the output tokens to the user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit event for the swap execution
        emit SwapExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to withdraw tokens in case of any issue
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
