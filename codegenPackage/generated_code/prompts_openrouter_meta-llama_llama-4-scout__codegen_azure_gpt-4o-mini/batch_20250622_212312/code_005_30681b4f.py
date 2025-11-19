"""
Generated Code Metadata:
========================
Original URL: https://linea-ten.vercel.app
Prompt: Create a Linea-based DeFi dapp that swaps tokens, farms yield, and accesses liquidity with EVM equivalence.
Generated: DETERMINISTIC_30681b4fdea03206
Batch ID: 20250622_212312
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Uniswap-like router for token swaps
interface IRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
}

// Main contract for the DeFi DApp
contract DeFiDapp is Ownable {
    using SafeMath for uint256;

    // State variables
    IRouter public router; // Router for swapping and adding liquidity
    address public tokenA;  // Address of Token A
    address public tokenB;  // Address of Token B

    // Events for logging
    event TokensSwapped(address indexed user, uint amountIn, uint amountOut);
    event LiquidityAdded(address indexed user, uint amountA, uint amountB);

    // Constructor to initialize the contract
    constructor(address _router, address _tokenA, address _tokenB) {
        router = IRouter(_router);
        tokenA = _tokenA;
        tokenB = _tokenB;
    }

    // Function to swap tokens
    function swapTokens(uint amountIn, uint amountOutMin, address[] calldata path, uint deadline) external {
        require(amountIn > 0, "Amount in must be greater than 0");
        require(path[0] == tokenA || path[0] == tokenB, "Invalid token path");

        // Transfer tokens from user to contract
        IERC20(path[0]).transferFrom(msg.sender, address(this), amountIn);

        // Approve the router to spend the tokens
        IERC20(path[0]).approve(address(router), amountIn);

        // Perform the swap
        uint[] memory amounts = router.swapExactTokensForTokens(amountIn, amountOutMin, path, msg.sender, deadline);

        // Emit event for logging
        emit TokensSwapped(msg.sender, amounts[0], amounts[amounts.length - 1]);
    }

    // Function to add liquidity
    function addLiquidity(uint amountADesired, uint amountBDesired, uint amountAMin, uint amountBMin, uint deadline) external {
        require(amountADesired > 0 && amountBDesired > 0, "Amounts must be greater than 0");

        // Transfer tokens from user to contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve the router to spend the tokens
        IERC20(tokenA).approve(address(router), amountADesired);
        IERC20(tokenB).approve(address(router), amountBDesired);

        // Add liquidity
        (uint amountA, uint amountB, ) = router.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        // Emit event for logging
        emit LiquidityAdded(msg.sender, amountA, amountB);
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(address token, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
