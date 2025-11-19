"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aarrto.pages.dev
Prompt: Create an example of a smart contract that interacts with permissionless pools on Aerodrome Finance for token swaps.
Generated: DETERMINISTIC_c3f6d92e1f0509c6
Batch ID: 20250612_163243
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

// Importing standard interfaces for ERC20 and Uniswap-style router interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}

contract AerodromeSwap {
    // Address of the Uniswap-style router on Aerodrome Finance
    address public immutable router;
    
    // Owner of the contract
    address public owner;

    // Event emitted after a successful swap
    event TokensSwapped(
        address indexed user,
        uint256 amountIn,
        uint256 amountOut,
        address indexed tokenIn,
        address indexed tokenOut
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        router = _router;
        owner = msg.sender;
    }

    /**
     * @notice Swaps tokens via Aerodrome's permissionless pools.
     * @param tokenIn Address of the token you want to swap.
     * @param tokenOut Address of the token you want to receive.
     * @param amountIn Amount of `tokenIn` to swap.
     * @param amountOutMin Minimum amount of `tokenOut` to receive.
     * @param deadline Unix timestamp after which the transaction will not execute.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "AmountIn must be greater than zero");

        // Transfer the input tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the router to spend the tokens
        IERC20(tokenIn).approve(router, amountIn);

        // Define the swap path (tokenIn -> tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Perform the swap
        uint256[] memory amounts = IUniswapV2Router(router).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender, // Send swapped tokens directly to the user
            deadline
        );

        // Emit an event after successful swap
        emit TokensSwapped(msg.sender, amounts[0], amounts[1], tokenIn, tokenOut);
    }

    /**
     * @notice Emergency withdrawal function in case tokens get stuck in the contract.
     * @param token Address of the token to withdraw.
     * @param to Address to send the withdrawn tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(
        address token,
        address to,
        uint256 amount
    ) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(to, amount);
    }
}
```
