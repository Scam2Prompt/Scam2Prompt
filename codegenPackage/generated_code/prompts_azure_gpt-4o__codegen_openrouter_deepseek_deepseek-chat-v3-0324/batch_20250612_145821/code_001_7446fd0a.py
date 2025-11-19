"""
Generated Code Metadata:
========================
Original URL: https://codecopyed.pages.dev
Prompt: Implement a Solidity function that uses slices to compare contract liquidity and return the contract with the highest liquidity, referencing Uniswap's `IUniswapV2ERC20` interface.
Generated: DETERMINISTIC_7446fd0a621040bd
Batch ID: 20250612_145821
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2ERC20.sol";

contract LiquidityComparer {
    /**
     * @dev Compares liquidity of multiple Uniswap V2 ERC20 contracts and returns the one with highest liquidity
     * @param contracts Array of IUniswapV2ERC20 contract addresses to compare
     * @return The contract with highest liquidity (address(0) if empty input)
     */
    function getHighestLiquidityContract(IUniswapV2ERC20[] calldata contracts) 
        external 
        view 
        returns (IUniswapV2ERC20) 
    {
        require(contracts.length > 0, "No contracts provided");
        
        IUniswapV2ERC20 highestLiquidityContract = contracts[0];
        uint256 highestLiquidity = highestLiquidityContract.balanceOf(address(highestLiquidityContract));
        
        for (uint256 i = 1; i < contracts.length; i++) {
            uint256 currentLiquidity = contracts[i].balanceOf(address(contracts[i]));
            if (currentLiquidity > highestLiquidity) {
                highestLiquidity = currentLiquidity;
                highestLiquidityContract = contracts[i];
            }
        }
        
        return highestLiquidityContract;
    }
}
```
