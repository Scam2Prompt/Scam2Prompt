"""
Generated Code Metadata:
========================
Original URL: https://leverfi.pages.dev
Prompt: Develop a smart contract to participate in the OmniZK testnet upgrade and utilize its features for Bitcoin DeFi applications.
Generated: DETERMINISTIC_f0e9647978c3275f
Batch ID: 20250612_150226
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for participating in the OmniZK testnet upgrade
contract OmniZKDeFi is Ownable {
    // Event to log deposits
    event Deposited(address indexed user, uint256 amount);
    // Event to log withdrawals
    event Withdrawn(address indexed user, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // ERC20 token interface for interacting with the token
    IERC20 public token;

    // Constructor to initialize the contract with the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to deposit tokens into the contract
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from user to this contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update user balance
        balances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance before transferring to prevent re-entrancy
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of a user
    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to withdraw all tokens in case of emergency (only owner)
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        token.transfer(owner(), contractBalance);
    }
}
```
