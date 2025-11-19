"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Provide an example of a smart contract that manages the staking and reward distribution for $SCOTTY tokens in a blockchain environment.
Generated: DETERMINISTIC_d496f44e608b3449
Batch ID: 20250612_162228
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

// Importing OpenZeppelin's ERC20 implementation for our $SCOTTY token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing staking and reward distribution
contract StakingContract is Ownable {
    // Token interface for interacting with the $SCOTTY token
    IERC20 public scottyToken;

    // Staker information
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 stakingStartTime; // Time when staking started
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of staker addresses to their staking info
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rate (tokens per second)
    uint256 public rewardRate = 1e18; // 1 SCOTTY token per second

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the SCOTTY token
    constructor(IERC20 _scottyToken) {
        scottyToken = _scottyToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(scottyToken.balanceOf(msg.sender) >= _amount, "Insufficient SCOTTY tokens");

        // Update the staker's information
        stakers[msg.sender].amountStaked += _amount;
        stakers[msg.sender].stakingStartTime = block.timestamp;
        totalStaked += _amount;

        // Transfer tokens from the staker to the contract
        scottyToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        staker.rewards += reward;

        // Transfer staked tokens back to the staker
        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0;
        totalStaked -= amountToUnstake;

        scottyToken.transfer(msg.sender, amountToUnstake);
        emit Unstaked(msg.sender, amountToUnstake);

        // Transfer rewards if any
        if (staker.rewards > 0) {
            scottyToken.transfer(msg.sender, staker.rewards);
            emit RewardClaimed(msg.sender, staker.rewards);
            staker.rewards = 0;
        }
    }

    // Function to calculate the reward for a staker
    function calculateReward(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.amountStaked == 0) {
            return 0;
        }
        uint256 duration = block.timestamp - staker.stakingStartTime;
        return (duration * staker.amountStaked * rewardRate) / 1e18;
    }

    // Function to update the reward rate (only owner can call this)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
