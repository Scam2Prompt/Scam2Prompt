"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hokkaidokeneth.vip
Prompt: Write a function in Solidity to check the liquidity lock status for a token contract like Hokkaido-ken.
Generated: DETERMINISTIC_83fdb7850b828c8c
Batch ID: 20250612_151024
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

interface IToken {
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

/**
 * @title LiquidityLockChecker
 * @dev A contract to check the liquidity lock status of a given token contract.
 */
contract LiquidityLockChecker {
    // Address of the token contract to check
    IToken public token;

    // Address of the liquidity lock contract
    address public liquidityLockAddress;

    // Event emitted when the liquidity lock status is checked
    event LiquidityLockStatusChecked(bool isLocked, uint256 lockedAmount, uint256 totalSupply);

    /**
     * @dev Constructor to set the token and liquidity lock contract addresses.
     * @param _tokenAddress The address of the token contract.
     * @param _liquidityLockAddress The address of the liquidity lock contract.
     */
    constructor(address _tokenAddress, address _liquidityLockAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_liquidityLockAddress != address(0), "Invalid liquidity lock address");

        token = IToken(_tokenAddress);
        liquidityLockAddress = _liquidityLockAddress;
    }

    /**
     * @dev Checks if the liquidity is locked and returns the locked amount.
     * @return isLocked A boolean indicating if liquidity is locked.
     * @return lockedAmount The amount of tokens locked in the liquidity lock contract.
     * @return totalSupply The total supply of the token.
     */
    function checkLiquidityLockStatus() external returns (bool isLocked, uint256 lockedAmount, uint256 totalSupply) {
        totalSupply = token.totalSupply();
        lockedAmount = token.balanceOf(liquidityLockAddress);
        
        // Check if the locked amount is greater than zero
        isLocked = lockedAmount > 0;

        emit LiquidityLockStatusChecked(isLocked, lockedAmount, totalSupply);
    }
}
```
