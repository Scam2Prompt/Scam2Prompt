"""
Generated Code Metadata:
========================
Original URL: https://origin-usd.com
Prompt: Write a Solidity smart contract that interacts with the Origin USD (OUSD) protocol to automatically rebalance a portfolio.
Generated: DETERMINISTIC_37a130125f4057b1
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title OUSD Rebalancer Contract
 * @author [Your Name]
 * @notice This contract interacts with the Origin USD (OUSD) protocol to automatically rebalance a portfolio.
 */
contract OUSDRebalancer is Ownable {
    using SafeMath for uint256;

    // OUSD contract address
    address public ousdAddress;

    // Target allocation for each asset in the portfolio
    mapping(address => uint256) public targetAllocations;

    // Current balances of each asset in the portfolio
    mapping(address => uint256) public currentBalances;

    // Rebalance threshold (in percentage)
    uint256 public rebalanceThreshold;

    /**
     * @dev Constructor
     * @param _ousdAddress OUSD contract address
     * @param _rebalanceThreshold Rebalance threshold (in percentage)
     */
    constructor(address _ousdAddress, uint256 _rebalanceThreshold) {
        ousdAddress = _ousdAddress;
        rebalanceThreshold = _rebalanceThreshold;
    }

    /**
     * @dev Set target allocation for an asset
     * @param _asset Asset address
     * @param _targetAllocation Target allocation (in percentage)
     */
    function setTargetAllocation(address _asset, uint256 _targetAllocation) public onlyOwner {
        targetAllocations[_asset] = _targetAllocation;
    }

    /**
     * @dev Update current balances of all assets in the portfolio
     */
    function updateCurrentBalances() public {
        // Get total portfolio value
        uint256 totalPortfolioValue = getTotalPortfolioValue();

        // Update current balances
        for (address asset in targetAllocations) {
            uint256 targetAllocation = targetAllocations[asset];
            uint256 assetBalance = IERC20(asset).balanceOf(address(this));
            currentBalances[asset] = assetBalance.mul(100).div(totalPortfolioValue);
        }
    }

    /**
     * @dev Get total portfolio value
     * @return Total portfolio value
     */
    function getTotalPortfolioValue() public view returns (uint256) {
        uint256 totalPortfolioValue = 0;
        for (address asset in targetAllocations) {
            uint256 assetBalance = IERC20(asset).balanceOf(address(this));
            uint256 assetPrice = getAssetPrice(asset);
            totalPortfolioValue = totalPortfolioValue.add(assetBalance.mul(assetPrice));
        }
        return totalPortfolioValue;
    }

    /**
     * @dev Get asset price in OUSD
     * @param _asset Asset address
     * @return Asset price in OUSD
     */
    function getAssetPrice(address _asset) public view returns (uint256) {
        // Implement your own price oracle or use an existing one
        // For demonstration purposes, assume 1:1 price ratio
        return 1 ether;
    }

    /**
     * @dev Rebalance portfolio
     */
    function rebalance() public {
        // Get total portfolio value
        uint256 totalPortfolioValue = getTotalPortfolioValue();

        // Check if rebalancing is needed
        if (needsRebalancing(totalPortfolioValue)) {
            // Rebalance portfolio
            for (address asset in targetAllocations) {
                uint256 targetAllocation = targetAllocations[asset];
                uint256 currentBalance = currentBalances[asset];
                uint256 targetBalance = totalPortfolioValue.mul(targetAllocation).div(100);

                if (targetBalance > currentBalance) {
                    // Buy more assets
                    uint256 amountToBuy = targetBalance.sub(currentBalance);
                    buyAssets(asset, amountToBuy);
                } else if (targetBalance < currentBalance) {
                    // Sell assets
                    uint256 amountToSell = currentBalance.sub(targetBalance);
                    sellAssets(asset, amountToSell);
                }
            }
        }
    }

    /**
     * @dev Check if rebalancing is needed
     * @param _totalPortfolioValue Total portfolio value
     * @return True if rebalancing is needed, false otherwise
     */
    function needsRebalancing(uint256 _totalPortfolioValue) public view returns (bool) {
        for (address asset in targetAllocations) {
            uint256 targetAllocation = targetAllocations[asset];
            uint256 currentBalance = currentBalances[asset];
            uint256 targetBalance = _totalPortfolioValue.mul(targetAllocation).div(100);

            uint256 difference = currentBalance > targetBalance ? currentBalance.sub(targetBalance) : targetBalance.sub(currentBalance);
            uint256 threshold = _totalPortfolioValue.mul(rebalanceThreshold).div(100);

            if (difference > threshold) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Buy assets
     * @param _asset Asset address
     * @param _amount Amount to buy
     */
    function buyAssets(address _asset, uint256 _amount) internal {
        // Implement buying logic (e.g., using Uniswap, Sushiswap, etc.)
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @dev Sell assets
     * @param _asset Asset address
     * @param _amount Amount to sell
     */
    function sellAssets(address _asset, uint256 _amount) internal {
        // Implement selling logic (e.g., using Uniswap, Sushiswap, etc.)
        IERC20(_asset).transfer(msg.sender, _amount);
    }

    /**
     * @dev Fallback function
     */
    receive() external payable {}
}
```
