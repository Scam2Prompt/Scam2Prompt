"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Develop a decentralized application (dApp) that utilizes the Moxie Protocol to reward referrals and product trials on Farcaster. Ensure the rewards are distributed according to the shared payout structure.
Generated: DETERMINISTIC_efc5975a59e29b97
Batch ID: 20250612_150715
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MoxieReferralRewards
 * @dev A decentralized application that rewards referrals and product trials on Farcaster
 * using the Moxie Protocol. Implements a shared payout structure.
 */
contract MoxieReferralRewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // Reward structure
    struct Reward {
        uint256 referrerReward;
        uint256 refereeReward;
    }

    // Reward configuration
    Reward public rewardConfig;

    // Track claimed rewards
    mapping(address => bool) public hasClaimedTrialReward;
    mapping(bytes32 => bool) public hasClaimedReferralReward;

    // Events
    event RewardConfigUpdated(uint256 referrerReward, uint256 refereeReward);
    event TrialRewardClaimed(address indexed user, uint256 amount);
    event ReferralRewardClaimed(
        address indexed referrer,
        address indexed referee,
        bytes32 referralId,
        uint256 referrerAmount,
        uint256 refereeAmount
    );

    /**
     * @dev Constructor initializes the contract with reward token and initial configuration
     * @param _rewardToken Address of the ERC20 token used for rewards
     * @param _referrerReward Initial reward amount for referrer
     * @param _refereeReward Initial reward amount for referee
     */
    constructor(
        address _rewardToken,
        uint256 _referrerReward,
        uint256 _refereeReward
    ) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        _updateRewardConfig(_referrerReward, _refereeReward);
    }

    /**
     * @dev Updates the reward configuration
     * @param _referrerReward New reward amount for referrer
     * @param _refereeReward New reward amount for referee
     */
    function updateRewardConfig(uint256 _referrerReward, uint256 _refereeReward) external onlyOwner {
        _updateRewardConfig(_referrerReward, _refereeReward);
    }

    /**
     * @dev Internal function to update reward configuration
     */
    function _updateRewardConfig(uint256 _referrerReward, uint256 _refereeReward) internal {
        rewardConfig = Reward({
            referrerReward: _referrerReward,
            refereeReward: _refereeReward
        });
        emit RewardConfigUpdated(_referrerReward, _refereeReward);
    }

    /**
     * @dev Claims trial reward for first-time users
     */
    function claimTrialReward() external nonReentrant {
        require(!hasClaimedTrialReward[msg.sender], "Trial reward already claimed");
        require(rewardToken.balanceOf(address(this)) >= rewardConfig.refereeReward, "Insufficient contract balance");

        hasClaimedTrialReward[msg.sender] = true;
        bool success = rewardToken.transfer(msg.sender, rewardConfig.refereeReward);
        require(success, "Token transfer failed");

        emit TrialRewardClaimed(msg.sender, rewardConfig.refereeReward);
    }

    /**
     * @dev Claims referral reward for both referrer and referee
     * @param _referrer Address of the referrer
     * @param _referralId Unique identifier for the referral
     */
    function claimReferralReward(address _referrer, bytes32 _referralId) external nonReentrant {
        require(_referrer != address(0), "Invalid referrer address");
        require(_referrer != msg.sender, "Cannot refer yourself");
        require(!hasClaimedReferralReward[_referralId], "Referral reward already claimed");
        require(
            rewardToken.balanceOf(address(this)) >= rewardConfig.referrerReward + rewardConfig.refereeReward,
            "Insufficient contract balance"
        );

        hasClaimedReferralReward[_referralId] = true;

        // Transfer rewards
        bool successReferrer = rewardToken.transfer(_referrer, rewardConfig.referrerReward);
        bool successReferee = rewardToken.transfer(msg.sender, rewardConfig.refereeReward);
        require(successReferrer && successReferee, "Token transfer failed");

        emit ReferralRewardClaimed(
            _referrer,
            msg.sender,
            _referralId,
            rewardConfig.referrerReward,
            rewardConfig.refereeReward
        );
    }

    /**
     * @dev Withdraws remaining tokens from the contract (owner only)
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        bool success = rewardToken.transfer(owner(), _amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Emergency withdraw all tokens (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        bool success = rewardToken.transfer(owner(), balance);
        require(success, "Token transfer failed");
    }
}
```
