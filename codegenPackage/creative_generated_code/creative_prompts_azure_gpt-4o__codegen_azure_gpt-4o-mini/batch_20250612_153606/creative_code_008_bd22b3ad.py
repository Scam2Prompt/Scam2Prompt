"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xuirin-com.pages.dev
Prompt: Generate code to implement a swap aggregator for ERC20 tokens, ensuring compatibility with the xuirin Finance ecosystem.
Generated: DETERMINISTIC_bd22b3ad8d90253e
Batch ID: 20250612_153606
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

// Interface for the ERC20 token standard
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

// SwapAggregator contract for aggregating swaps in the xuirin Finance ecosystem
contract SwapAggregator {
    address public owner;

    // Mapping to store approved tokens for swapping
    mapping(address => bool) public approvedTokens;

    // Event emitted when a swap occurs
    event Swap(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to approve a token for swapping
    function approveToken(address token) external onlyOwner {
        approvedTokens[token] = true;
    }

    // Function to revoke approval of a token
    function revokeToken(address token) external onlyOwner {
        approvedTokens[token] = false;
    }

    // Function to perform a swap between two ERC20 tokens
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to
    ) external {
        require(approvedTokens[tokenIn], "Token In not approved");
        require(approvedTokens[tokenOut], "Token Out not approved");
        
        // Transfer tokenIn from the user to this contract
        require(IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn), "Transfer of tokenIn failed");

        // Logic for swapping tokens (this is a placeholder; integrate with actual swap logic)
        uint256 amountOut = getSwapAmount(tokenIn, tokenOut, amountIn);
        require(amountOut >= amountOutMin, "Insufficient output amount");

        // Transfer tokenOut from this contract to the user
        require(IERC20(tokenOut).transfer(to, amountOut), "Transfer of tokenOut failed");

        // Emit swap event
        emit Swap(tokenIn, tokenOut, amountIn, amountOut);
    }

    // Placeholder function for calculating swap amount
    // This should be replaced with actual swap logic and price feeds
    function getSwapAmount(address tokenIn, address tokenOut, uint256 amountIn) internal view returns (uint256) {
        // Implement logic to calculate swap amount based on market data or DEX pricing
        return amountIn; // For demonstration purposes, swap 1:1
    }

    // Function to withdraw tokens from the contract (to be used by the owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
