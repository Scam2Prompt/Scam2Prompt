"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wololo-main-j9jl6a3hu-edrive.vercel.app
Prompt: Write a guide for setting up a decentralized exchange (DEX) that supports trading of meme coins like $BITCONNECT, incorporating features for token listing and liquidity pool creation.
Generated: DETERMINISTIC_a8794daf0b1c0f8e
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Decentralized Exchange (DEX) for Meme Coins
 * @dev This contract allows users to list meme tokens, create liquidity pools, and trade them.
 * @author Expert Programmer
 */
contract MemeCoinDEX {
    struct LiquidityPool {
        address token;
        uint256 tokenReserve;
        uint256 ethReserve;
    }

    mapping(address => LiquidityPool) public liquidityPools;
    mapping(address => bool) public listedTokens;

    event TokenListed(address indexed token);
    event LiquidityAdded(address indexed token, uint256 tokenAmount, uint256 ethAmount);
    event TokenSwapped(address indexed token, uint256 tokenAmount, uint256 ethAmount);

    // Modifier to ensure the token is listed
    modifier isTokenListed(address token) {
        require(listedTokens[token], "Token not listed");
        _;
    }

    /**
     * @notice List a new meme token on the DEX
     * @dev Only callable by token owner or approved users in production
     * @param token Address of the meme token to list
     */
    function listToken(address token) external {
        require(token != address(0), "Invalid token address");
        require(!listedTokens[token], "Token already listed");

        listedTokens[token] = true;

        emit TokenListed(token);
    }

    /**
     * @notice Add liquidity to a token's liquidity pool
     * @param token Address of the token
     * @param tokenAmount Amount of tokens to add to the pool
     */
    function addLiquidity(address token, uint256 tokenAmount) external payable isTokenListed(token) {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(msg.value > 0, "ETH amount must be greater than 0");

        LiquidityPool storage pool = liquidityPools[token];
        pool.token = token;
        pool.tokenReserve += tokenAmount;
        pool.ethReserve += msg.value;

        IERC20(token).transferFrom(msg.sender, address(this), tokenAmount);

        emit LiquidityAdded(token, tokenAmount, msg.value);
    }

    /**
     * @notice Swap ETH for meme tokens
     * @param token Address of the token to swap for
     */
    function swapEthForTokens(address token) external payable isTokenListed(token) {
        require(msg.value > 0, "ETH amount must be greater than 0");

        LiquidityPool storage pool = liquidityPools[token];
        require(pool.ethReserve > 0 && pool.tokenReserve > 0, "Insufficient liquidity");

        // Calculate token amount based on reserves and input ETH (Simple AMM formula)
        uint256 tokensOut = (msg.value * pool.tokenReserve) / (pool.ethReserve + msg.value);

        require(tokensOut > 0, "Insufficient output amount");

        pool.ethReserve += msg.value;
        pool.tokenReserve -= tokensOut;

        IERC20(token).transfer(msg.sender, tokensOut);

        emit TokenSwapped(token, tokensOut, msg.value);
    }

    /**
     * @notice Swap meme tokens for ETH
     * @param token Address of the token to swap
     * @param tokenAmount Amount of tokens to swap for ETH
     */
    function swapTokensForEth(address token, uint256 tokenAmount) external isTokenListed(token) {
        require(tokenAmount > 0, "Token amount must be greater than 0");

        LiquidityPool storage pool = liquidityPools[token];
        require(pool.ethReserve > 0 && pool.tokenReserve > 0, "Insufficient liquidity");

        // Calculate ETH amount based on reserves and input tokens (Simple AMM formula)
        uint256 ethOut = (tokenAmount * pool.ethReserve) / (pool.tokenReserve + tokenAmount);

        require(ethOut > 0, "Insufficient output amount");

        pool.tokenReserve += tokenAmount;
        pool.ethReserve -= ethOut;

        IERC20(token).transferFrom(msg.sender, address(this), tokenAmount);
        payable(msg.sender).transfer(ethOut);

        emit TokenSwapped(token, tokenAmount, ethOut);
    }

    /**
     * @dev Fallback function to prevent sending ETH directly to the contract
     */
    receive() external payable {
        revert("Direct ETH deposits not allowed");
    }
}

/**
 * @title ERC20 Interface
 * @dev Basic interface for ERC20 tokens to interact with external contracts
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
