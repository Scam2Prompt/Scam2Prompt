"""
Generated Code Metadata:
========================
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a Solidity function that allows users to view and claim their referral rewards, similar to the "Claim Rewards" feature on the Zora Air Spring platform.
Generated: DETERMINISTIC_50c3e66d6c5d9e1d
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ReferralRewardsContract
 * @author [Your Name]
 * @notice A contract for managing referral rewards.
 */
contract ReferralRewardsContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user referrals
    mapping(address => address) public referrals;

    // Mapping of user rewards
    mapping(address => uint256) public rewards;

    // Mapping of claimed rewards
    mapping(address => bool) public claimed;

    // Reward token
    IERC20 public rewardToken;

    /**
     * @param _rewardToken Address of the reward token.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @notice Set a user's referral.
     * @param _user Address of the user.
     * @param _referral Address of the referral.
     */
    function setReferral(address _user, address _referral) public onlyOwner {
        require(_user != address(0) && _referral != address(0), "User and referral addresses cannot be zero");
        referrals[_user] = _referral;
    }

    /**
     * @notice Add rewards to a user's account.
     * @param _user Address of the user.
     * @param _amount Amount of rewards to add.
     */
    function addRewards(address _user, uint256 _amount) public onlyOwner {
        require(_user != address(0), "User address cannot be zero");
        require(_amount > 0, "Reward amount must be greater than zero");
        rewards[_user] = rewards[_user].add(_amount);
    }

    /**
     * @notice View a user's rewards.
     * @param _user Address of the user.
     * @return uint256 The user's rewards.
     */
    function viewRewards(address _user) public view returns (uint256) {
        return rewards[_user];
    }

    /**
     * @notice Claim a user's rewards.
     * @param _user Address of the user.
     */
    function claimRewards(address _user) public {
        require(_user != address(0), "User address cannot be zero");
        require(rewards[_user] > 0, "User has no rewards to claim");
        require(!claimed[_user], "User has already claimed their rewards");

        uint256 _rewards = rewards[_user];
        rewards[_user] = 0;
        claimed[_user] = true;

        // Transfer rewards to user
        require(rewardToken.transfer(_user, _rewards), "Failed to transfer rewards");
    }
}
```
