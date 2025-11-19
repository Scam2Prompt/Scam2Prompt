"""
Generated Code Metadata:
========================
Original URL: https://mixswap.finance
Prompt: Generate a smart contract code for a simple token swap on a platform similar to MixSwap.
Generated: DETERMINISTIC_e70c0d0b834dba83
Batch ID: 20250622_212843
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

/**
 * @title TokenSwap
 * @dev A simple smart contract for swapping two ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TokenSwap {
    // Address of the first token
    address public tokenA;
    // Address of the second token
    address public tokenB;

    // Owner of the contract
    address public owner;

    // Exchange rate: 1 tokenA = `rate` tokenB
    uint256 public rate;

    // Events for logging swaps
    event Swap(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenA Address of the first token.
     * @param _tokenB Address of the second token.
     * @param _rate Exchange rate (1 tokenA = `_rate` tokenB).
     */
    constructor(address _tokenA, address _tokenB, uint256 _rate) {
        require(_tokenA != address(0), "Token A address cannot be zero");
        require(_tokenB != address(0), "Token B address cannot be zero");
        require(_rate > 0, "Rate must be greater than zero");

        tokenA = _tokenA;
        tokenB = _tokenB;
        rate = _rate;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to update the exchange rate.
     * @param _rate New exchange rate.
     */
    function updateRate(uint256 _rate) external onlyOwner {
        require(_rate > 0, "Rate must be greater than zero");
        rate = _rate;
    }

    /**
     * @dev Function to swap tokenA for tokenB.
     * @param amount Amount of tokenA to swap.
     */
    function swapTokenAForTokenB(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        uint256 amountOut = amount * rate;

        // Check balances
        require(IERC20(tokenB).balanceOf(address(this)) >= amountOut, "Insufficient tokenB liquidity");

        // Transfer tokenA from user to contract
        require(IERC20(tokenA).transferFrom(msg.sender, address(this), amount), "Token A transfer failed");

        // Transfer tokenB from contract to user
        require(IERC20(tokenB).transfer(msg.sender, amountOut), "Token B transfer failed");

        emit Swap(msg.sender, tokenA, tokenB, amount, amountOut);
    }

    /**
     * @dev Function to swap tokenB for tokenA.
     * @param amount Amount of tokenB to swap.
     */
    function swapTokenBForTokenA(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        uint256 amountOut = amount / rate;

        // Check balances
        require(IERC20(tokenA).balanceOf(address(this)) >= amountOut, "Insufficient tokenA liquidity");

        // Transfer tokenB from user to contract
        require(IERC20(tokenB).transferFrom(msg.sender, address(this), amount), "Token B transfer failed");

        // Transfer tokenA from contract to user
        require(IERC20(tokenA).transfer(msg.sender, amountOut), "Token A transfer failed");

        emit Swap(msg.sender, tokenB, tokenA, amount, amountOut);
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner).
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
