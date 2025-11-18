"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visit-ethena.pages.dev
Prompt: Develop a smart contract for managing repo financing to unlock composable leverage and post-leverage returns on USDe Internet Bonds.
Generated: DETERMINISTIC_6e003ae9490c822c
Batch ID: 20250612_152410
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

/// @title Repo Financing Smart Contract
/// @notice This contract manages repo financing, allowing composable leverage 
///         and post-leverage returns on USDe Internet Bonds.
contract RepoFinancing {
    // State variables
    address public owner;
    mapping(address => uint256) public userBalances; // User balances for repo financing
    mapping(address => uint256) public leverageAmounts; // User leverage amounts
    uint256 public totalLocked; // Total funds locked in repo

    // Events
    event FundsDeposited(address indexed user, uint256 amount);
    event FundsWithdrawn(address indexed user, uint256 amount);
    event LeverageActivated(address indexed user, uint256 leverageAmount);
    event LeverageDeactivated(address indexed user, uint256 leverageAmount);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasSufficientBalance(uint256 amount) {
        require(userBalances[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /// @notice Deposit funds into the repo financing system
    /// @dev Emits FundsDeposited event
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        
        userBalances[msg.sender] += msg.value;
        totalLocked += msg.value;

        emit FundsDeposited(msg.sender, msg.value);
    }

    /// @notice Withdraw funds from the repo financing system
    /// @param amount The amount to withdraw
    /// @dev Emits FundsWithdrawn event
    function withdrawFunds(uint256 amount) external hasSufficientBalance(amount) {
        userBalances[msg.sender] -= amount;
        totalLocked -= amount;
        
        payable(msg.sender).transfer(amount);

        emit FundsWithdrawn(msg.sender, amount);
    }

    /// @notice Activate leverage for the user
    /// @param leverageAmount The amount of leverage to activate
    /// @dev Emits LeverageActivated event
    function activateLeverage(uint256 leverageAmount) external hasSufficientBalance(leverageAmount) {
        leverageAmounts[msg.sender] += leverageAmount;
        userBalances[msg.sender] -= leverageAmount;
        totalLocked += leverageAmount;

        emit LeverageActivated(msg.sender, leverageAmount);
    }

    /// @notice Deactivate leverage for the user
    /// @param leverageAmount The amount of leverage to deactivate
    /// @dev Emits LeverageDeactivated event
    function deactivateLeverage(uint256 leverageAmount) external {
        require(leverageAmounts[msg.sender] >= leverageAmount, "Insufficient leverage amount");
        
        leverageAmounts[msg.sender] -= leverageAmount;
        userBalances[msg.sender] += leverageAmount;
        totalLocked -= leverageAmount;

        emit LeverageDeactivated(msg.sender, leverageAmount);
    }

    /// @notice Get the user's balance
    /// @return The balance of the calling user
    function getBalance() external view returns (uint256) {
        return userBalances[msg.sender];
    }

    /// @notice Get the user's leverage amount
    /// @return The leverage amount of the calling user
    function getLeverageAmount() external view returns (uint256) {
        return leverageAmounts[msg.sender];
    }

    /// @notice Transfer ownership of the contract
    /// @param newOwner The address of the new owner
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }

    /// @notice Fallback function to receive ETH
    receive() external payable {
        depositFunds(); // Automatically deposit incoming funds
    }
}
```
