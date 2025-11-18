"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexmultichains.co
Prompt: Generate a smart contract for managing transactions within the Utopos blockchain city framework.
Generated: DETERMINISTIC_175280e3600fb513
Batch ID: 20250612_151018
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

/**
 * @title UtoposTransactionManager
 * @dev Smart contract for managing transactions in the Utopos blockchain city framework.
 */
contract UtoposTransactionManager {
    // Event to log successful transactions
    event TransactionExecuted(
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        uint256 timestamp
    );

    // Event to log failed transactions
    event TransactionFailed(
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        string reason,
        uint256 timestamp
    );

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to specific functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Function to execute a transaction between two parties.
     * @param receiver The address to receive the funds.
     * @param amount The amount to be transferred in wei.
     */
    function executeTransaction(address payable receiver, uint256 amount) external payable {
        // Check that the transaction sender has enough balance
        require(msg.sender.balance >= amount, "Insufficient balance.");
        
        // Check that the amount to transfer is greater than 0
        require(amount > 0, "Transfer amount must be greater than 0.");

        // Try to transfer the amount and handle errors
        try receiver.send(amount) {
            emit TransactionExecuted(msg.sender, receiver, amount, block.timestamp);
        } catch {
            emit TransactionFailed(msg.sender, receiver, amount, "Transfer failed.", block.timestamp);
        }
    }

    /**
     * @dev Function to withdraw funds from the contract (only by the owner).
     * @param amount The amount to withdraw in wei.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance.");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to check the contract's balance.
     * @return The current balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
