"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asteerdex.com
Prompt: Develop a smart contract in Solidity that integrates with Aster to automate staking and reward collection for supported assets.
Generated: DETERMINISTIC_9e886eaf53dfa5fa
Batch ID: 20250612_154021
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

// Importing the ERC20 interface for interacting with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// This contract automates staking and reward collection for supported assets
contract AsterStaking {
    // State variables
    IERC20 public stakingToken; // The token that will be staked
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate for staking (tokens per block)
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user
    mapping(address => uint256) public lastUpdate; // Last update time for each user

    // Events to log staking and reward actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any action (stake/withdraw)
    modifier updateReward(address _user) {
        rewards[_user] += earned(_user);
        lastUpdate[_user] = block.number; // Update the last block number
        _;
    }

    // Function to calculate earned rewards for a user
    function earned(address _user) public view returns (uint256) {
        return stakedAmount[_user] * rewardRate * (block.number - lastUpdate[_user]) / 1e18;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Amount must be greater than 0");
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        totalStaked += _amount;
        stakedAmount[msg.sender] += _amount;
        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= _amount, "Insufficient staked amount");
        
        stakedAmount[msg.sender] -= _amount;
        totalStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function getReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");
        
        rewards[msg.sender] = 0; // Reset rewards after claiming
        stakingToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to get the total staked amount for an address
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakedAmount[_user];
    }

    // Function to get the total rewards for an address
    function getRewards(address _user) external view returns (uint256) {
        return rewards[_user] + earned(_user);
    }
}
```
