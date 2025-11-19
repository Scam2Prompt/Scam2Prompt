"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs.vercel.app
Prompt: Write a Solidity smart contract that utilizes Sonic's EVM compatibility for fast transaction processing.
Generated: DETERMINISTIC_c153f039b1cdfe42
Batch ID: 20250612_164046
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

// Importing required OpenZeppelin contracts for security and utility functions
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// SonicEVM is a smart contract that demonstrates fast transaction processing
contract SonicEVM is Ownable {
    // State variable to hold the token contract address
    IERC20 public token;

    // Events to log important actions
    event TokensDeposited(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Mapping to keep track of user balances
    mapping(address => uint256) private balances;

    // Constructor to initialize the token contract address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }

    // Deposit tokens into the contract
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from sender to this contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's balance
        balances[msg.sender] += amount;

        // Emit an event for the deposit
        emit TokensDeposited(msg.sender, amount);
    }

    // Withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring tokens
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit an event for the withdrawal
        emit TokensWithdrawn(msg.sender, amount);
    }

    // Function to check the balance of a user
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to set a new token contract address (only owner)
    function setTokenAddress(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }
}
```
