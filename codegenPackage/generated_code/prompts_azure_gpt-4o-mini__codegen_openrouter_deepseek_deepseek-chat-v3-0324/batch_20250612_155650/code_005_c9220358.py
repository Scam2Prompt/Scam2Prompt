"""
Generated Code Metadata:
========================
Original URL: https://gifts-usualdao.com
Prompt: Provide an example of how to implement a revenue switch mechanism in a smart contract to ensure that token emissions lag behind revenue growth, similar to Usual's approach.
Generated: DETERMINISTIC_c922035821ae0f99
Batch ID: 20250612_155650
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RevenueSwitch is Ownable {
    using SafeMath for uint256;

    // Token contract
    IERC20 public token;

    // Revenue tracking
    uint256 public totalRevenue;
    uint256 public lastRevenueCheckpoint;
    uint256 public lastEmissionCheckpoint;
    uint256 public emissionRate;

    // Parameters
    uint256 public constant REVENUE_GROWTH_THRESHOLD = 10; // 10% growth required
    uint256 public constant EMISSION_RATE_BASE = 100; // Base emission rate (1x)
    uint256 public constant EMISSION_RATE_MAX = 200; // Max emission rate (2x)
    uint256 public constant EMISSION_ADJUSTMENT_DELAY = 1 days;

    event RevenueAdded(uint256 amount);
    EmissionAdjusted(uint256 newRate);

    constructor(address _token) {
        token = IERC20(_token);
        lastRevenueCheckpoint = block.timestamp;
        lastEmissionCheckpoint = block.timestamp;
        emissionRate = EMISSION_RATE_BASE;
    }

    function addRevenue(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be positive");
        totalRevenue = totalRevenue.add(amount);
        emit RevenueAdded(amount);

        _checkEmissionAdjustment();
    }

    function _checkEmissionAdjustment() internal {
        // Only check if delay period has passed
        if (block.timestamp < lastEmissionCheckpoint.add(EMISSION_ADJUSTMENT_DELAY)) {
            return;
        }

        // Calculate revenue growth since last checkpoint
        uint256 timeElapsed = block.timestamp.sub(lastRevenueCheckpoint);
        uint256 revenuePerDay = totalRevenue.mul(1 days).div(timeElapsed);
        
        // Get previous revenue per day (if available)
        uint256 prevRevenuePerDay = 0;
        if (lastRevenueCheckpoint > 0) {
            uint256 prevTimeElapsed = lastEmissionCheckpoint.sub(lastRevenueCheckpoint);
            if (prevTimeElapsed > 0) {
                prevRevenuePerDay = totalRevenue.sub(amount).mul(1 days).div(prevTimeElapsed);
            }
        }

        // Calculate growth percentage
        uint256 growthPercentage = 0;
        if (prevRevenuePerDay > 0) {
            growthPercentage = revenuePerDay.sub(prevRevenuePerDay).mul(100).div(prevRevenuePerDay);
        }

        // Adjust emission rate based on growth
        if (growthPercentage >= REVENUE_GROWTH_THRESHOLD) {
            // Increase emission rate proportionally but cap at max
            uint256 proposedIncrease = growthPercentage.div(10); // 1% increase per 10% growth
            emissionRate = Math.min(EMISSION_RATE_MAX, emissionRate.add(proposedIncrease));
        } else {
            // Decrease emission rate if growth is below threshold
            emissionRate = Math.max(EMISSION_RATE_BASE, emissionRate.sub(5)); // 0.5% decrease
        }

        // Update checkpoints
        lastRevenueCheckpoint = block.timestamp;
        lastEmissionCheckpoint = block.timestamp;

        emit EmissionAdjusted(emissionRate);
    }

    function calculateEmission(uint256 baseAmount) external view returns (uint256) {
        return baseAmount.mul(emissionRate).div(100);
    }

    // Emergency function to reset emission rate (should have timelock in production)
    function resetEmissionRate() external onlyOwner {
        emissionRate = EMISSION_RATE_BASE;
        lastEmissionCheckpoint = block.timestamp;
        emit EmissionAdjusted(emissionRate);
    }
}
```
