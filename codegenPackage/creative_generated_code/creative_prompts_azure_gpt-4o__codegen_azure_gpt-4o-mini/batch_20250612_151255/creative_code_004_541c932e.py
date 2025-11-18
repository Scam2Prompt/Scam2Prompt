"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethoq.xyz
Prompt: Write a smart contract in Solidity for a basic DeFi application that supports ETH staking and rewards distribution.
Generated: DETERMINISTIC_541c932e49dfa5c9
Batch ID: 20250612_151255
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

// Importing OpenZeppelin's ERC20 interface for reward token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// A simple DeFi staking contract
contract EthStaking {
    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    // Struct to hold user staking data
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimed;
    }

    // Mapping of user addresses to their staking data
    mapping(address => Staker) public stakers;

    // Total amount of ETH staked in the contract
    uint256 public totalStaked;

    // Reward token address
    IERC20 public rewardToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Constructor to initialize the contract with the reward token and rate
    constructor(IERC20 _rewardToken, uint256 _rewardRate) {
        require(address(_rewardToken) != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake ETH
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount");

        // Update the staker's data
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += msg.value;
        staker.lastClaimed = block.timestamp;

        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    // Function to unstake ETH
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Distribute rewards before unstaking
        distributeRewards();

        // Update staker data and total staked
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer ETH back to the user
        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards to the user
    function distributeRewards() public {
        Staker storage staker = stakers[msg.sender];

        // Calculate the time passed since last claim
        uint256 timePassed = block.timestamp - staker.lastClaimed;
        uint256 reward = timePassed * rewardRate;

        require(reward > 0, "No rewards available");

        // Update the last claimed timestamp
        staker.lastClaimed = block.timestamp;

        // Transfer the reward tokens to the user
        require(rewardToken.balanceOf(address(this)) >= reward, "Insufficient reward balance in contract");
        rewardToken.transfer(msg.sender, reward);

        emit RewardsDistributed(msg.sender, reward);
    }

    // Function to check the staker's balance
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
