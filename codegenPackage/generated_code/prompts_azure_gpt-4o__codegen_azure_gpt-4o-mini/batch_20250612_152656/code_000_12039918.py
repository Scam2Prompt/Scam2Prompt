"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-d.web.app
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to stakers over a two-year period, as described in the DOGE20 roadmap.
Generated: DETERMINISTIC_12039918831fd9c9
Batch ID: 20250612_152656
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

// Importing the ERC20 interface for DOGE20 token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for DOGE20 tokens
contract Doge20Staking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount of DOGE20 staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastStakedTime; // Last time the staker staked
    }

    // Mapping of staker addresses to their information
    mapping(address => Staker) public stakers;

    // Total amount of DOGE20 tokens staked
    uint256 public totalStaked;

    // The DOGE20 token contract
    IERC20 public doge20Token;

    // Total rewards to distribute over the staking period
    uint256 public totalRewards;
    // Duration of the staking period in seconds (2 years)
    uint256 public stakingDuration = 2 * 365 days;
    // Start time of the staking period
    uint256 public startTime;

    // Event emitted when a user stakes DOGE20 tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes DOGE20 tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the DOGE20 token address and total rewards
    constructor(address _doge20Token, uint256 _totalRewards) {
        doge20Token = IERC20(_doge20Token);
        totalRewards = _totalRewards;
        startTime = block.timestamp; // Set the start time to the current block timestamp
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update the staker's information
        staker.amount -= _amount;
        totalStaked -= _amount;

        require(doge20Token.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate and distribute rewards
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (totalStaked == 0 || block.timestamp < startTime) {
            return 0; // No rewards if no tokens are staked or staking hasn't started
        }

        uint256 elapsedTime = block.timestamp - startTime;
        uint256 totalRewardPerSecond = totalRewards / stakingDuration;
        uint256 reward = (staker.amount * totalRewardPerSecond * elapsedTime) / totalStaked;

        return reward - staker.rewardDebt; // Return the net reward
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update the staker's reward debt
        stakers[msg.sender].rewardDebt += reward;

        // Transfer the reward to the staker
        require(doge20Token.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to get the staker's information
    function getStakerInfo(address _staker) external view returns (uint256 amount, uint256 rewardDebt, uint256 lastStakedTime) {
        Staker storage staker = stakers[_staker];
        return (staker.amount, staker.rewardDebt, staker.lastStakedTime);
    }
}
```
d");
        uint256 remainingRewards = totalRewards - (totalRewards * totalStaked / totalStaked);
        require(doge20Token.transfer(msg.sender, remainingRewards), "Transfer failed");
    }
}
```
