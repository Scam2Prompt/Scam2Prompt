"""
Generated Code Metadata:
========================
Original URL: https://btfd-bonus.ink
Prompt: Create a Solidity function to calculate and distribute staking rewards for an ERC20 token, ensuring compliance with the vesting schedule (e.g., 16 weeks for staking rewards).
Generated: DETERMINISTIC_a55981d9713e4522
Batch ID: 20250612_154029
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingRewards contract to manage staking and reward distribution
contract StakingRewards is Ownable {
    // ERC20 token to be used for staking
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastClaimed; // Last time rewards were claimed
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (adjust as necessary)
    uint256 public rewardRate = 1e18; // Example: 1 token per second

    // Vesting period for rewards (in seconds)
    uint256 public vestingPeriod = 16 weeks;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        staker.rewardDebt = calculatePendingRewards(msg.sender);
        staker.lastClaimed = block.timestamp;

        totalStaked += _amount;
    }

    // Function to calculate pending rewards for a staker
    function calculatePendingRewards(address _staker) internal view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp - staker.lastClaimed;
        uint256 pendingRewards = (staker.amount * rewardRate * timeStaked) / 1e18;
        return pendingRewards + staker.rewardDebt;
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        require(pendingRewards > 0, "No rewards to claim");
        require(block.timestamp >= staker.lastClaimed + vestingPeriod, "Rewards are still vesting");

        // Reset the last claimed time and reward debt
        staker.lastClaimed = block.timestamp;
        staker.rewardDebt = 0;

        // Transfer rewards to the staker
        stakingToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update staker information
        staker.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, _amount);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
