"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invistribe.com
Prompt: Generate a Solidity smart contract that implements a referral-based reward system similar to the Fortunity platform, allowing users to earn rewards by inviting others.
Generated: DETERMINISTIC_a5a75dff0f50c69a
Batch ID: 20250612_150426
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
 * @title ReferralRewardSystem
 * @dev A smart contract implementing a referral-based reward system.
 */
contract ReferralRewardSystem {
    address public owner;

    // Reward per referral
    uint256 public rewardAmount;

    // Mapping of user to their referrer
    mapping(address => address) public referrerOf;

    // Mapping of user to their earned rewards
    mapping(address => uint256) public rewardsEarned;

    // Event emitted when a user registers
    event UserRegistered(address indexed user, address indexed referrer);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict functions to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can execute this");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardAmount The amount rewarded per referral.
     */
    constructor(uint256 _rewardAmount) {
        owner = msg.sender;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Allows a user to register with a referrer.
     * @param _referrer The address of the referrer.
     * Requirements:
     * - The user must not already be registered.
     * - The referrer cannot be the user themselves.
     */
    function register(address _referrer) external {
        require(referrerOf[msg.sender] == address(0), "User already registered");
        require(_referrer != msg.sender, "Cannot refer yourself");
        require(_referrer == address(0) || referrerOf[_referrer] != address(0), "Referrer must be registered");

        // Assign the referrer
        referrerOf[msg.sender] = _referrer;

        // Reward the referrer
        if (_referrer != address(0)) {
            rewardsEarned[_referrer] += rewardAmount;
        }

        emit UserRegistered(msg.sender, _referrer);
    }

    /**
     * @dev Allows a user to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = rewardsEarned[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards balance before sending to avoid re-entrancy attack
        rewardsEarned[msg.sender] = 0;

        // Transfer rewards
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to fund the contract with Ether.
     */
    function fundContract() external payable onlyOwner {}

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     * @param _amount The amount to withdraw.
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient funds");
        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Updates the reward amount per referral.
     * @param _newRewardAmount The new reward amount.
     */
    function updateRewardAmount(uint256 _newRewardAmount) external onlyOwner {
        rewardAmount = _newRewardAmount;
    }

    /**
     * @dev Fallback function to allow receiving Ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Use the fundContract function to send Ether");
    }
}
```
