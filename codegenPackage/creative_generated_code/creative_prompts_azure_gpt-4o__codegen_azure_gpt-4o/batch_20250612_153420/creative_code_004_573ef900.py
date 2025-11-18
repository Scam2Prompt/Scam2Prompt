"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephantrewards.pages.dev
Prompt: Write a Solidity contract that implements a referral rewards system, paying out 1% rewards via staking, inspired by Elephant Money Farms' partner rewards feature.
Generated: DETERMINISTIC_573ef900626e6312
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
 * @title ReferralRewards
 * @dev This contract implements a staking-based referral rewards system where referrers earn a 1% reward.
 */
contract ReferralRewards {
    // --- State Variables ---
    uint256 public rewardPercentage = 1; // Reward percentage (1%)
    address public owner; // Contract owner for administrative purposes

    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of staking
    }

    mapping(address => Stake) public stakes; // Tracks user stakes
    mapping(address => address) public referrals; // Tracks referral relationships

    // --- Events ---
    event Staked(address indexed staker, uint256 amount);
    event RewardPaid(address indexed referrer, uint256 rewardAmount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // --- Modifiers ---
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // --- Constructor ---
    constructor() {
        owner = msg.sender; // Initial owner is the contract deployer
    }

    // --- External Functions ---
    /**
     * @dev Allows a user to stake funds.
     * @param referrer Address of the referrer (optional, can be zero address).
     */
    function stake(address referrer) external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Update the user's stake
        stakes[msg.sender].amount += msg.value;
        stakes[msg.sender].timestamp = block.timestamp;

        // Set the referrer for the user if not already set
        if (referrals[msg.sender] == address(0) && referrer != msg.sender && referrer != address(0)) {
            referrals[msg.sender] = referrer;
        }

        emit Staked(msg.sender, msg.value);

        // Pay referral reward
        address referrerAddress = referrals[msg.sender];
        if (referrerAddress != address(0)) {
            uint256 reward = (msg.value * rewardPercentage) / 100;
            (bool success, ) = referrerAddress.call{value: reward}("");
            require(success, "Failed to transfer referral reward");
            emit RewardPaid(referrerAddress, reward);
        }
    }

    /**
     * @dev Allows the owner to update the reward percentage.
     * @param newRewardPercentage The new reward percentage (e.g., 1 for 1%).
     */
    function updateRewardPercentage(uint256 newRewardPercentage) external onlyOwner {
        require(newRewardPercentage > 0 && newRewardPercentage <= 100, "Invalid reward percentage");
        rewardPercentage = newRewardPercentage;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // --- Fallback Functions ---
    receive() external payable {
        revert("Use the stake function to deposit funds");
    }
}
```
