"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicatclaim.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token similar to $KAI, including staking functionality that rewards users based on the amount of tokens staked and duration of staking.
Generated: DETERMINISTIC_590fac696adfd5be
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the ERC20 token with staking functionality
contract KaiToken is ERC20, ReentrancyGuard, Ownable {
    // Struct to hold staking information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping of user addresses to their staking details
    mapping(address => Staker) private stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the token and reward rate
    constructor(uint256 initialSupply, uint256 _rewardRate) ERC20("KAI Token", "KAI") {
        _mint(msg.sender, initialSupply * (10 ** uint256(decimals())));
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update staker details
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.startTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards based on staked amount and duration
    function calculateReward(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        if (staker.amount == 0) return 0;

        uint256 duration = block.timestamp - staker.startTime;
        return (staker.amount * rewardRate * duration) / 1e18; // Adjusting for precision
    }

    // Function to unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        uint256 amountToUnstake = staker.amount;

        // Reset the staker details
        staker.amount = 0;
        totalStaked -= amountToUnstake;

        // Transfer staked tokens and rewards back to the user
        _transfer(address(this), msg.sender, amountToUnstake);
        if (reward > 0) {
            _mint(msg.sender, reward); // Mint reward tokens
        }

        emit Unstaked(msg.sender, amountToUnstake, reward);
    }

    // Function to allow the owner to set a new reward rate
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to check staked tokens of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakers[user].amount;
    }
}
```
