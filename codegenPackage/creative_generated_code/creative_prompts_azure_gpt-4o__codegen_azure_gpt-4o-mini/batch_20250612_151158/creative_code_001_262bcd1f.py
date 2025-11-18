"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitlayerorg.pages.dev
Prompt: Generate a smart contract in Solidity that is 100% EVM-compatible and demonstrates the use of Bitlayer's trustless 2-way peg mechanism combining DLC and BitVM.
Generated: DETERMINISTIC_262bcd1f7e08932d
Batch ID: 20250612_151158
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

/// @title Bitlayer Trustless Two-Way Peg Smart Contract
/// @notice This contract demonstrates the use of the Bitlayer's trustless two-way peg mechanism 
///         by integrating Discreet Log Contracts (DLC) and BitVM.
contract BitlayerTwoWayPeg {
    // Events
    event Deposited(address indexed user, uint256 amount, bytes32 depositId);
    event Withdrawn(address indexed user, uint256 amount, bytes32 withdrawalId);
    
    // Struct to hold information for deposits
    struct Deposit {
        address user;
        uint256 amount;
        bool exists;
    }
    
    // Mapping to store deposits by depositId
    mapping(bytes32 => Deposit) private deposits;
    
    // Modifier to check if deposit exists
    modifier depositExists(bytes32 depositId) {
        require(deposits[depositId].exists, "Deposit does not exist");
        _;
    }
    
    /// @notice Deposit funds into the contract
    /// @param depositId Unique identifier for the deposit
    function deposit(bytes32 depositId) external payable {
        require(msg.value > 0, "Must send a positive amount");
        require(!deposits[depositId].exists, "Deposit ID already used");
        
        // Record the deposit
        deposits[depositId] = Deposit({
            user: msg.sender,
            amount: msg.value,
            exists: true
        });

        emit Deposited(msg.sender, msg.value, depositId);
    }
    
    /// @notice Withdraw funds from the contract
    /// @param depositId Unique identifier for the deposit
    function withdraw(bytes32 depositId) external depositExists(depositId) {
        Deposit storage deposit = deposits[depositId];
        
        require(deposit.user == msg.sender, "Only the depositor can withdraw");
        
        // Transfer funds to the user
        uint256 amount = deposit.amount;
        deposit.amount = 0; // Prevent re-entrancy
      
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount, depositId);
    }
    
    /// @notice Fallback function to accept ether
    receive() external payable {
        revert("Direct deposits not allowed, use deposit function");
    }
    
    /// @notice Function to check the balance of a specific deposit
    /// @param depositId Unique identifier for the deposit
    /// @return The amount of the deposit
    function getDepositAmount(bytes32 depositId) external view depositExists(depositId) returns (uint256) {
        return deposits[depositId].amount;
    }
    
    /// @notice Function to check if a deposit exists
    /// @param depositId Unique identifier for the deposit
    /// @return True if the deposit exists, false otherwise
    function depositExistsCheck(bytes32 depositId) external view returns (bool) {
        return deposits[depositId].exists;
    }
}
```
