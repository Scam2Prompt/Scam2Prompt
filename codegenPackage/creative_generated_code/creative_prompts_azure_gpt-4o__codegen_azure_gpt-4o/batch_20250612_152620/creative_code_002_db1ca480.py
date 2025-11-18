"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a smart contract in Solidity that implements staking functionality similar to the $POODL token staking system, including dynamic reward calculation per Ethereum block.
Generated: DETERMINISTIC_db1ca480e2ab8293
Batch ID: 20250612_152620
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
 * @dev Implements a staking system with dynamic rewards calculation per Ethereum block.
 */
contract StakingContract {
    // State variables
    address public owner;
    uint256 public rewardRatePerBlock; // Reward rate per block (tokens per block)
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastClaimedBlock; // Block number when rewards were last claimed
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    mapping(address => uint256) public pendingRewards; // Rewards pending claim per user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the contract owner");
        _;
    }

    constructor(uint256 _rewardRatePerBlock) {
        owner = msg.sender;
        rewardRatePerBlock = _rewardRatePerBlock;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update pending rewards before modifying stake
        _updateRewards(msg.sender);

        // Update staking data
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastClaimedBlock = block.number;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked tokens");

        // Update pending rewards before modifying stake
        _updateRewards(msg.sender);

        // Update staking data
        stakes[msg.sender].amount -= _amount;
        if (stakes[msg.sender].amount == 0) {
            stakes[msg.sender].lastClaimedBlock = 0;
        }
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = pendingRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        pendingRewards[msg.sender] = 0;

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Update the reward rate per block.
     * @param _newRewardRate New reward rate per block.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRatePerBlock = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeData = stakes[_user];
        if (stakeData.amount > 0 && stakeData.lastClaimedBlock > 0) {
            uint256 blocksStaked = block.number - stakeData.lastClaimedBlock;
            uint256 reward = blocksStaked * rewardRatePerBlock * stakeData.amount / totalStaked;
            pendingRewards[_user] += reward;
            stakeData.lastClaimedBlock = block.number;
        }
    }
}
```
