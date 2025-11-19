"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: How can I implement a staking mechanism for a gaming token similar to PARAM in the Param Network?
Generated: DETERMINISTIC_86ba8b33e51ae3d7
Batch ID: 20250612_160940
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token and ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a gaming token
contract Staking is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // Struct to represent a staker
    struct Staker {
        uint256 amount; // Amount staked
        uint256 reward; // Accumulated rewards
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping from user address to their staking details
    mapping(address => Staker) public stakers;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward rate per second (in tokens)
    uint256 public rewardRate = 1e18; // Example: 1 token per second

    // Events for logging staking and withdrawing
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the token to be staked
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update staker's reward before changing their balance
        _updateReward(msg.sender);
        
        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update the staker's details
        stakers[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens and claim rewards
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update staker's reward before changing their balance
        _updateReward(msg.sender);

        // Update the staker's details
        stakers[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimReward() external {
        _updateReward(msg.sender);
        uint256 reward = stakers[msg.sender].reward;

        require(reward > 0, "No reward available");
        stakers[msg.sender].reward = 0; // Reset reward to prevent re-entrancy

        // Transfer reward tokens to the staker
        stakingToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to calculate and update the reward for the specified staker
    function _updateReward(address _staker) internal {
        Staker storage staker = stakers[_staker];

        // Calculate reward based on the time since last stake and the amount staked
        if (staker.lastStakedTime > 0) {
            uint256 timeStaked = block.timestamp - staker.lastStakedTime;
            staker.reward += (staker.amount * rewardRate * timeStaked) / 1e18; // Assuming rewardRate is scaled
        }
        
        // Update the last staked time
        staker.lastStakedTime = block.timestamp;
    }

    // Function to set a new reward rate (only owner can call this)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to retrieve the staked amount of a user
    function stakedAmount(address _staker) external view returns (uint256) {
        return stakers[_staker].amount;
    }
}
```
