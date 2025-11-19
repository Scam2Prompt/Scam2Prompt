"""
Generated Code Metadata:
========================
Original URL: https://aipepetrader-c9j0k84jr-edrive.vercel.app
Prompt: Create an example of a referral reward system in a smart contract that aligns with the Ai Pepe Trader's airdrop strategy.
Generated: DETERMINISTIC_cf36702d92c05980
Batch ID: 20250612_161420
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ReferralRewardSystem
 * @author [Your Name]
 * @notice A smart contract that manages a referral reward system.
 */
contract ReferralRewardSystem is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their referral counts
    mapping(address => uint256) public referralCounts;

    // Mapping of users to their referral rewards
    mapping(address => uint256) public referralRewards;

    // Mapping of users to their referrers
    mapping(address => address) public referrers;

    // ERC20 token contract for rewards
    ERC20 public rewardToken;

    // Reward amount for each referral
    uint256 public rewardAmount;

    // Maximum number of referrals allowed
    uint256 public maxReferrals;

    // Event emitted when a user refers another user
    event Referral(address indexed referrer, address indexed user);

    // Event emitted when a referral reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @param _rewardToken Address of the ERC20 token contract for rewards
     * @param _rewardAmount Reward amount for each referral
     * @param _maxReferrals Maximum number of referrals allowed
     */
    constructor(
        address _rewardToken,
        uint256 _rewardAmount,
        uint256 _maxReferrals
    ) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(_maxReferrals > 0, "Max referrals must be greater than zero");

        rewardToken = ERC20(_rewardToken);
        rewardAmount = _rewardAmount;
        maxReferrals = _maxReferrals;
    }

    /**
     * @notice Refer a user and earn a reward
     * @param _user Address of the user to refer
     */
    function refer(address _user) external nonReentrant {
        require(_user != address(0), "User address cannot be zero");
        require(referrers[_user] == address(0), "User has already been referred");

        // Check if the referrer has not exceeded the max referrals
        require(referralCounts[msg.sender] < maxReferrals, "Max referrals exceeded");

        // Update referral counts and rewards
        referralCounts[msg.sender] = referralCounts[msg.sender].add(1);
        referralRewards[msg.sender] = referralRewards[msg.sender].add(rewardAmount);

        // Set the referrer for the user
        referrers[_user] = msg.sender;

        // Emit referral event
        emit Referral(msg.sender, _user);
    }

    /**
     * @notice Claim referral rewards
     */
    function claimRewards() external nonReentrant {
        require(referralRewards[msg.sender] > 0, "No rewards to claim");

        // Transfer reward to user
        uint256 reward = referralRewards[msg.sender];
        referralRewards[msg.sender] = 0;
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Emit reward claimed event
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Get the referral count for a user
     * @param _user Address of the user
     * @return Referral count
     */
    function getReferralCount(address _user) external view returns (uint256) {
        return referralCounts[_user];
    }

    /**
     * @notice Get the referral reward for a user
     * @param _user Address of the user
     * @return Referral reward
     */
    function getReferralReward(address _user) external view returns (uint256) {
        return referralRewards[_user];
    }

    /**
     * @notice Get the referrer for a user
     * @param _user Address of the user
     * @return Referrer address
     */
    function getReferrer(address _user) external view returns (address) {
        return referrers[_user];
    }
}
```
