"""
Generated Code Metadata:
========================
Original URL: https://soniclaqs.com
Prompt: Write a Solidity smart contract that utilizes Sonic's EVM compatibility for high-speed transactions.
Generated: DETERMINISTIC_384e3bc23b3d1b2d
Batch ID: 20250612_155442
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

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// SonicEVM is a smart contract that demonstrates high-speed transactions
contract SonicEVM is Ownable {
    // Event to log successful transactions
    event TransactionExecuted(address indexed sender, uint256 amount, string message);

    // Mapping to keep track of balances
    mapping(address => uint256) private balances;

    // Modifier to check if the sender has sufficient balance
    modifier hasSufficientBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    // Function to deposit Ether into the contract
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    // Function to withdraw Ether from the contract
    function withdraw(uint256 amount) external hasSufficientBalance(amount) {
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit TransactionExecuted(msg.sender, amount, "Withdrawal successful");
    }

    // Function to execute a high-speed transaction
    function executeTransaction(address recipient, uint256 amount, string calldata message) 
        external 
        hasSufficientBalance(amount) 
    {
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit TransactionExecuted(msg.sender, amount, message);
    }

    // Function to check the balance of an address
    function checkBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    // Function to withdraw contract's balance in case of emergency
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");
        payable(owner()).transfer(contractBalance);
    }

    // Fallback function to accept Ether
    receive() external payable {
        deposit();
    }
}
```
