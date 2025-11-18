"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstake-myblend.pages.dev
Prompt: Generate code to implement a referral system for a decentralized staking platform, allowing users to earn rewards by referring others to stake BLEND tokens.
Generated: DETERMINISTIC_65f74278b6ff70be
Batch ID: 20250612_145919
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

contract ReferralSystem {
    // State variables
    address public owner;
    uint256 public referralReward; // Reward for referring a new staker
    mapping(address => uint256) public rewards; // Stores rewards for each referrer
    mapping(address => address) public referrals; // Maps each user to their referrer
    mapping(address => bool) public hasStaked; // Tracks if a user has staked BLEND tokens

    // Events
    event NewReferral(address indexed referrer, address indexed referee);
    event RewardClaimed(address indexed referrer, uint256 reward);
    
    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _referralReward) {
        owner = msg.sender; // Set the contract deployer as the owner
        referralReward = _referralReward; // Set the referral reward amount
    }

    // Function to allow users to stake tokens and create referrals
    function stake(address _referrer) external {
        require(_referrer != msg.sender, "You cannot refer yourself.");
        require(!hasStaked[msg.sender], "You have already staked.");

        // Record the referral if it does not exist
        if (referrals[msg.sender] == address(0)) {
            referrals[msg.sender] = _referrer; // Map the referrer
            rewards[_referrer] += referralReward; // Increment reward for the referrer
            emit NewReferral(_referrer, msg.sender); // Emit an event for new referral
        }

        // Logic to handle staking BLEND tokens would go here
        hasStaked[msg.sender] = true; // Mark the user as having staked
    }

    // Function for referrer to claim their rewards
    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "You have no rewards to claim.");

        // Logic to transfer the reward to the referrer would go here

        rewards[msg.sender] = 0; // Reset the reward after claiming
        emit RewardClaimed(msg.sender, reward); // Emit an event for claiming reward
    }

    // Function for the owner to withdraw funds (if applicable)
    function withdraw() external onlyOwner {
        // Logic for owner to withdraw funds collected would go here
    }

    // Function to update the referral reward, only callable by the owner
    function setReferralReward(uint256 _referralReward) external onlyOwner {
        referralReward = _referralReward;
    }

    // Function to retrieve the current referral reward
    function getReferralReward() external view returns (uint256) {
        return referralReward;
    }

    // Fallback function to prevent accidental Ether transfer
    receive() external payable {
        revert("Direct Ether transfers not allowed.");
    }
}
```
