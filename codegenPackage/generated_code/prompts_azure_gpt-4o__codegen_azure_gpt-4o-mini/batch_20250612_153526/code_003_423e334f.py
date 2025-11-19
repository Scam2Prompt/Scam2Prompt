"""
Generated Code Metadata:
========================
Original URL: https://dodgecoiin20.pages.dev
Prompt: Generate Solidity code for a liquidity provision mechanism that allocates 10% of the DOGE20 token supply to Uniswap, ensuring early liquidity for trading.
Generated: DETERMINISTIC_423e334ff0e611c9
Batch ID: 20250612_153526
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

// Importing the necessary interfaces for ERC20 and Uniswap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

contract DOGE20 is ERC20Burnable, Ownable {
    // Uniswap router and factory addresses (mainnet)
    IUniswapV2Router02 public uniswapRouter;
    address public uniswapPair;

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("DOGE20", "DOGE20") {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply);
        
        // Set the Uniswap router address
        uniswapRouter = IUniswapV2Router02(0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D); // Uniswap V2 Router

        // Create a Uniswap pair for this token
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory()).createPair(address(this), uniswapRouter.WETH());
        
        // Allocate 10% of the total supply to liquidity
        uint256 liquidityAmount = initialSupply * 10 / 100;
        _approve(address(this), address(uniswapRouter), liquidityAmount);
        
        // Add liquidity to Uniswap
        addLiquidity(liquidityAmount);
    }

    // Function to add liquidity to Uniswap
    function addLiquidity(uint256 tokenAmount) private {
        // Calculate the amount of ETH to add as liquidity (1:1 ratio for simplicity)
        uint256 ethAmount = address(this).balance;

        // Add the liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: ethAmount}(
            address(this),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            owner(),
            block.timestamp
        );

        // Emit an event for liquidity added
        emit LiquidityAdded(amountToken, amountETH);
    }

    // Function to receive ETH when sending ETH to the contract
    receive() external payable {}
}
```
