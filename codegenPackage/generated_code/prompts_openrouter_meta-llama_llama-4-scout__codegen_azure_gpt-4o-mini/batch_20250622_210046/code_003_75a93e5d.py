"""
Generated Code Metadata:
========================
Original URL: https://flockerz-claim.web.app
Prompt: Design a simple smart contract in Solidity that allows users to stake $FLOCK tokens and earn rewards based on their voting participation in the Flockerz DAO.
Generated: DETERMINISTIC_75a93e5d2d956e4f
Batch ID: 20250622_210046
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

// Importing the ERC20 interface for the $FLOCK token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking $FLOCK tokens and earning rewards based on voting participation
contract FlockStaking is Ownable {
    // State variables
    IERC20 public flockToken; // The $FLOCK token contract
    uint256 public rewardRate; // Reward rate per vote
    mapping(address => uint256) public stakedAmount; // Amount of $FLOCK staked by each user
    mapping(address => uint256) public votingParticipation; // Voting participation count for each user
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $FLOCK token address and reward rate
    constructor(IERC20 _flockToken, uint256 _rewardRate) {
        flockToken = _flockToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $FLOCK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(flockToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedAmount[msg.sender] += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake $FLOCK tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        stakedAmount[msg.sender] -= amount;
        require(flockToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to participate in voting
    function participateInVoting() external {
        require(stakedAmount[msg.sender] > 0, "Must stake tokens to participate");
        
        votingParticipation[msg.sender] += 1;
    }

    // Function to claim rewards based on voting participation
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] += reward;
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        return votingParticipation[user] * rewardRate;
    }

    // Function to withdraw accumulated rewards (if rewards are in a separate token)
    function withdrawRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        rewards[msg.sender] = 0;
        // Assuming rewards are paid in $FLOCK tokens
        require(flockToken.transfer(msg.sender, reward), "Transfer failed");
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
