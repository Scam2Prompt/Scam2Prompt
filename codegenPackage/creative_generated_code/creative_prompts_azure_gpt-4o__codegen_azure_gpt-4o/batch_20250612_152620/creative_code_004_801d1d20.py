"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai-claim.pages.dev
Prompt: Write a Solidity smart contract snippet to distribute $SCOTTY staking rewards dynamically based on the user's share of the staking pool and the current reward rate per ETH block.
Generated: DETERMINISTIC_801d1d2060d19c0c
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
 * @title StakingRewards
 * @dev Smart contract to distribute staking rewards dynamically based on the user's share of the staking pool.
 */
contract StakingRewards {
    // Total staked amount in the pool
    uint256 public totalStaked;

    // Mapping from user address to their staked amount
    mapping(address => uint256) public userStakes;

    // Mapping from user address to their pending rewards
    mapping(address => uint256) public userRewards;

    // Reward rate in SCOTTY tokens per ETH block
    uint256 public rewardRate;

    // Last block number when rewards were calculated
    uint256 public lastRewardBlock;

    // Event to notify when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event to notify when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event to notify when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the reward rate.
     * @param _rewardRate Reward rate in SCOTTY tokens per ETH block.
     */
    constructor(uint256 _rewardRate) {
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake ETH into the pool. Rewards are updated before staking.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than 0");
        
        _updateRewards();

        userStakes[msg.sender] += msg.value;
        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw staked ETH from the pool. Rewards are updated before withdrawal.
     * @param _amount Amount to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(userStakes[msg.sender] >= _amount, "Insufficient staked balance");
        
        _updateRewards();

        userStakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        payable(msg.sender).transfer(_amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards in SCOTTY tokens. Rewards are updated before claiming.
     */
    function claimRewards() external {
        _updateRewards();

        uint256 rewards = userRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        userRewards[msg.sender] = 0;

        // Transfer the SCOTTY tokens (assumed to be already implemented in this contract)
        _transferRewards(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for all users.
     */
    function _updateRewards() internal {
        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        if (blocksSinceLastReward > 0 && totalStaked > 0) {
            uint256 totalRewards = blocksSinceLastReward * rewardRate;

            for (address stakeholder in _getStakeholders()) {
                uint256 userShare = userStakes[stakeholder];
                uint256 userReward = (userShare * totalRewards) / totalStaked;
                userRewards[stakeholder] += userReward;
            }
        }
        lastRewardBlock = block.number;
    }

    /**
     * @dev Internal function to transfer SCOTTY tokens to users.
     * @param _user Address of the user to transfer rewards to.
     * @param _amount Amount of SCOTTY tokens to transfer.
     */
    function _transferRewards(address _user, uint256 _amount) internal {
        // Implement token transfer logic (e.g., ERC20 transfer)
    }

    /**
     * @dev Helper function to retrieve all stakeholders (not implemented for brevity).
     */
    function _getStakeholders() internal view returns (address[] memory) {
        // This function should return the list of all users who have staked.
        // Since Solidity doesn't allow iteration over mappings, you need to implement
        // a mechanism to track stakeholders when they stake or withdraw.
    }
}
```
