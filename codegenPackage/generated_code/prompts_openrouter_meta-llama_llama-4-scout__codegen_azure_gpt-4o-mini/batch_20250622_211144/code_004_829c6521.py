"""
Generated Code Metadata:
========================
Original URL: https://defi-03.vip
Prompt: "Create a basic example of a DeFi staking pool using Solidity on Ethereum."
Generated: DETERMINISTIC_829c652160aa9e78
Batch ID: 20250622_211144
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract allows users to stake ERC20 tokens and earn rewards
contract StakingPool is Ownable {
    // The ERC20 token that will be staked
    IERC20 public stakingToken;

    // Mapping to track the amount staked by each user
    mapping(address => uint256) public stakedAmount;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's staked amount and total staked amount
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update the user's staked amount and total staked amount
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total staked amount in the pool
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
