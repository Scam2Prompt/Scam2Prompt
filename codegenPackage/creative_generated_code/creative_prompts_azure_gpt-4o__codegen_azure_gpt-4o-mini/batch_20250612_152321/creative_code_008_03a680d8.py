"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-6s6.pages.dev
Prompt: Create a smart contract in Solidity for the $FROP token that includes features for staking, rewards distribution, and multichain compatibility.
Generated: DETERMINISTIC_03a680d8c9b56f4e
Batch ID: 20250612_152321
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FROPToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Staking structure
    struct Staker {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt
        uint256 lastStakedAt; // Last timestamp of staking
    }

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor for initializing the token
    constructor(uint256 initialSupply, uint256 _rewardRate) ERC20("FROP Token", "FROP") {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the owner
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update total staked and individual staker data
        totalStaked = totalStaked.add(amount);
        stakers[msg.sender].amount = stakers[msg.sender].amount.add(amount);
        stakers[msg.sender].lastStakedAt = block.timestamp;
        
        // Transfer tokens from staker to the contract
        _transfer(msg.sender, address(this), amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards
        uint256 reward = calculateReward(msg.sender);
        distributeRewards(msg.sender, reward);

        // Update staker data
        staker.amount = staker.amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the staker
        _transfer(address(this), msg.sender, amount);
    }

    // Function to calculate rewards for a staker
    function calculateReward(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 timeStaked = block.timestamp.sub(staker.lastStakedAt);
        uint256 reward = timeStaked.mul(rewardRate).mul(staker.amount).div(1e18);
        return reward.add(staker.rewardDebt);
    }

    // Function to distribute rewards to a staker
    function distributeRewards(address user, uint256 amount) internal {
        require(amount > 0, "No rewards to distribute");
        stakers[user].rewardDebt = stakers[user].rewardDebt.add(amount);
        _mint(user, amount); // Mint new tokens as rewards
        emit RewardsDistributed(user, amount);
    }

    // Function for owner to change rewardRate
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to view the staker's details
    function viewStaker(address user) external view returns (uint256 stakedAmount, uint256 pendingRewards) {
        Staker storage staker = stakers[user];
        return (staker.amount, calculateReward(user));
    }
}
```
