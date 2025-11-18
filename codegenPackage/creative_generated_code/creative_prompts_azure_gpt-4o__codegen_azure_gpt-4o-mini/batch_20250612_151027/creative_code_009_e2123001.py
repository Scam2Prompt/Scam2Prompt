"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-d2u.pages.dev
Prompt: Write a Solidity contract for managing token rewards and referrals, inspired by the Nyan Heroes platform.
Generated: DETERMINISTIC_e21230011e2b56be
Batch ID: 20250612_151027
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

// Importing OpenZeppelin libraries for safe math and ERC20 token functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for managing token rewards and referrals
contract TokenRewardReferral is Ownable {
    // State variables
    IERC20 public rewardToken;               // ERC20 token used for rewards
    mapping(address => uint256) public rewards;  // Mapping to track rewards for each user
    mapping(address => address) public referrals; // Mapping for storing referrer for each user

    event RewardClaimed(address indexed user, uint256 amount);
    event ReferralSet(address indexed user, address indexed referrer);

    // Constructor to initialize the reward token address
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    // Function to set a referral for a user
    function setReferral(address _referrer) external {
        require(_referrer != address(0), "Referrer cannot be the zero address");
        require(referrals[msg.sender] == address(0), "Referral already set");

        // Set the referrer
        referrals[msg.sender] = _referrer;

        emit ReferralSet(msg.sender, _referrer);
    }

    // Function to reward a user
    function rewardUser(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "User cannot be the zero address");
        require(_amount > 0, "Reward amount must be greater than zero");

        // Update the user's total rewards
        rewards[_user] += _amount;

        // Transfer tokens from the contract to the user
        require(rewardToken.transfer(_user, _amount), "Token transfer failed");

        emit RewardClaimed(_user, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transfer
        rewards[msg.sender] = 0;

        // Transfer tokens from the contract to the user
        require(rewardToken.transfer(msg.sender, amount), "Token transfer failed");

        emit RewardClaimed(msg.sender, amount);
    }

    // Function to check the rewards of a user
    function checkRewards(address _user) external view returns (uint256) {
        return rewards[_user];
    }

    // Function to check the referrer of a user
    function checkReferrer(address _user) external view returns (address) {
        return referrals[_user];
    }
}
```
