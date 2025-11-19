"""
Generated Code Metadata:
========================
Original URL: https://cryptodex.pages.dev
Prompt: Develop a smart contract to handle slippage errors during token swaps on decentralized platforms.
Generated: DETERMINISTIC_a02debefa472e540
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the decentralized exchange (DEX) router
interface IDexRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}

// Smart contract for handling token swaps with slippage control
contract TokenSwap {
    IDexRouter public dexRouter; // DEX router address
    address public owner; // Owner of the contract

    // Event emitted when a swap is successful
    event SwapSuccessful(address indexed user, uint256 amountIn, uint256 amountOut);
    // Event emitted when a swap fails
    event SwapFailed(address indexed user, uint256 amountIn, string reason);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the DEX router address and the owner
    constructor(address _dexRouter) {
        dexRouter = IDexRouter(_dexRouter);
        owner = msg.sender;
    }

    // Function to swap tokens with slippage control
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        // Transfer tokens from the user to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the DEX router to spend the tokens
        IERC20(tokenIn).approve(address(dexRouter), amountIn);

        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Attempt the token swap
        try dexRouter.swapExactTokensForTokens(amountIn, amountOutMin, path, msg.sender, deadline) {
            emit SwapSuccessful(msg.sender, amountIn, amountOutMin);
        } catch (bytes memory reason) {
            // If the swap fails, emit an event with the reason
            emit SwapFailed(msg.sender, amountIn, string(reason));
        }
    }

    // Function to withdraw tokens from the contract (for owner only)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }

    // Function to update the DEX router address (for owner only)
    function updateDexRouter(address newDexRouter) external onlyOwner {
        dexRouter = IDexRouter(newDexRouter);
    }
}
```
