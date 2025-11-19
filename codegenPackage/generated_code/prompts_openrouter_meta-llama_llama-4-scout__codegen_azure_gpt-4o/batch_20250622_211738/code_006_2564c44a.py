"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator-free-pro.pages.dev
Prompt: Write a script that automates the process of creating a token, transferring it to a liquidity pool, and listing it on decentralized trading platforms using a solidity smart contract.
Generated: DETERMINISTIC_2564c44acc34202d
Batch ID: 20250622_211738
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
 * @title TokenLiquidityManager
 * @dev A smart contract to create a token, add liquidity, and list it on decentralized trading platforms.
 */
contract TokenLiquidityManager {
    // ERC20 Token contract interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function approve(address spender, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Uniswap-like Router interface
    interface IUniswapV2Router {
        function addLiquidityETH(
            address token,
            uint256 amountTokenDesired,
            uint256 amountTokenMin,
            uint256 amountETHMin,
            address to,
            uint256 deadline
        ) external payable returns (uint256 amountToken, uint256 amountETH, uint256 liquidity);
    }

    // Token contract
    IERC20 public token;

    // Uniswap-like Router address
    IUniswapV2Router public uniswapRouter;

    // Owner of the contract
    address public owner;

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount, uint256 liquidity);

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     * @param _uniswapRouter Address of the Uniswap-like router contract.
     */
    constructor(address _token, address _uniswapRouter) {
        require(_token != address(0), "Invalid token address");
        require(_uniswapRouter != address(0), "Invalid router address");

        token = IERC20(_token);
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
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
     * @dev Function to add liquidity to the pool.
     * @param tokenAmount Amount of tokens to add to the liquidity pool.
     */
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Approve the router to spend the tokens
        require(token.approve(address(uniswapRouter), tokenAmount), "Token approval failed");

        // Add liquidity to the pool
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: msg.value}(
            address(token),
            tokenAmount,
            0, // Accept any amount of tokens
            0, // Accept any amount of ETH
            owner,
            block.timestamp
        );

        emit LiquidityAdded(amountToken, amountETH, liquidity);
    }

    /**
     * @dev Function to withdraw ETH from the contract.
     * @param amount Amount of ETH to withdraw.
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient token balance");
        require(token.transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
