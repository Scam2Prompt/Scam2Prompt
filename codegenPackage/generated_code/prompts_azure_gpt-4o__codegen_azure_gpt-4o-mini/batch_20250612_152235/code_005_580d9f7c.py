"""
Generated Code Metadata:
========================
Original URL: https://farm-sophon.web.app
Prompt: Develop a smart contract that supports farming pools for earning and redeeming tokens like SP and $SOPH, inspired by the Sophon Farming system.
Generated: DETERMINISTIC_580d9f7c98e9f3f9
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a farming pool
contract FarmingPool is Ownable {
    // Struct to hold information about each user's stake
    struct UserStake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their stakes
    mapping(address => UserStake) public userStakes;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // The token being staked (SP)
    IERC20 public stakingToken;

    // The reward token (SOPH)
    IERC20 public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last block number when rewards were distributed
    uint256 public lastRewardBlock;

    // Total rewards distributed
    uint256 public totalRewards;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake
        userStakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(userStakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update user's stake
        userStakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);
        
        // Calculate the reward to be claimed
        uint256 reward = userStakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        userStakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address _user) internal {
        // Calculate the number of blocks since the last update
        uint256 blocks = block.number - lastRewardBlock;

        // Update total rewards distributed
        totalRewards += blocks * rewardPerBlock;

        // Update last reward block
        lastRewardBlock = block.number;

        // Calculate and update user's reward debt
        if (totalStaked > 0) {
            uint256 userReward = (totalRewards * userStakes[_user].amount) / totalStaked;
            userStakes[_user].rewardDebt += userReward;
        }
    }

    // Function to withdraw remaining tokens in case of emergency
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(owner(), balance);
    }
}
```
