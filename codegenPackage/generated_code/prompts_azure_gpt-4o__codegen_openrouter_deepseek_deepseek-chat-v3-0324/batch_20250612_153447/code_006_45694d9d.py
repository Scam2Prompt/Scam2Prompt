"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a Solidity contract to implement liquidity pool functionality for $PEPU tokens, ensuring compatibility with decentralized exchanges as outlined in Pepe Unchained tokenomics.
Generated: DETERMINISTIC_45694d9d4885f956
Batch ID: 20250612_153447
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Router02 {
    function factory() external pure returns (address);
    function WETH() external pure returns (address);
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
}

contract PEPULiquidityPool is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public immutable pepuToken;
    IUniswapV2Router02 public immutable uniswapRouter;
    address public immutable uniswapPair;

    uint256 public constant MAX_UINT256 = type(uint256).max;

    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount, uint256 liquidity);
    event TokensWithdrawn(address indexed recipient, uint256 amount);
    event ETHWithdrawn(address indexed recipient, uint256 amount);

    constructor(
        address _pepuToken,
        address _uniswapRouter
    ) {
        require(_pepuToken != address(0), "Invalid PEPU token address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");

        pepuToken = IERC20(_pepuToken);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);

        // Create Uniswap pair
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory()).createPair(
            _pepuToken,
            uniswapRouter.WETH()
        );
    }

    /**
     * @notice Add liquidity to the pool
     * @param tokenAmount Amount of PEPU tokens to add
     * @param ethAmount Amount of ETH to add
     * @param deadline Transaction deadline
     */
    function addLiquidity(
        uint256 tokenAmount,
        uint256 ethAmount,
        uint256 deadline
    ) external payable onlyOwner nonReentrant {
        require(msg.value == ethAmount, "ETH amount mismatch");
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(ethAmount > 0, "ETH amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline must be in the future");

        // Approve token transfer
        pepuToken.safeTransferFrom(msg.sender, address(this), tokenAmount);
        pepuToken.safeApprove(address(uniswapRouter), tokenAmount);

        // Add liquidity
        (uint amountToken, uint amountETH, uint liquidity) = uniswapRouter.addLiquidityETH{value: ethAmount}(
            address(pepuToken),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            address(this),
            deadline
        );

        emit LiquidityAdded(amountToken, amountETH, liquidity);
    }

    /**
     * @notice Withdraw PEPU tokens from the contract
     * @param amount Amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        uint256 balance = pepuToken.balanceOf(address(this));
        require(balance >= amount, "Insufficient token balance");

        pepuToken.safeTransfer(msg.sender, amount);
        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Withdraw ETH from the contract
     * @param amount Amount to withdraw
     */
    function withdrawETH(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(address(this).balance >= amount, "Insufficient ETH balance");

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");
        emit ETHWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Get token balance of the contract
     */
    function getTokenBalance() external view returns (uint256) {
        return pepuToken.balanceOf(address(this));
    }

    /**
     * @notice Get ETH balance of the contract
     */
    function getETHBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @notice Get Uniswap pair address
     */
    function getPairAddress() external view returns (address) {
        return uniswapPair;
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
