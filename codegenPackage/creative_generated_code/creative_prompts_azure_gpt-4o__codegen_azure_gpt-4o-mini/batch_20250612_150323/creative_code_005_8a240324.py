"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Provide an example of a Solidity contract for a prize wallet system, similar to the MotorBoat Prize Wallet described on the CryptoTitties webpage.
Generated: DETERMINISTIC_8a240324b21bd7a6
Batch ID: 20250612_150323
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

/// @title Prize Wallet System
/// @notice This contract allows users to deposit funds, and a designated winner can withdraw the total balance as a prize.
/// @dev This contract is designed to be simple and secure for managing prize pools.

contract PrizeWallet {
    address public owner;               // Address of the contract owner
    address public winner;              // Address of the current winner
    uint256 public totalBalance;        // Total balance in the prize wallet
    mapping(address => uint256) public balances; // Mapping to store users' deposit balances

    // Event emitted when funds are deposited
    event Deposited(address indexed user, uint256 amount);
    
    // Event emitted when a winner is set
    event WinnerSet(address indexed winner);
    
    // Event emitted when the prize is withdrawn
    event PrizeWithdrawn(address indexed winner, uint256 amount);

    // Modifier to restrict certain functions to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Modifier to restrict functions to the current winner only
    modifier onlyWinner() {
        require(msg.sender == winner, "Not the current winner");
        _;
    }

    /// @notice Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Function to deposit funds into the prize wallet
    /// @dev Requires the sent amount to be greater than zero
    function deposit() external payable {
        require(msg.value > 0, "Deposit must be greater than zero");

        balances[msg.sender] += msg.value; // Update the user's balance
        totalBalance += msg.value;          // Update the total balance
        
        emit Deposited(msg.sender, msg.value); // Emit the deposit event
    }

    /// @notice Function to set a winner for the prize wallet
    /// @param _winner The address of the winner
    /// @dev Only the owner can set a winner
    function setWinner(address _winner) external onlyOwner {
        require(_winner != address(0), "Invalid address for winner");
        
        winner = _winner; // Set the winner address
        
        emit WinnerSet(_winner); // Emit the winner set event
    }

    /// @notice Function for the winner to withdraw the total balance
    /// @dev Only the current winner can withdraw funds
    function withdrawPrize() external onlyWinner {
        uint256 amount = totalBalance; // Store the total balance to withdraw
        totalBalance = 0;               // Reset the total balance

        // Transfer the funds to the winner's address
        (bool success, ) = winner.call{value: amount}("");
        require(success, "Transfer failed"); // Ensure the transfer was successful

        emit PrizeWithdrawn(winner, amount); // Emit the prize withdrawn event
    }

    /// @notice Function to check the balance of a specific user
    /// @param user The address of the user to check
    /// @return The balance of the user
    function checkBalance(address user) external view returns (uint256) {
        return balances[user]; // Return the user's balance
    }
}
```
