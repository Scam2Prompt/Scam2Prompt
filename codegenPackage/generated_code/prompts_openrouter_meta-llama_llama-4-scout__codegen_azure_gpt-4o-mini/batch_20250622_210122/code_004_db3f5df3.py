"""
Generated Code Metadata:
========================
Original URL: https://ketoken.com
Prompt: "Create a simple blockchain-based loyalty program using Solidity and Ethereum, inspired by KeToken's use case for customer retention and employee incentives."
Generated: DETERMINISTIC_db3f5df31b754f2c
Batch ID: 20250622_210122
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

/// @title Loyalty Program Smart Contract
/// @author Your Name
/// @notice This contract implements a simple blockchain-based loyalty program
/// @dev The contract allows users to earn and redeem loyalty tokens

contract LoyaltyProgram {
    // State variables
    string public name; // Name of the loyalty program
    address public owner; // Owner of the contract
    uint256 public totalSupply; // Total supply of loyalty tokens

    // Mapping from user addresses to their loyalty token balances
    mapping(address => uint256) private balances;

    // Events
    event TokensEarned(address indexed user, uint256 amount);
    event TokensRedeemed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /// @notice Constructor to initialize the loyalty program
    /// @param _name The name of the loyalty program
    constructor(string memory _name) {
        name = _name;
        owner = msg.sender; // Set the contract deployer as the owner
        totalSupply = 0; // Initialize total supply to zero
    }

    /// @notice Function to earn loyalty tokens
    /// @param _amount The amount of tokens to earn
    /// @dev Only the owner can call this function
    function earnTokens(address _user, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        
        balances[_user] += _amount; // Increase user's balance
        totalSupply += _amount; // Increase total supply

        emit TokensEarned(_user, _amount); // Emit event
    }

    /// @notice Function to redeem loyalty tokens
    /// @param _amount The amount of tokens to redeem
    /// @dev Users can only redeem tokens they have
    function redeemTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        balances[msg.sender] -= _amount; // Decrease user's balance
        totalSupply -= _amount; // Decrease total supply

        emit TokensRedeemed(msg.sender, _amount); // Emit event
    }

    /// @notice Function to check the loyalty token balance of a user
    /// @param _user The address of the user
    /// @return The loyalty token balance of the user
    function checkBalance(address _user) external view returns (uint256) {
        return balances[_user]; // Return user's balance
    }

    /// @notice Function to get the total supply of loyalty tokens
    /// @return The total supply of loyalty tokens
    function getTotalSupply() external view returns (uint256) {
        return totalSupply; // Return total supply
    }
}
```
