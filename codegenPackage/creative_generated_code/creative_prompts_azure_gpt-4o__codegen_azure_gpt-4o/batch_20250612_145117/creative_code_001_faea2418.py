"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponyswap.finance
Prompt: Provide an example of how to use a smart contract to enable token swapping functionality in a DeFi app similar to PonySwap.
Generated: DETERMINISTIC_faea24187a5ec660
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

/**
 * @title TokenSwap
 * @dev A simple smart contract for token swapping in a decentralized application.
 * This example assumes two ERC20 tokens: TokenA and TokenB.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract TokenSwap {
    // Addresses of the two tokens to swap
    IERC20 public tokenA;
    IERC20 public tokenB;

    // Exchange rate expressed as tokenA per tokenB (e.g., 1 tokenB = 2 tokenA)
    uint256 public exchangeRate; // Example: 1 tokenB = exchangeRate of tokenA

    // Owner of the contract
    address public owner;

    event TokensSwapped(address indexed user, address indexed tokenSent, uint256 amountSent, address indexed tokenReceived, uint256 amountReceived);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to set the token addresses and exchange rate.
     * @param _tokenA Address of the first token (TokenA).
     * @param _tokenB Address of the second token (TokenB).
     * @param _exchangeRate Exchange rate for swapping tokens.
     */
    constructor(IERC20 _tokenA, IERC20 _tokenB, uint256 _exchangeRate) {
        tokenA = _tokenA;
        tokenB = _tokenB;
        exchangeRate = _exchangeRate;
        owner = msg.sender;
    }

    /**
     * @dev Updates the exchange rate for the token swap.
     * @param newRate New exchange rate in terms of tokenA per tokenB.
     */
    function updateExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be greater than zero");
        exchangeRate = newRate;
    }

    /**
     * @dev Swap TokenA for TokenB or vice versa based on exchange rate.
     * @param tokenSent Address of the token being sent by the user.
     * @param amountSent Amount of the token being sent by the user.
     */
    function swapTokens(IERC20 tokenSent, uint256 amountSent) external {
        // Validate input token
        require(tokenSent == tokenA || tokenSent == tokenB, "Invalid token address");

        // Determine the token to be received and its amount
        IERC20 tokenReceived = (tokenSent == tokenA) ? tokenB : tokenA;
        uint256 amountReceived = (tokenSent == tokenA) ? (amountSent / exchangeRate) : (amountSent * exchangeRate);

        // Check if the user has enough allowance
        require(tokenSent.allowance(msg.sender, address(this)) >= amountSent, "Insufficient allowance");

        // Check if the contract has enough balance of the token to be sent back to the user
        require(tokenReceived.balanceOf(address(this)) >= amountReceived, "Insufficient contract balance for the token swap");

        // Transfer the tokens sent by the user to the contract
        require(tokenSent.transferFrom(msg.sender, address(this), amountSent), "Token transfer failed");

        // Transfer the swapped tokens from the contract to the user
        require(tokenReceived.transfer(msg.sender, amountReceived), "Token receipt failed");

        // Emit an event for the swap
        emit TokensSwapped(msg.sender, address(tokenSent), amountSent, address(tokenReceived), amountReceived);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(token.transfer(owner, amount), "Token transfer failed");
    }
}
```

This Solidity contract provides a secure and functional implementation for token swapping in a decentralized finance (DeFi) application. The contract allows the owner to update the exchange rate and withdraw tokens, and users to swap between two tokens using the pre-defined exchange rate.
