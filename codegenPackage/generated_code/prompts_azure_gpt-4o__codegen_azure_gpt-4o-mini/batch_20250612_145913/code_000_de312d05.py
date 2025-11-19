"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-en.pages.dev
Prompt: Write a smart contract in Solidity for staking $GFOX tokens, ensuring a 2% contribution to the staking rewards pool for every transaction, as described in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_de312d0506098c6a
Batch ID: 20250612_145913
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

// Importing the ERC20 interface for interacting with the $GFOX token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $GFOX tokens
contract GFOXStaking is Ownable {
    // State variables
    IERC20 public gfoxToken; // The $GFOX token contract
    uint256 public totalStaked; // Total amount of $GFOX tokens staked
    uint256 public rewardPool; // Total rewards pool
    uint256 public rewardRate; // Reward rate for stakers
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastStakedTime; // Last time user staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 amount);

    // Constructor to initialize the contract with the $GFOX token address
    constructor(address _gfoxToken, uint256 _rewardRate) {
        gfoxToken = IERC20(_gfoxToken);
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake $GFOX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gfoxToken.balanceOf(msg.sender) >= amount, "Insufficient $GFOX balance");

        // Transfer $GFOX tokens from the user to the contract
        gfoxToken.transferFrom(msg.sender, address(this), amount);
        
        // Calculate and update the reward pool
        uint256 contribution = (amount * 2) / 100; // 2% contribution
        rewardPool += contribution;

        // Update staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $GFOX tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer $GFOX tokens back to the user
        gfoxToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards to stakers
    function distributeRewards() external onlyOwner {
        require(rewardPool > 0, "No rewards to distribute");

        // Distribute rewards proportionally to stakers
        for (uint256 i = 0; i < totalStaked; i++) {
            // Logic to distribute rewards based on staked amounts
            // This is a placeholder for actual distribution logic
        }

        emit RewardsDistributed(rewardPool);
        rewardPool = 0; // Reset the reward pool after distribution
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to get the current reward pool
    function getRewardPool() external view returns (uint256) {
        return rewardPool;
    }
}
```
