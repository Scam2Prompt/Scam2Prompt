"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeek.social
Prompt: Generate code to integrate a referral system in a Web3 SocialFi Dapp similar to Zeek Network.
Generated: DETERMINISTIC_39f42b4b0e608479
Batch ID: 20250612_161035
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
 * @dev A smart contract for integrating a referral system in a Web3 SocialFi Dapp.
 */
contract ReferralSystem {
    // Struct to represent referral data
    struct Referral {
        address referrer; // Address of the referrer
        uint256 reward;   // Reward earned by the referrer
    }

    // Mapping to store referrals for each user
    mapping(address => Referral) public referrals;

    // Mapping to track the total rewards for each referrer
    mapping(address => uint256) public totalRewards;

    // Event emitted when a user is referred
    event UserReferred(address indexed referee, address indexed referrer);

    // Event emitted when a reward is distributed
    event RewardDistributed(address indexed referrer, uint256 rewardAmount);

    // Modifier to ensure valid addresses
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address provided");
        _;
    }

    /**
     * @dev Records a referral and associates a referrer with a new user.
     * @param _referee Address of the referred user.
     * @param _referrer Address of the referrer.
     */
    function recordReferral(address _referee, address _referrer)
        external
        validAddress(_referee)
        validAddress(_referrer)
    {
        require(referrals[_referee].referrer == address(0), "User already referred");
        require(_referee != _referrer, "Cannot refer self");

        // Record the referral
        referrals[_referee] = Referral({referrer: _referrer, reward: 0});

        emit UserReferred(_referee, _referrer);
    }

    /**
     * @dev Distributes rewards to the referrer based on the referral system logic.
     * @param _referee Address of the referred user.
     * @param _rewardAmount Amount of reward to distribute.
     */
    function distributeReward(address _referee, uint256 _rewardAmount)
        external
        validAddress(_referee)
    {
        require(referrals[_referee].referrer != address(0), "No referrer found for this user");

        address referrer = referrals[_referee].referrer;

        // Update the referrer's total rewards
        referrals[_referee].reward += _rewardAmount;
        totalRewards[referrer] += _rewardAmount;

        emit RewardDistributed(referrer, _rewardAmount);
    }

    /**
     * @dev Retrieves referral information for a given user.
     * @param _user Address of the user.
     * @return referrer Address of the referrer.
     * @return reward Total reward earned by the referrer from this user.
     */
    function getReferralInfo(address _user)
        external
        view
        validAddress(_user)
        returns (address referrer, uint256 reward)
    {
        referrer = referrals[_user].referrer;
        reward = referrals[_user].reward;
    }

    /**
     * @dev Retrieves the total rewards earned by a specific referrer.
     * @param _referrer Address of the referrer.
     * @return Total rewards earned by the referrer.
     */
    function getTotalRewards(address _referrer)
        external
        view
        validAddress(_referrer)
        returns (uint256)
    {
        return totalRewards[_referrer];
    }
}
```
