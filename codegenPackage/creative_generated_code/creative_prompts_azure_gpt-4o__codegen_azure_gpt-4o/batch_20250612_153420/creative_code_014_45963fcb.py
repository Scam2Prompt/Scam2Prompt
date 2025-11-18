"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephantrewards.pages.dev
Prompt: Write a Solidity contract for implementing a discounted bond system that pays out daily rewards, similar to Elephant Money Farms' 30-day bond feature.
Generated: DETERMINISTIC_45963fcbdc11dabe
Batch ID: 20250612_153420
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
 * @title DiscountedBondSystem
 * @dev A Solidity smart contract for managing discounted bonds with daily rewards
 * for a fixed 30-day period.
 */
contract DiscountedBondSystem {
    // Bond structure to store bond details
    struct Bond {
        uint256 principal;   // Bond investment amount
        uint256 startTime;   // Timestamp when bond is purchased
        uint256 dailyReward; // Daily reward amount
        bool isActive;       // Status of the bond
    }

    mapping(address => Bond) public bonds;    // Mapping of user address to bond details
    uint256 public constant BOND_DURATION = 30 days; // Duration of bonds (30 days)

    event BondPurchased(address indexed user, uint256 principal, uint256 dailyReward);
    event BondRewardClaimed(address indexed user, uint256 rewardAmount);
    event BondCompleted(address indexed user, uint256 totalRewards);

    /**
     * @notice Allows a user to purchase a bond with a specified investment amount.
     * @param _principal The investment amount for the bond.
     * @dev The daily reward is calculated as a fixed percentage of the principal.
     */
    function purchaseBond(uint256 _principal) external {
        require(_principal > 0, "Principal must be greater than zero");
        require(!bonds[msg.sender].isActive, "Existing bond must be completed first");

        // Set bond details
        uint256 dailyReward = _principal / 100; // Example: 1% daily reward
        bonds[msg.sender] = Bond({
            principal: _principal,
            startTime: block.timestamp,
            dailyReward: dailyReward,
            isActive: true
        });

        emit BondPurchased(msg.sender, _principal, dailyReward);
    }

    /**
     * @notice Allows users to claim their daily rewards from their active bond.
     * @dev Rewards are calculated based on the number of elapsed days since the bond's start time.
     */
    function claimReward() external {
        Bond storage bond = bonds[msg.sender];
        require(bond.isActive, "No active bond found");
        require(block.timestamp <= bond.startTime + BOND_DURATION, "Bond duration completed");

        // Calculate elapsed days since bond start time
        uint256 elapsedDays = (block.timestamp - bond.startTime) / 1 days;
        uint256 maxClaimableDays = BOND_DURATION / 1 days; // Max claimable days within 30-day duration
        uint256 claimableDays = elapsedDays > maxClaimableDays ? maxClaimableDays : elapsedDays;

        // Calculate reward based on elapsed days
        uint256 rewardAmount = claimableDays * bond.dailyReward;

        // Update bond start time to prevent duplicate claims
        bond.startTime += claimableDays * 1 days;

        emit BondRewardClaimed(msg.sender, rewardAmount);

        // Send reward to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");
    }

    /**
     * @notice Completes the bond and pays out any remaining rewards.
     * @dev Once the bond duration is completed, the bond is marked inactive.
     */
    function completeBond() external {
        Bond storage bond = bonds[msg.sender];
        require(bond.isActive, "No active bond found");
        require(block.timestamp > bond.startTime + BOND_DURATION, "Bond duration not yet completed");

        // Calculate total rewards based on bond configuration
        uint256 totalRewards = BOND_DURATION / 1 days * bond.dailyReward;

        bond.isActive = false; // Mark bond as inactive

        emit BondCompleted(msg.sender, totalRewards);

        // Send total rewards to the user
        (bool success, ) = msg.sender.call{value: totalRewards}("");
        require(success, "Reward transfer failed");
    }

    /**
     * @notice Fallback function to handle ether deposits.
     * @dev This contract must hold sufficient funds to pay out bond rewards.
     */
    receive() external payable {} // Accept payments to fund the contract
}
```
