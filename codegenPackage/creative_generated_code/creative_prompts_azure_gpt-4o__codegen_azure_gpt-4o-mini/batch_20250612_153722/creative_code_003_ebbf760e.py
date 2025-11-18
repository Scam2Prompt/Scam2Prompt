"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-puffer.com
Prompt: Write a smart contract that enables automated and optimized yield strategies for users participating in Puffer Finance's staking ecosystem.
Generated: DETERMINISTIC_ebbf760e9786abd0
Batch ID: 20250612_153722
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

interface IStakingToken {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

interface IYieldStrategy {
    function executeStrategy(address user, uint256 amount) external returns (uint256);
}

contract PufferFinanceYield {
    // State variables
    IStakingToken public stakingToken;            // The token being staked by users
    IYieldStrategy public yieldStrategy;          // The yield strategy to be executed

    // Event emitted when yield is harvested
    event YieldHarvested(address indexed user, uint256 amount);

    // Mapping to keep track of user balances
    mapping(address => uint256) private userBalances;

    // Constructor to initialize the staking token and yield strategy
    constructor(IStakingToken _stakingToken, IYieldStrategy _yieldStrategy) {
        stakingToken = _stakingToken;
        yieldStrategy = _yieldStrategy;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        stakingToken.stake(amount);
        
        // Update the user's balance
        userBalances[msg.sender] += amount;
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");
        
        // Update the user's balance before the withdrawal
        userBalances[msg.sender] -= amount;

        // Withdraw tokens from the staking contract
        stakingToken.withdraw(amount);
    }

    // Function to execute yield strategies
    function harvestYield() external {
        uint256 userBalance = userBalances[msg.sender];
        require(userBalance > 0, "No staked tokens to harvest yield from");

        // Execute the yield strategy for the user
        uint256 yieldAmount = yieldStrategy.executeStrategy(msg.sender, userBalance);
        
        // Emit an event for the yield harvested
        emit YieldHarvested(msg.sender, yieldAmount);
    }

    // View function to check user balance
    function getUserBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }

    // Function to change the yield strategy (only owner can change)
    function setYieldStrategy(IYieldStrategy _yieldStrategy) external onlyOwner {
        yieldStrategy = _yieldStrategy;
    }

    // Modifier to restrict access to owner functions
    modifier onlyOwner() {
        // Implement ownership check
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }
}
```
