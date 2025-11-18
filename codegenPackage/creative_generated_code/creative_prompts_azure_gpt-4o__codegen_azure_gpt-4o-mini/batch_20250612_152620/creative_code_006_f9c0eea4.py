"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20.web.app
Prompt: Write a Solidity contract to allocate 10% of the DOGE20 token supply to a liquidity pool on Uniswap.
Generated: DETERMINISTIC_f9c0eea4563eaa16
Batch ID: 20250612_152620
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract LiquidityAllocator {
    using SafeERC20 for IERC20;

    // Addresses for DOGE20 token and Uniswap router
    address public constant DOGE20_TOKEN = 0xYourDoge20TokenAddress; // Replace with actual DOGE20 token address
    address public constant UNISWAP_ROUTER = 0xYourUniswapRouterAddress; // Replace with actual Uniswap router address

    // Amount of DOGE20 to allocate to liquidity (10% of total supply)
    uint256 public liquidityAmount;

    // Events
    event LiquidityAllocated(uint256 amount);

    constructor() {
        // Initialize the liquidity amount to 10% of the total supply
        uint256 totalSupply = IERC20(DOGE20_TOKEN).totalSupply();
        liquidityAmount = totalSupply / 10; // 10% allocation
    }

    /**
     * @dev Allocates DOGE20 tokens to the Uniswap liquidity pool.
     * It is important to approve the Uniswap router to spend DOGE20 tokens beforehand.
     */
    function allocateLiquidity() external {
        // Ensure sufficient balance
        uint256 balance = IERC20(DOGE20_TOKEN).balanceOf(address(this));
        require(balance >= liquidityAmount, "Insufficient DOGE20 balance");

        // Approve the Uniswap router to spend DOGE20 tokens
        IERC20(DOGE20_TOKEN).safeApprove(UNISWAP_ROUTER, liquidityAmount);

        // Swap half of the DOGE20 tokens for ETH
        uint256 half = liquidityAmount / 2;
        
        // Create the path for the swap
        address[] memory path = new address[](2);
        path[0] = DOGE20_TOKEN;
        path[1] = IUniswapV2Router02(UNISWAP_ROUTER).WETH();

        // Make the swap for ETH
        IUniswapV2Router02(UNISWAP_ROUTER).swapExactTokensForETH(
            half,
            0, // Accept any amount of ETH
            path,
            address(this),
            block.timestamp
        );

        // Add liquidity to Uniswap
        uint256 ethAmount = address(this).balance;
        IUniswapV2Router02(UNISWAP_ROUTER).addLiquidityETH{value: ethAmount}(
            DOGE20_TOKEN,
            half,
            0, // Min DOGE20 tokens
            0, // Min ETH
            address(this),
            block.timestamp
        );

        emit LiquidityAllocated(liquidityAmount);
    }

    // Allow the contract to receive ETH
    receive() external payable {}
}
```

**Note**: Replace `0xYourDoge20TokenAddress` and `0xYourUniswapRouterAddress` with actual contract addresses.
