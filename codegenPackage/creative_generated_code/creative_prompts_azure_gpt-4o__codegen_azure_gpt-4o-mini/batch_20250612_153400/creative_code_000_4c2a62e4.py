"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://param-35r.pages.dev
Prompt: Write a smart contract in Solidity for a staking mechanism that aligns with the tokenomics described in the Param Network platform.
Generated: DETERMINISTIC_4c2a62e49a03d413
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

// Importing OpenZeppelin's ERC20 token standard and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for the Param Network platform
contract ParamStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    // Mapping from user address to their staking information
    mapping(address => Staker) public stakers;

    // Token that can be staked
    IERC20 public stakingToken;

    // Reward tokens distributed per block
    uint256 public rewardPerBlock;

    // Total staked amount
    uint256 public totalStaked;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer the staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.lastStakedTime = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update the staker's information
        staker.amount -= _amount;
        totalStaked -= _amount;

        // Transfer the staked tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards based on staked amount
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);

        require(reward > 0, "No rewards to claim");

        // Update staker's reward debt
        staker.rewardDebt += reward;
        totalRewards += reward;

        // Transfer the reward tokens to the user
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 blocksStaked = (block.timestamp - staker.lastStakedTime) / 15; // assuming a block time of 15 seconds
        return (blocksStaked * rewardPerBlock * staker.amount) / totalStaked;
    }

    // Function to update reward rate (only owner can call)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardPerBlock = _newRate;
    }
}
```
