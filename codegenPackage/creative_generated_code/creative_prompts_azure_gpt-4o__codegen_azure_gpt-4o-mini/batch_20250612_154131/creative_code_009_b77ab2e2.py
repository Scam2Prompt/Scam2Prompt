"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curvefi.co
Prompt: Generate a Solidity contract snippet for interacting with Curve Finance's liquidity pools to provide liquidity and earn rewards.
Generated: DETERMINISTIC_b77ab2e25bee99d3
Batch ID: 20250612_154131
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Curve's liquidity pool
interface ICurvePool {
    function add_liquidity(uint256[2] calldata amounts, uint256 min_mint_amount) external;
    function remove_liquidity(uint256 _amount, uint256[2] calldata min_amounts) external;
}

contract CurveLiquidityProvider is ReentrancyGuard, Ownable {
    // Address of the Curve liquidity pool
    address public curvePool;

    // Events for logging actions
    event LiquidityAdded(uint256 amountA, uint256 amountB, uint256 minted);
    event LiquidityRemoved(uint256 amount, uint256[2] minAmounts);

    // Constructor to set the Curve pool address
    constructor(address _curvePool) {
        require(_curvePool != address(0), "Invalid pool address");
        curvePool = _curvePool;
    }

    // Function to provide liquidity to the Curve pool
    function provideLiquidity(uint256 amountA, uint256 amountB, uint256 minMintAmount) external nonReentrant {
        // Transfer tokens from user to this contract
        IERC20 tokenA = IERC20(0x...); // Replace with actual token A address
        IERC20 tokenB = IERC20(0x...); // Replace with actual token B address
        
        require(tokenA.transferFrom(msg.sender, address(this), amountA), "Transfer of token A failed");
        require(tokenB.transferFrom(msg.sender, address(this), amountB), "Transfer of token B failed");

        // Approve the Curve pool to spend the tokens
        tokenA.approve(curvePool, amountA);
        tokenB.approve(curvePool, amountB);

        // Add liquidity to the Curve pool
        uint256[2] memory amounts = [amountA, amountB];
        // Call the add_liquidity function of the Curve pool
        ICurvePool(curvePool).add_liquidity(amounts, minMintAmount);

        // Emit event for liquidity added
        emit LiquidityAdded(amountA, amountB, minMintAmount);
    }

    // Function to remove liquidity from the Curve pool
    function removeLiquidity(uint256 amount, uint256 minAmountA, uint256 minAmountB) external nonReentrant {
        // Transfer liquidity tokens from user to this contract
        IERC20 curveToken = IERC20(curvePool); // Assuming the Curve pool itself is an ERC20 token
        require(curveToken.transferFrom(msg.sender, address(this), amount), "Transfer of Curve token failed");

        // Approve the Curve pool to spend the liquidity tokens
        curveToken.approve(curvePool, amount);

        // Call the remove_liquidity function of the Curve pool
        uint256[2] memory minAmounts = [minAmountA, minAmountB];
        ICurvePool(curvePool).remove_liquidity(amount, minAmounts);

        // Emit event for liquidity removed
        emit LiquidityRemoved(amount, minAmounts);
    }

    // Function to withdraw the contract's tokens (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```

Make sure to replace the placeholder addresses for token A, token B, and the Curve pool with actual deployed contract addresses before deploying the contract.
