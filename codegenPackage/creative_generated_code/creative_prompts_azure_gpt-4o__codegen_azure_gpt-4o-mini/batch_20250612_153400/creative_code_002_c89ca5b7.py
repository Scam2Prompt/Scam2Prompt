"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge-live.pages.dev
Prompt: Create a smart contract in Solidity that implements a staking mechanism similar to DOGE20, with dynamic rewards calculated per block and distributed over a fixed period.
Generated: DETERMINISTIC_c89ca5b7b52cb300
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingPool is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Reward token to be distributed
    IERC20 public rewardToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for claiming
        uint256 lastStakedBlock; // Last block when user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block per staker
    uint256 public rewardPerBlock;

    // Start block for rewards
    uint256 public startBlock;

    // End block for rewards
    uint256 public endBlock;

    // Events for staking, unstaking, and claiming rewards
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerBlock, uint256 _startBlock, uint256 _endBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    // Modifier to check if staking is active
    modifier stakingActive() {
        require(block.number >= startBlock, "Staking not started");
        require(block.number <= endBlock, "Staking ended");
        _;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external stakingActive {
        require(_amount > 0, "Cannot stake 0");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staker info
        stakers[msg.sender].amount += _amount;
        totalStaked += _amount;
        stakers[msg.sender].lastStakedBlock = block.number;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external stakingActive {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        staker.amount -= _amount;
        totalStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
    }

    // Internal function to update rewards for a staker
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        uint256 blocksStaked = block.number - staker.lastStakedBlock;
        
        if (blocksStaked > 0) {
            uint256 reward = (staker.amount * rewardPerBlock * blocksStaked) / totalStaked;
            rewardToken.transfer(_staker, reward);
            staker.rewardDebt += reward;
            staker.lastStakedBlock = block.number;

            emit RewardClaimed(_staker, reward);
        }
    }

    // Function to get the pending rewards for a user
    function pendingRewards(address _staker) external view returns (uint256) {
        Staker memory staker = stakers[_staker];
        uint256 blocksStaked = block.number - staker.lastStakedBlock;
        return (staker.amount * rewardPerBlock * blocksStaked) / totalStaked;
    }
}
```
