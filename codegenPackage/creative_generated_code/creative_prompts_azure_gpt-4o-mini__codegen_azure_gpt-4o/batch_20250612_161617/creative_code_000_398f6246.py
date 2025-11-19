"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: How can I implement a staking mechanism for the DOGE20 ERC-20 token using smart contracts on Ethereum?
Generated: DETERMINISTIC_398f6246997c2155
Batch ID: 20250612_161617
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
 * @title StakingContract
 * @dev Implements a staking mechanism for the DOGE20 ERC-20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    IERC20 public immutable stakingToken; // Reference to the DOGE20 token contract
    uint256 public rewardRate; // Reward rate per second
    
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already claimed/debt
        uint256 lastUpdated; // Last time stake was updated
    }
    
    mapping(address => Stake) public stakes; // Tracks stakes for each address
    uint256 public totalStaked; // Total amount of tokens staked
    
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake DOGE20 tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        Stake storage userStake = stakes[msg.sender];

        // Update rewards for the user before modifying stake
        _updateRewards(msg.sender);

        // Transfer tokens to the staking contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake and global total
        userStake.amount += _amount;
        totalStaked += _amount;

        // Update the lastUpdated timestamp
        userStake.lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens. Rewards must be claimed separately.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update rewards before modifying the stake
        _updateRewards(msg.sender);

        // Reduce user's stake and global total
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards for the user.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);
        
        Stake storage userStake = stakes[msg.sender];
        uint256 rewardToClaim = userStake.rewardDebt;

        require(rewardToClaim > 0, "No rewards available");

        // Reset the reward debt before transferring rewards
        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, rewardToClaim);

        emit RewardClaimed(msg.sender, rewardToClaim);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 accruedRewards = ((block.timestamp - userStake.lastUpdated) * userStake.amount * rewardRate) / 1e18;
            userStake.rewardDebt += accruedRewards;
        }
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Get pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 accruedRewards = ((block.timestamp - userStake.lastUpdated) * userStake.amount * rewardRate) / 1e18;
        return userStake.rewardDebt + accruedRewards;
    }
}
```
