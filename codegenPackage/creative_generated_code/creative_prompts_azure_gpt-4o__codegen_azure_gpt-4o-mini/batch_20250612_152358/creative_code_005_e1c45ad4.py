"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-dashboards-inqubeta.pages.dev
Prompt: Develop a smart contract that replicates the staking reward rate functionality for $QUBE tokens as described in the dashboard.
Generated: DETERMINISTIC_e1c45ad4da2594b5
Batch ID: 20250612_152358
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

// Import OpenZeppelin contracts for safe math and access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking $QUBE tokens and managing rewards
contract QubeStaking is Ownable {
    // Variables to store the token and staking information
    IERC20 public qubeToken;
    uint256 public rewardRate; // Reward rate in tokens per second
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public totalRewards; // Total rewards distributed

    // Struct to represent a staker's data
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Debt of rewards for the staker
        uint256 lastStakeTime; // Last time the staker updated their stake
    }

    // Mapping to track stakers
    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the token and reward rate
    constructor(IERC20 _qubeToken, uint256 _rewardRate) {
        qubeToken = _qubeToken;
        rewardRate = _rewardRate;
    }

    // Stake tokens in the contract
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        require(qubeToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens from user to contract
        qubeToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.rewardDebt += _calculateRewards(msg.sender);
        staker.lastStakeTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens and claim rewards
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Calculate and claim rewards before unstaking
        uint256 reward = _calculateRewards(msg.sender);
        _claimReward(msg.sender, reward);

        // Update staker information
        staker.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        qubeToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Claim accrued rewards
    function claimRewards() external {
        uint256 reward = _calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        _claimReward(msg.sender, reward);
    }

    // Internal function to calculate rewards for a staker
    function _calculateRewards(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        return (block.timestamp - staker.lastStakeTime) * rewardRate * staker.amount / 1e18; // Assumes rewardRate is in tokens per 1e18 units
    }

    // Internal function to handle reward payments
    function _claimReward(address _staker, uint256 _reward) internal {
        require(_reward > 0, "No rewards to claim");

        // Transfer rewards to the staker
        qubeToken.transfer(_staker, _reward);
        totalRewards += _reward;

        // Update staker information
        Staker storage staker = stakers[_staker];
        staker.rewardDebt += _reward;
        staker.lastStakeTime = block.timestamp;

        emit RewardClaimed(_staker, _reward);
    }

    // Owner-only function to update the reward rate
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
