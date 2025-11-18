"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dodgecoiin20.pages.dev
Prompt: Generate Solidity code for a liquidity provision mechanism that allocates 10% of the DOGE20 token supply to Uniswap, ensuring early liquidity for trading.
Generated: DETERMINISTIC_423e334ff0e611c9
Batch ID: 20250612_153526
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

// Import interfaces for Uniswap functionality
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Doge20Token is ERC20, Ownable {
    // Uniswap Router address (ensure this is correct for the desired network)
    address public constant UNISWAP_ROUTER_ADDRESS = 0xYourRouterAddressHere;

    IUniswapV2Router02 public uniswapRouter;
    address public uniswapPair;

    // Constructor to initialize the token with name, symbol, and initial supply
    constructor(uint256 initialSupply) ERC20("DOGE20", "DOGE20") {
        // Mint the total supply to the contract owner (msg.sender)
        _mint(msg.sender, initialSupply);

        // Initialize Uniswap Router
        uniswapRouter = IUniswapV2Router02(UNISWAP_ROUTER_ADDRESS);

        // Create Uniswap pair for DOGE20 and WETH
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory()).createPair(
            address(this), 
            uniswapRouter.WETH()
        );

        // Allocate 10% of the total supply to provide liquidity
        _allocateLiquidity(initialSupply);
    }

    /**
     * @dev Allocate 10% of the DOGE20 token supply to Uniswap liquidity pool
     * @param totalSupply The total supply of the token
     */
    function _allocateLiquidity(uint256 totalSupply) internal {
        // Calculate 10% of the total supply
        uint256 liquidityTokens = (totalSupply * 10) / 100;

        // Approve Uniswap Router to spend tokens
        _approve(address(this), address(uniswapRouter), liquidityTokens);

        // Add liquidity to Uniswap pool
        // The contract needs to hold enough ETH to pair with the tokens for liquidity provision
        try uniswapRouter.addLiquidityETH{value: address(this).balance}(
            address(this), // Token address
            liquidityTokens, // Amount of tokens to add
            0, // Minimum tokens (slippage)
            0, // Minimum ETH (slippage)
            owner(), // Liquidity receiver
            block.timestamp // Deadline
        ) {
            // Liquidity added successfully
        } catch {
            revert("Liquidity addition failed");
        }
    }

    /**
     * @dev Allow contract to receive ETH for liquidity provision
     */
    receive() external payable {}
}
```
