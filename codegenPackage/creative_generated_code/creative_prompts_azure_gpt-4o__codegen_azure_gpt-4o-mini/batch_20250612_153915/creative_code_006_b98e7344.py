"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton4.org
Prompt: Create a smart contract using TON blockchain for secure and automated business transactions, emphasizing its security features.
Generated: DETERMINISTIC_b98e7344cace777a
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma ton-solidity >=0.47.0;

// Import necessary TON libraries
import "Tvm.sol";

contract SecureBusinessTransaction {
    // Define state variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // Balances of each participant
    uint256 public transactionFee; // Transaction fee for using the contract

    // Event to notify transaction completion
    event TransactionCompleted(address indexed sender, address indexed receiver, uint256 amount);

    // Constructor to initialize the contract
    constructor(uint256 _transactionFee) public {
        require(_transactionFee > 0, "Transaction fee must be greater than zero.");
        owner = msg.sender; // Set the contract creator as the owner
        transactionFee = _transactionFee; // Set the transaction fee
    }

    // Function to deposit funds into the contract
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        
        // Update the balance of the sender
        balances[msg.sender] += msg.value;
    }

    // Function to execute a business transaction
    function executeTransaction(address payable receiver, uint256 amount) public {
        require(balances[msg.sender] >= amount + transactionFee, "Insufficient balance for the transaction.");

        // Deduct the transaction amount and fee from the sender's balance
        balances[msg.sender] -= (amount + transactionFee);
        balances[receiver] += amount; // Credit the receiver

        // Emit transaction event
        emit TransactionCompleted(msg.sender, receiver, amount);

        // Transfer the transaction fee to the owner
        owner.transfer(transactionFee);
    }

    // Function to withdraw funds from the contract
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance to withdraw.");
        
        // Update the balance before transferring to avoid re-entrancy attacks
        balances[msg.sender] -= amount;

        // Transfer the amount to the caller
        msg.sender.transfer(amount);
    }

    // Function to get the balance of a specific user
    function getBalance(address user) public view returns (uint256) {
        return balances[user];
    }

    // Function to change the transaction fee (only by the owner)
    function setTransactionFee(uint256 newFee) public {
        require(msg.sender == owner, "Only the owner can change the transaction fee.");
        require(newFee > 0, "Transaction fee must be greater than zero.");
        
        transactionFee = newFee; // Update the transaction fee
    }

    // Fallback function to prevent direct ether transfers to the contract
    receive() external payable {
        revert("Direct ether transfer not allowed. Use deposit function instead.");
    }
}
```
