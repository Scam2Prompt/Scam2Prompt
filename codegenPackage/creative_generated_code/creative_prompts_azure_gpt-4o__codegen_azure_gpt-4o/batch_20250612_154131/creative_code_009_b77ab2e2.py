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

/**
 * @title CurveLiquidityProvider
 * @dev A smart contract for interacting with Curve Finance's liquidity pools to provide liquidity and earn rewards.
 */
interface ICurvePool {
    function add_liquidity(uint256[] calldata amounts, uint256 min_mint_amount) external;
    function remove_liquidity(uint256 _amount, uint256[] calldata min_amounts) external;
    function balanceOf(address account) external view returns (uint256);
}

contract CurveLiquidityProvider {
    // Address of the Curve pool contract
    ICurvePool public curvePool;
    
    // Address of the ERC20 tokens used in the pool
    address[] public poolTokens;

    /**
     * @dev Sets the Curve pool contract address.
     * @param _curvePool Address of the Curve pool contract.
     * @param _poolTokens Array of token addresses used in the Curve pool.
     */
    constructor(address _curvePool, address[] memory _poolTokens) {
        require(_curvePool != address(0), "Invalid Curve pool address");
        curvePool = ICurvePool(_curvePool);
        poolTokens = _poolTokens;
    }

    /**
     * @dev Provides liquidity to the Curve pool.
     * @param amounts Array of token amounts to deposit.
     * @param minMintAmount Minimum amount of LP tokens to mint.
     */
    function provideLiquidity(uint256[] calldata amounts, uint256 minMintAmount) external {
        require(amounts.length == poolTokens.length, "Invalid token amounts length");

        // Transfer tokens from the sender to the contract
        for (uint256 i = 0; i < poolTokens.length; i++) {
            IERC20(poolTokens[i]).transferFrom(msg.sender, address(this), amounts[i]);
            IERC20(poolTokens[i]).approve(address(curvePool), amounts[i]);
        }

        // Add liquidity to the Curve pool
        curvePool.add_liquidity(amounts, minMintAmount);
    }

    /**
     * @dev Removes liquidity from the Curve pool.
     * @param _amount Amount of LP tokens to burn.
     * @param minAmounts Array of minimum token amounts to receive.
     */
    function removeLiquidity(uint256 _amount, uint256[] calldata minAmounts) external {
        require(_amount > 0, "Invalid LP token amount");

        // Remove liquidity from the Curve pool
        curvePool.remove_liquidity(_amount, minAmounts);

        // Transfer received tokens back to the sender
        for (uint256 i = 0; i < poolTokens.length; i++) {
            uint256 balance = IERC20(poolTokens[i]).balanceOf(address(this));
            if (balance > 0) {
                IERC20(poolTokens[i]).transfer(msg.sender, balance);
            }
        }
    }

    /**
     * @dev Retrieves the balance of LP tokens held by the contract.
     * @return The balance of LP tokens.
     */
    function getLPBalance() external view returns (uint256) {
        return curvePool.balanceOf(address(this));
    }
}

/**
 * @dev Minimal interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
