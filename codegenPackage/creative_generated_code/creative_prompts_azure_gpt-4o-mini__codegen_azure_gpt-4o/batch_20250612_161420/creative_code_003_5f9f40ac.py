"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miner-pepebnb2.vercel.app
Prompt: How can I implement a referral system in a smart contract that rewards users with a percentage of their referrals' deposits?
Generated: DETERMINISTIC_5f9f40ac1d45fb98
Batch ID: 20250612_161420
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
 * @title ReferralSystem
 * @dev A simple referral system in a smart contract that rewards users with a percentage of their referrals' deposits.
 */
contract ReferralSystem {
    // A percentage (e.g., 5%) that referrers will earn from their referrals' deposits
    uint256 public constant REFERRAL_REWARD_PERCENTAGE = 5;

    // Mapping to store referrers for each user
    mapping(address => address) public referrers;

    // Mapping to store rewards earned by each user
    mapping(address => uint256) public rewards;

    // Event emitted when a user makes a deposit
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a referrer earns a reward
    event Reward(address indexed referrer, uint256 reward);

    /**
     * @notice Allows a user to register a referrer.
     * @param _referrer The address of the referrer.
     */
    function registerReferrer(address _referrer) external {
        require(_referrer != msg.sender, "You cannot refer yourself");
        require(referrers[msg.sender] == address(0), "Referrer already registered");
        require(_referrer != address(0), "Invalid referrer");

        referrers[msg.sender] = _referrer;
    }

    /**
     * @notice Allows a user to make a deposit and rewards their referrer if registered.
     * @dev Referrer will earn a percentage of the deposit amount.
     * @param _amount The amount being deposited.
     */
    function deposit(uint256 _amount) external payable {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(msg.value == _amount, "Incorrect value sent");

        emit Deposit(msg.sender, _amount);

        // Check if the user has a registered referrer
        address referrer = referrers[msg.sender];
        if (referrer != address(0)) {
            // Calculate the reward for the referrer
            uint256 reward = (_amount * REFERRAL_REWARD_PERCENTAGE) / 100;

            // Update the referrer's rewards balance
            rewards[referrer] += reward;

            emit Reward(referrer, reward);
        }
    }

    /**
     * @notice Allows a user to withdraw their accumulated rewards.
     */
    function withdrawRewards() external {
        uint256 rewardBalance = rewards[msg.sender];
        require(rewardBalance > 0, "No rewards available for withdrawal");

        // Reset the reward balance to zero before transferring
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user's wallet
        payable(msg.sender).transfer(rewardBalance);
    }

    /**
     * @notice Fallback function to receive Ether directly.
     */
    receive() external payable {}

    /**
     * @notice Prevent accidental Ether transfers by rejecting calls without data.
     */
    fallback() external payable {
        revert("Invalid call");
    }
}
```
