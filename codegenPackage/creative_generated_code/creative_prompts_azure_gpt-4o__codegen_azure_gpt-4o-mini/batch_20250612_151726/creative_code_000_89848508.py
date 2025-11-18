"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon-bag-claim.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token similar to MoonBag ($MBAG), including features like staking with an APY of 88%, referral incentives, and token vesting for 3 months after listing.
Generated: DETERMINISTIC_89848508af3bd3bb
Batch ID: 20250612_151726
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MoonBagToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Staking structure
    struct Staker {
        uint256 amount;        // Amount staked
        uint256 reward;        // Accumulated rewards
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    uint256 public totalStaked; // Total amount staked in the contract
    uint256 public rewardRate;   // Annual Percentage Yield (APY)
    uint256 public vestingDuration; // Vesting duration in seconds
    uint256 public listingTime;   // Time of token listing

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set up the token
    constructor() ERC20("MoonBag", "$MBAG") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply
        rewardRate = 88; // Set APY to 88%
        vestingDuration = 90 days; // Set vesting duration to 3 months
        listingTime = block.timestamp; // Set listing time to current block timestamp
    }

    // Stake tokens to earn rewards
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount = staker.amount.add(amount);
        staker.lastStakedTime = block.timestamp;
        totalStaked = totalStaked.add(amount);

        // Transfer tokens from user to the contract
        _transfer(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];

        require(staker.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        staker.reward = staker.reward.add(reward);
        
        // Transfer staked amount back to the user only if the vesting period has passed
        require(block.timestamp >= listingTime + vestingDuration, "Tokens are currently vesting");

        // Transfer tokens back to the user
        uint256 amountToUnstake = staker.amount;
        staker.amount = 0;
        totalStaked = totalStaked.sub(amountToUnstake);
        _transfer(address(this), msg.sender, amountToUnstake);

        // Transfer rewards if applicable
        if (staker.reward > 0) {
            _mint(msg.sender, staker.reward);
            emit RewardPaid(msg.sender, staker.reward);
            staker.reward = 0; // Reset rewards after claiming
        }

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Calculate rewards for a staker
    function calculateReward(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        if (staker.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp.sub(staker.lastStakedTime);
        uint256 reward = staker.amount.mul(rewardRate).mul(stakingDuration).div(365 days).div(100);
        return reward;
    }

    // Function to claim rewards without unstaking
    function claimRewards() external nonReentrant {
        Staker storage staker = stakers[msg.sender];

        require(staker.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        staker.reward = staker.reward.add(reward);
        staker.lastStakedTime = block.timestamp; // Reset last staking time

        _mint(msg.sender, staker.reward);
        emit RewardPaid(msg.sender, staker.reward);
        staker.reward = 0; // Reset rewards after claiming
    }

    // Function to get the staker's details
    function getStakerDetails(address stakerAddress) external view returns (uint256 amount, uint256 reward) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amount, staker.reward);
    }
}
```
