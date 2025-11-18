"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://threshold-network.firebaseapp.com
Prompt: Write a smart contract function to stake T tokens on the Threshold Network and query the staked balance.
Generated: DETERMINISTIC_6b94108e8600648f
Batch ID: 20250612_155102
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

// Importing the ERC20 interface for interacting with the token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Defining the Threshold Network Staking Contract
contract ThresholdNetworkStaking {
    // Declare variables
    IERC20 public token;  // Token to be staked
    mapping(address => uint256) private stakedBalances;  // Mapping to track staked balances of users

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to check the amount is greater than zero
    modifier validStake(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Constructor to initialize the contract with the token address
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(tokenAddress);
    }

    // Function to stake tokens
    function stake(uint256 amount) external validStake(amount) {
        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance
        stakedBalances[msg.sender] += amount;

        // Emit Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external validStake(amount) {
        // require that the user has enough staked balance
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the staked balance
        stakedBalances[msg.sender] -= amount;

        // Transfer tokens back to user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to query the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}
```
