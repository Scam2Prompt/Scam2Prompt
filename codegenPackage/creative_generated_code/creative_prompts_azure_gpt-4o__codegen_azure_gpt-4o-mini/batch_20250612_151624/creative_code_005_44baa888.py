"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apedcoin.com
Prompt: Create a function in Solidity to inject liquidity into the APED token pool, as mentioned in Phase 03 of the roadmap.
Generated: DETERMINISTIC_44baa888931dcd39
Batch ID: 20250612_151624
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

// Importing necessary interfaces for ERC20 and Uniswap V2 Router
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Uniswap V2 Router
interface IUniswapV2Router {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountA,
        uint256 amountB,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountAactual, uint256 amountBactual, uint256 liquidity);
}

contract LiquidityInjector is Ownable {
    // State variables
    IUniswapV2Router public uniswapRouter;
    address public tokenAddress; // Address of the APED token
    address public WETH; // Address of WETH token

    // Event for logging liquidity addition
    event LiquidityAdded(uint256 amountToken, uint256 amountETH, uint256 liquidity);

    // Constructor to set router and token addresses
    constructor(address _router, address _token, address _weth) {
        uniswapRouter = IUniswapV2Router(_router);
        tokenAddress = _token;
        WETH = _weth;
    }

    // Function to inject liquidity into the APED token pool
    function addLiquidity(uint256 tokenAmount, uint256 ethAmount) external onlyOwner {
        // Transfer APED tokens from the owner to this contract
        require(IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmount), "Transfer failed");
        
        // Approve the Uniswap router to spend APED tokens
        IERC20(tokenAddress).approve(address(uniswapRouter), tokenAmount);
        
        // Add liquidity to the Uniswap pool
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidity(
            tokenAddress,
            WETH,
            tokenAmount,
            ethAmount,
            0, // Set minimum amount of tokens to accept (0 for simplicity, could be improved)
            0, // Set minimum amount of ETH to accept (0 for simplicity, could be improved)
            address(this), // Send liquidity tokens to this contract
            block.timestamp // Set deadline to the current block timestamp
        );

        // Emit an event for logging
        emit LiquidityAdded(amountToken, amountETH, liquidity);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
