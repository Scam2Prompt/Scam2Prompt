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

contract ReferralRewardSystem {
    // State variables
    address public owner;
    uint256 public rewardAmount; // Reward amount for each referral
    mapping(address => address) public referrer; // Maps user to their referrer
    mapping(address => uint256) public referralCount; // Count of referrals per user
    mapping(address => bool) public hasClaimedReward; // Track claimed rewards

    // Events
    event RewardClaimed(address indexed user, address indexed referrer, uint256 reward);
    event NewReferral(address indexed user, address indexed referrer);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _rewardAmount) {
        owner = msg.sender; // Set contract deployer as owner
        rewardAmount = _rewardAmount; // Set the reward amount
    }

    // Function to set the reward amount (only owner)
    function setRewardAmount(uint256 _rewardAmount) external onlyOwner {
        rewardAmount = _rewardAmount;
    }

    // Function to invite a new user
    function inviteUser(address _referrer) external {
        // Ensure the user is not inviting themselves and has not been referred already
        require(msg.sender != _referrer, "You cannot refer yourself");
        require(referrer[msg.sender] == address(0), "You have already been referred");

        // Assign the referrer
        referrer[msg.sender] = _referrer;
        referralCount[_referrer] += 1;

        emit NewReferral(msg.sender, _referrer); // Emit event for new referral
    }

    // Function to claim rewards based on referrals
    function claimReward() external {
        // Ensure the user has a referrer and has not claimed the reward before
        require(referrer[msg.sender] != address(0), "You do not have a referrer");
        require(!hasClaimedReward[msg.sender], "Reward has already been claimed");

        // Calculate the reward based on the number of referrals
        uint256 reward = referralCount[referrer[msg.sender]] * rewardAmount;

        // Mark the reward as claimed
        hasClaimedReward[msg.sender] = true;

        // Transfer the reward to the user
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, referrer[msg.sender], reward); // Emit event for claiming reward
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
