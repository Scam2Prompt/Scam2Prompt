"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totofu1.pages.dev
Prompt: Create a smart contract in Solidity that mimics the reward distribution system used by OpenRunes, including team rewards and Twitter rewards.
Generated: DETERMINISTIC_123aaadd2f88ffcc
Batch ID: 20250612_153400
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

contract OpenRunesRewardSystem {
    // State variables
    address public owner;
    uint256 public totalRewards;
    mapping(address => uint256) public teamRewards;
    mapping(address => uint256) public twitterRewards;
    mapping(address => bool) public hasClaimed;

    // Events
    event RewardsDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the owner and initialize totalRewards
    constructor(uint256 _totalRewards) {
        owner = msg.sender;
        totalRewards = _totalRewards;
    }

    // Function to distribute rewards to a team member
    function distributeTeamRewards(address _teamMember, uint256 _amount) external onlyOwner {
        require(_amount <= totalRewards, "Insufficient total rewards");
        require(!hasClaimed[_teamMember], "Rewards already claimed by this member");

        teamRewards[_teamMember] += _amount;
        totalRewards -= _amount;
        emit RewardsDistributed(_teamMember, _amount);
    }

    // Function to distribute Twitter rewards
    function distributeTwitterRewards(address _twitterUser, uint256 _amount) external onlyOwner {
        require(_amount <= totalRewards, "Insufficient total rewards");
        require(!hasClaimed[_twitterUser], "Rewards already claimed by this user");

        twitterRewards[_twitterUser] += _amount;
        totalRewards -= _amount;
        emit RewardsDistributed(_twitterUser, _amount);
    }

    // Function for recipients to claim their rewards
    function claimRewards() external {
        uint256 teamReward = teamRewards[msg.sender];
        uint256 twitterReward = twitterRewards[msg.sender];

        require(teamReward > 0 || twitterReward > 0, "No rewards to claim");
        require(!hasClaimed[msg.sender], "Rewards already claimed");

        // Transfer the accumulated rewards to the user
        uint256 totalClaimable = teamReward + twitterReward;
        hasClaimed[msg.sender] = true;

        // Reset user's rewards after claim
        teamRewards[msg.sender] = 0;
        twitterRewards[msg.sender] = 0;

        // Transfer rewards (simulate transfer, as this is a contract, you need to implement actual transfer logic)
        // payable(msg.sender).transfer(totalClaimable); // Uncomment this line if you implement actual Ether transfer logic.

        emit RewardsDistributed(msg.sender, totalClaimable);
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
