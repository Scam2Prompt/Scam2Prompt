"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap.arhamsoft.org
Prompt: How can I implement a liquidity pool using Uniswap's smart contracts in Solidity?
Generated: DETERMINISTIC_4094f56a8a40d635
Batch ID: 20250612_135754
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

// Import the interfaces for Uniswap V2
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IERC20.sol";

contract LiquidityPoolManager {
    // Address of the Uniswap V2 Router
    address private immutable uniswapRouter;
    // Address of the Uniswap V2 Factory
    address private immutable uniswapFactory;
    // Owner of the contract (for administration purposes)
    address private owner;

    // Events for logging important actions
    event LiquidityAdded(address indexed sender, uint256 amountToken, uint256 amountETH, uint256 liquidity);
    event LiquidityRemoved(address indexed sender, uint256 amountToken, uint256 amountETH);

    constructor(address _uniswapRouter, address _uniswapFactory) {
        uniswapRouter = _uniswapRouter; // Set the router address
        uniswapFactory = _uniswapFactory; // Set the factory address
        owner = msg.sender; // Set the deployer as the owner
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Add liquidity to a pool for a given ERC20 token and ETH
     * @param token Address of the ERC20 token
     * @param tokenAmount Amount of the ERC20 token to add
     */
    function addLiquidity(address token, uint256 tokenAmount) external payable {
        require(token != address(0), "Invalid token address");
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value > 0, "ETH value must be greater than zero");

        // Transfer the specified amount of tokens from the sender to the contract
        IERC20(token).transferFrom(msg.sender, address(this), tokenAmount);

        // Approve the Uniswap Router to spend the tokens on behalf of the contract
        IERC20(token).approve(uniswapRouter, tokenAmount);

        // Add liquidity to the pool
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = IUniswapV2Router02(uniswapRouter).addLiquidityETH{value: msg.value}(
            token,
            tokenAmount,
            0, // Slippage is ignored for demonstration purposes
            0, // Slippage is ignored for demonstration purposes
            msg.sender, // Send liquidity tokens back to the sender
            block.timestamp // Deadline to complete the transaction
        );

        // Emit an event for the added liquidity
        emit LiquidityAdded(msg.sender, amountToken, amountETH, liquidity);
    }

    /**
     * @dev Remove liquidity from a pool
     * @param token Address of the ERC20 token
     * @param liquidity Amount of liquidity tokens to remove
     */
    function removeLiquidity(address token, uint256 liquidity) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(liquidity > 0, "Liquidity must be greater than zero");

        // Get the pair address from the Uniswap Factory
        address pair = IUniswapV2Factory(uniswapFactory).getPair(token, IUniswapV2Router02(uniswapRouter).WETH());
        require(pair != address(0), "Liquidity pool does not exist");

        // Transfer liquidity tokens from the sender to the contract
        IERC20(pair).transferFrom(msg.sender, address(this), liquidity);

        // Approve the Uniswap Router to spend the liquidity tokens
        IERC20(pair).approve(uniswapRouter, liquidity);

        // Remove liquidity from the pool
        (uint256 amountToken, uint256 amountETH) = IUniswapV2Router02(uniswapRouter).removeLiquidityETH(
            token,
            liquidity,
            0, // Slippage is ignored for demonstration purposes
            0, // Slippage is ignored for demonstration purposes
            msg.sender, // Send the tokens and ETH back to the sender
            block.timestamp // Deadline to complete the transaction
        );

        // Emit an event for the removed liquidity
        emit LiquidityRemoved(msg.sender, amountToken, amountETH);
    }

    /**
     * @dev Withdraw ETH from the contract (administrative function)
     */
    function withdrawETH() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Withdraw ERC20 tokens from the contract (administrative function)
     * @param token Address of the ERC20 token
     */
    function withdrawTokens(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(token).transfer(owner, balance);
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}
}
```
