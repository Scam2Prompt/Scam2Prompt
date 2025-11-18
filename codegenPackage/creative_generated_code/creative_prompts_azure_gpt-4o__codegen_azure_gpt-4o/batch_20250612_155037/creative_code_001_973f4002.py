"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Generate a Solidity smart contract example that implements a reward system based on social media follower milestones, similar to the $WING tokenomics structure.
Generated: DETERMINISTIC_973f400262e7104a
Batch ID: 20250612_155037
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
 * @title SocialMediaRewardToken
 * @dev Implements a reward system based on social media follower milestones.
 */
contract SocialMediaRewardToken {
    // Token details
    string public name = "RewardToken";
    string public symbol = "RTKN";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Reward configuration for follower milestones
    struct Milestone {
        uint256 followers; // Number of followers required to unlock the milestone
        uint256 rewardAmount; // Reward amount for the milestone
    }

    // Address of the contract owner
    address public owner;

    // Mapping to track balances of users
    mapping(address => uint256) public balanceOf;

    // List of predefined milestones
    Milestone[] public milestones;

    // Mapping to track if an address has claimed a specific milestone reward
    mapping(address => mapping(uint256 => bool)) public milestoneClaimed;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event MilestoneRewardClaimed(address indexed user, uint256 milestoneIndex, uint256 rewardAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender; // Set the owner as the deployer of the contract
        totalSupply = _initialSupply * (10**decimals); // Set initial total supply with decimals
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner's balance

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Function to add a new follower milestone and reward.
     * @param _followers Number of followers required for the milestone.
     * @param _rewardAmount Number of tokens rewarded for reaching the milestone.
     */
    function addMilestone(uint256 _followers, uint256 _rewardAmount) external onlyOwner {
        milestones.push(Milestone(_followers, _rewardAmount));
    }

    /**
     * @dev Function to claim rewards based on a milestone.
     * @param _milestoneIndex Index of the milestone in the milestones array.
     * @param _currentFollowers Current number of followers of the user.
     */
    function claimReward(uint256 _milestoneIndex, uint256 _currentFollowers) external {
        require(_milestoneIndex < milestones.length, "Invalid milestone index");
        Milestone memory milestone = milestones[_milestoneIndex];

        require(_currentFollowers >= milestone.followers, "Followers count does not meet the milestone requirement");
        require(!milestoneClaimed[msg.sender][_milestoneIndex], "Reward already claimed for this milestone");

        require(balanceOf[owner] >= milestone.rewardAmount, "Insufficient tokens in the contract for reward");

        // Mark the milestone reward as claimed
        milestoneClaimed[msg.sender][_milestoneIndex] = true;

        // Transfer reward tokens to the user
        balanceOf[owner] -= milestone.rewardAmount;
        balanceOf[msg.sender] += milestone.rewardAmount;

        emit Transfer(owner, msg.sender, milestone.rewardAmount);
        emit MilestoneRewardClaimed(msg.sender, _milestoneIndex, milestone.rewardAmount);
    }

    /**
     * @dev Function to transfer tokens between accounts.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Function for the owner to mint new tokens.
     * @param _amount Amount of tokens to mint.
     */
    function mint(uint256 _amount) external onlyOwner {
        uint256 mintAmount = _amount * (10**decimals);
        totalSupply += mintAmount;
        balanceOf[owner] += mintAmount;

        emit Transfer(address(0), owner, mintAmount);
    }
}
```
