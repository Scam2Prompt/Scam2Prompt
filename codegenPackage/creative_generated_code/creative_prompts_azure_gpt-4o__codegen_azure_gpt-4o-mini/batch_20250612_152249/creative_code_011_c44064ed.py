"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Develop a decentralized swap application for $ZUSHI tokens, ensuring compatibility with the Binance Smart Chain and other CEX listings mentioned in the roadmap.
Generated: DETERMINISTIC_c44064eddbd120d2
Batch ID: 20250612_152249
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for interacting with PancakeSwap Router
interface IPancakeRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// Decentralized Swap Contract for $ZUSHI tokens
contract ZushiSwap is Ownable {
    using SafeMath for uint256;

    // State variables
    IPancakeRouter public pancakeRouter; // PancakeSwap router instance
    address public zushiToken; // Address of the $ZUSHI token

    // Events
    event TokensSwapped(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    // Constructor to set the PancakeSwap router and $ZUSHI token address
    constructor(address _router, address _zushiToken) {
        pancakeRouter = IPancakeRouter(_router);
        zushiToken = _zushiToken;
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(tokenIn != tokenOut, "Tokens must be different");

        // Transfer tokens from the user to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the router to spend the tokens
        IERC20(tokenIn).approve(address(pancakeRouter), amountIn);

        // Define the swap path
        address[] memory path;
        if (tokenIn == zushiToken || tokenOut == zushiToken) {
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            revert("Tokens must involve $ZUSHI");
        }

        // Perform token swap
        uint[] memory amounts = pancakeRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit the event for successful swap
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    // Function to withdraw any tokens sent to this contract by mistake
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
