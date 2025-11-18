"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riftproject.pages.dev
Prompt: Write a smart contract in Solidity to implement a referral reward mechanism similar to the $RIFT referral system described on the Rift Swap website.
Generated: DETERMINISTIC_39b52cd635912fd6
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ReferralReward
 * @dev This contract implements a referral reward mechanism.
 */
contract ReferralReward is Ownable {
    using SafeMath for uint256;

    // Events
    event ReferralRegistered(address indexed referrer, address indexed referee);
    event RewardsClaimed(address indexed user, uint256 amount);

    // State variables
    IERC20 public rewardToken; // Token to be rewarded
    uint256 public referralReward; // Reward amount for referrals

    // Mapping to track referrals
    mapping(address => address) public referrals; // referrer => referee
    mapping(address => uint256) public rewards; // user => accumulated rewards

    // Constructor to set the reward token and reward amount
    constructor(IERC20 _rewardToken, uint256 _referralReward) {
        rewardToken = _rewardToken;
        referralReward = _referralReward;
    }

    /**
     * @dev Registers a referral.
     * @param referrer The address of the referrer.
     */
    function registerReferral(address referrer) external {
        require(referrer != msg.sender, "You cannot refer yourself.");
        require(referrals[msg.sender] == address(0), "Referral already registered.");

        referrals[msg.sender] = referrer;

        // Reward the referrer
        rewards[referrer] = rewards[referrer].add(referralReward);
        emit ReferralRegistered(referrer, msg.sender);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim.");

        // Reset the rewards for the user
        rewards[msg.sender] = 0;

        // Transfer the reward tokens to the user
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance.");
        rewardToken.transfer(msg.sender, amount);

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance.");
        rewardToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Updates the referral reward amount.
     * @param newReward The new reward amount for referrals.
     */
    function updateReferralReward(uint256 newReward) external onlyOwner {
        referralReward = newReward;
    }
}
```
