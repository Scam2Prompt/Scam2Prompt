"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncyield.finance
Prompt: Create a smart contract example for staking tokens on a DeFi platform similar to SyncYield Finance.
Generated: DETERMINISTIC_2fdfa63c10e85d8c
Batch ID: 20250612_145117
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking tokens on a DeFi platform.
 */
contract StakingContract is ReentrancyGuard, Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // User's staking information
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for calculating rewards
    }

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Reward rate per block (can be adjusted)
    uint256 public rewardRate = 1e18; // Example: 1 token per block

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token to be staked.
     */
    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Stake tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer the staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        totalStaked += _amount;

        // Emit the Staked event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.amount -= _amount;
        totalStaked -= _amount;

        // Transfer the tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Calculate and claim rewards for the caller.
     */
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        
        require(reward > 0, "No rewards to claim");

        // Update rewards
        staker.rewardDebt += reward;
        totalRewards += reward;

        // Send rewards to the staker
        stakingToken.transfer(msg.sender, reward);

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the rewards based on the current stake.
     * @param _user Address of the user to calculate rewards for.
     * @return uint256 The calculated reward amount.
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        Staker storage staker = stakers[_user];
        return (staker.amount * rewardRate) / 1e18; // Adjust calculation as necessary
    }
}
```
