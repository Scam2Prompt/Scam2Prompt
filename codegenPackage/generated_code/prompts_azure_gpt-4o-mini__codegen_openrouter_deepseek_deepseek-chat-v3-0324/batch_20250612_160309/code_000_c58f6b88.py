"""
Generated Code Metadata:
========================
Original URL: https://lynexfl.org
Prompt: How can I use Lynex's AMM technology to optimize liquidity distribution for my DeFi project on the Linea blockchain?
Generated: DETERMINISTIC_c58f6b8883d6d9f1
Batch ID: 20250612_160309
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface ILynexAMM {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);

    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB);

    function getReserves(address tokenA, address tokenB) external view returns (uint reserveA, uint reserveB);
}

contract LynexLiquidityOptimizer is Ownable, ReentrancyGuard {
    ILynexAMM public lynexAMM;
    address public lineaToken;
    address public projectToken;

    event LiquidityAdded(uint amountA, uint amountB, uint liquidity);
    event LiquidityRemoved(uint amountA, uint amountB);
    event LiquidityReallocated(uint newAmountA, uint newAmountB);

    constructor(address _lynexAMM, address _lineaToken, address _projectToken) {
        require(_lynexAMM != address(0), "Invalid Lynex AMM address");
        require(_lineaToken != address(0), "Invalid Linea token address");
        require(_projectToken != address(0), "Invalid project token address");

        lynexAMM = ILynexAMM(_lynexAMM);
        lineaToken = _lineaToken;
        projectToken = _projectToken;
    }

    /**
     * @dev Adds liquidity to the Lynex AMM pool
     * @param amountADesired Amount of tokenA (Linea) desired
     * @param amountBDesired Amount of tokenB (Project) desired
     * @param amountAMin Minimum amount of tokenA to add
     * @param amountBMin Minimum amount of tokenB to add
     * @param deadline Transaction deadline
     */
    function addLiquidity(
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external onlyOwner nonReentrant {
        // Transfer tokens from owner to contract
        IERC20(lineaToken).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(projectToken).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve Lynex AMM to spend tokens
        IERC20(lineaToken).approve(address(lynexAMM), amountADesired);
        IERC20(projectToken).approve(address(lynexAMM), amountBDesired);

        // Add liquidity
        (uint amountA, uint amountB, uint liquidity) = lynexAMM.addLiquidity(
            lineaToken,
            projectToken,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            address(this),
            deadline
        );

        emit LiquidityAdded(amountA, amountB, liquidity);
    }

    /**
     * @dev Removes liquidity from the Lynex AMM pool
     * @param liquidity Amount of liquidity tokens to remove
     * @param amountAMin Minimum amount of tokenA to receive
     * @param amountBMin Minimum amount of tokenB to receive
     * @param deadline Transaction deadline
     */
    function removeLiquidity(
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external onlyOwner nonReentrant {
        // Remove liquidity
        (uint amountA, uint amountB) = lynexAMM.removeLiquidity(
            lineaToken,
            projectToken,
            liquidity,
            amountAMin,
            amountBMin,
            address(this),
            deadline
        );

        emit LiquidityRemoved(amountA, amountB);
    }

    /**
     * @dev Optimizes liquidity distribution based on current reserves
     * @param targetRatio Target ratio of tokenA/tokenB (in wei)
     * @param slippageTolerance Acceptable slippage percentage (e.g., 1 = 1%)
     * @param deadline Transaction deadline
     */
    function optimizeLiquidity(
        uint targetRatio,
        uint slippageTolerance,
        uint deadline
    ) external onlyOwner nonReentrant {
        (uint reserveA, uint reserveB) = lynexAMM.getReserves(lineaToken, projectToken);
        require(reserveA > 0 && reserveB > 0, "No liquidity in pool");

        uint currentRatio = (reserveA * 1e18) / reserveB;
        
        if (currentRatio > targetRatio) {
            // Too much tokenA, need to add more tokenB
            uint amountBToAdd = ((reserveA * 1e18 / targetRatio) - reserveB) * (100 - slippageTolerance) / 100;
            uint amountADesired = 0;
            
            addLiquidity(
                amountADesired,
                amountBToAdd,
                0,
                amountBToAdd * (100 - slippageTolerance) / 100,
                deadline
            );
        } else if (currentRatio < targetRatio) {
            // Too much tokenB, need to add more tokenA
            uint amountAToAdd = ((reserveB * targetRatio / 1e18) - reserveA) * (100 - slippageTolerance) / 100;
            uint amountBDesired = 0;
            
            addLiquidity(
                amountAToAdd,
                amountBDesired,
                amountAToAdd * (100 - slippageTolerance) / 100,
                0,
                deadline
            );
        }

        emit LiquidityReallocated(reserveA, reserveB);
    }

    /**
     * @dev Withdraws tokens from the contract (emergency use only)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address token, uint amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
