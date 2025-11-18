"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappv2reclaim.pages.dev
Prompt: Write a smart contract that interacts with Uniswap to provide liquidity to a pool and earn fees. Include initialization for supported chains.
Generated: DETERMINISTIC_4239ace7c1d25340
Batch ID: 20250612_152321
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

// Importing necessary interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Pair.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LiquidityProvider {
    // Declare variables
    IUniswapV2Router02 public uniswapRouter; // Uniswap router interface
    address public liquidityToken; // Token for providing liquidity
    address public weth; // Wrapped Ether address
    address public owner; // Contract owner

    // Event for logging liquidity provision
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount, uint256 liquidity);

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _router, address _liquidityToken) {
        uniswapRouter = IUniswapV2Router02(_router);
        liquidityToken = _liquidityToken;
        weth = uniswapRouter.WETH(); // Get WETH address
        owner = msg.sender; // Set contract deployer as owner
    }

    // Function to provide liquidity to the Uniswap pool
    function provideLiquidity(uint256 tokenAmount, uint256 ethAmount) external payable onlyOwner {
        require(msg.value == ethAmount, "ETH amount does not match value sent");
        
        // Transfer the token to this contract for liquidity provision
        IERC20(liquidityToken).transferFrom(msg.sender, address(this), tokenAmount);

        // Approve the Uniswap router to spend the token
        IERC20(liquidityToken).approve(address(uniswapRouter), tokenAmount);

        // Add liquidity to the pool
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: ethAmount}(
            liquidityToken,
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            address(this),
            block.timestamp
        );

        // Emit an event for successful liquidity provision
        emit LiquidityAdded(amountToken, amountETH, liquidity);
    }

    // Function to withdraw tokens and ETH from the contract
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 _amount) external onlyOwner {
        payable(msg.sender).transfer(_amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
