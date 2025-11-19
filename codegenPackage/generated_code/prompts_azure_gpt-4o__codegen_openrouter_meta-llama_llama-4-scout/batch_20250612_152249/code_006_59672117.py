"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Generate a Solidity contract that burns liquidity pool tokens as part of the `$gummy` tokenomics strategy, ensuring compliance with the allocation percentages provided.
Generated: DETERMINISTIC_596721175f6b8947
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title GummyTokenomicsStrategy
 * @author [Your Name]
 * @notice This contract burns liquidity pool tokens as part of the $gummy tokenomics strategy.
 */
contract GummyTokenomicsStrategy {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of liquidity pool tokens to their respective allocation percentages
    mapping(address => uint256) public poolTokenAllocations;

    // Mapping of liquidity pool tokens to their respective balances
    mapping(address => uint256) public poolTokenBalances;

    // Address of the $gummy token
    address public gummyTokenAddress;

    // Total allocation percentage
    uint256 public totalAllocationPercentage;

    // Event emitted when a liquidity pool token is burned
    event BurnedLiquidityPoolToken(address indexed poolToken, uint256 amount);

    /**
     * @notice Constructor
     * @param _gummyTokenAddress Address of the $gummy token
     */
    constructor(address _gummyTokenAddress) {
        require(_gummyTokenAddress != address(0), "GummyTokenomicsStrategy: gummy token address cannot be zero");

        gummyTokenAddress = _gummyTokenAddress;
    }

    /**
     * @notice Adds a liquidity pool token to the strategy with its allocation percentage
     * @param _poolToken Address of the liquidity pool token
     * @param _allocationPercentage Allocation percentage of the liquidity pool token
     */
    function addPoolToken(address _poolToken, uint256 _allocationPercentage) public {
        require(_poolToken != address(0), "GummyTokenomicsStrategy: pool token address cannot be zero");
        require(_allocationPercentage > 0, "GummyTokenomicsStrategy: allocation percentage must be greater than zero");

        poolTokenAllocations[_poolToken] = _allocationPercentage;
        totalAllocationPercentage = totalAllocationPercentage.add(_allocationPercentage);
    }

    /**
     * @notice Burns liquidity pool tokens according to their allocation percentages
     */
    function burnPoolTokens() public {
        require(totalAllocationPercentage == 100, "GummyTokenomicsStrategy: total allocation percentage must equal 100");

        for (address poolToken in poolTokenAllocations) {
            uint256 poolTokenBalance = IERC20(poolToken).balanceOf(address(this));
            uint256 allocationPercentage = poolTokenAllocations[poolToken];

            uint256 burnAmount = poolTokenBalance.mul(allocationPercentage).div(100);

            // Burn the liquidity pool tokens
            IERC20(poolToken).safeTransfer(address(0x000000000000000000000000000000000000dEaD), burnAmount);

            // Update the pool token balance
            poolTokenBalances[poolToken] = poolTokenBalances[poolToken].sub(burnAmount);

            emit BurnedLiquidityPoolToken(poolToken, burnAmount);
        }
    }

    /**
     * @notice Deposits liquidity pool tokens into the strategy
     * @param _poolToken Address of the liquidity pool token
     * @param _amount Amount of liquidity pool tokens to deposit
     */
    function depositPoolToken(address _poolToken, uint256 _amount) public {
        require(_poolToken != address(0), "GummyTokenomicsStrategy: pool token address cannot be zero");
        require(_amount > 0, "GummyTokenomicsStrategy: deposit amount must be greater than zero");

        IERC20(_poolToken).safeTransferFrom(msg.sender, address(this), _amount);

        // Update the pool token balance
        poolTokenBalances[_poolToken] = poolTokenBalances[_poolToken].add(_amount);
    }

    /**
     * @notice Withdraws liquidity pool tokens from the strategy
     * @param _poolToken Address of the liquidity pool token
     * @param _amount Amount of liquidity pool tokens to withdraw
     */
    function withdrawPoolToken(address _poolToken, uint256 _amount) public {
        require(_poolToken != address(0), "GummyTokenomicsStrategy: pool token address cannot be zero");
        require(_amount > 0, "GummyTokenomicsStrategy: withdrawal amount must be greater than zero");
        require(poolTokenBalances[_poolToken] >= _amount, "GummyTokenomicsStrategy: insufficient pool token balance");

        IERC20(_poolToken).safeTransfer(msg.sender, _amount);

        // Update the pool token balance
        poolTokenBalances[_poolToken] = poolTokenBalances[_poolToken].sub(_amount);
    }
}
```
