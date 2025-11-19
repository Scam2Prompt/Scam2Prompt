"""
Generated Code Metadata:
========================
Original URL: https://beefcom.pages.dev
Prompt: Design a simple token distribution system in Solidity, inspired by BEEF Coin's 75% DEX liquidity pool allocation.
Generated: DETERMINISTIC_d09db666ae5695c9
Batch ID: 20250622_210806
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BeefToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Address for DEX liquidity pool
    address public dexLiquidityPool;

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Allocation percentages (in basis points)
    uint256 public constant DEX_LIQUIDITY_PERCENT = 7500; // 75%
    uint256 public constant TEAM_PERCENT = 1500; // 15%
    uint256 public constant COMMUNITY_PERCENT = 1000; // 10%

    // Track distribution status
    bool private _distributionComplete;

    /**
     * @dev Constructor that mints the total supply and assigns allocations
     * @param _dexLiquidityPool Address of the DEX liquidity pool
     */
    constructor(address _dexLiquidityPool) ERC20("BEEF Coin", "BEEF") {
        require(_dexLiquidityPool != address(0), "DEX liquidity pool address cannot be zero");
        dexLiquidityPool = _dexLiquidityPool;
        
        // Mint total supply to contract
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Distribute tokens according to predefined allocations
     * Can only be called once by the owner
     */
    function distributeTokens() external onlyOwner {
        require(!_distributionComplete, "Tokens already distributed");
        
        // Calculate allocations
        uint256 dexAmount = TOTAL_SUPPLY.mul(DEX_LIQUIDITY_PERCENT).div(10000);
        uint256 teamAmount = TOTAL_SUPPLY.mul(TEAM_PERCENT).div(10000);
        uint256 communityAmount = TOTAL_SUPPLY.mul(COMMUNITY_PERCENT).div(10000);

        // Verify total distribution equals total supply
        require(
            dexAmount.add(teamAmount).add(communityAmount) == TOTAL_SUPPLY,
            "Invalid token distribution"
        );

        // Transfer tokens to respective addresses
        _transfer(address(this), dexLiquidityPool, dexAmount);
        _transfer(address(this), owner(), teamAmount); // Team allocation to owner
        _transfer(address(this), owner(), communityAmount); // Community allocation to owner

        _distributionComplete = true;
    }

    /**
     * @dev Change DEX liquidity pool address
     * @param newLiquidityPool New liquidity pool address
     */
    function setDexLiquidityPool(address newLiquidityPool) external onlyOwner {
        require(newLiquidityPool != address(0), "Invalid address");
        dexLiquidityPool = newLiquidityPool;
    }

    /**
     * @dev Check if token distribution is complete
     * @return bool Whether distribution is complete
     */
    function isDistributionComplete() external view returns (bool) {
        return _distributionComplete;
    }
}
```
