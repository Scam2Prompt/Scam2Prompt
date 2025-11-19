"""
Generated Code Metadata:
========================
Original URL: https://dione-9h0.pages.dev
Prompt: "Generate a smart contract code for facilitating secure transactions of clean energy through a blockchain platform like Nebra on Dione Protocol."
Generated: DETERMINISTIC_c45284d90daf8083
Batch ID: 20250622_210057
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

/**
 * @title CleanEnergyTransaction
 * @dev A smart contract for facilitating secure transactions of clean energy
 *      on a blockchain platform like Nebra on Dione Protocol.
 */
contract CleanEnergyTransaction {
    // Struct to represent an energy transaction
    struct EnergyTransaction {
        address buyer; // Address of the buyer
        address seller; // Address of the seller
        uint256 energyAmount; // Amount of energy in kWh
        uint256 price; // Price per kWh in wei
        bool completed; // Status of the transaction
    }

    // Mapping to store transactions by ID
    mapping(uint256 => EnergyTransaction) public transactions;

    // Counter for transaction IDs
    uint256 public transactionCounter;

    // Event emitted when a new transaction is created
    event TransactionCreated(
        uint256 indexed transactionId,
        address indexed buyer,
        address indexed seller,
        uint256 energyAmount,
        uint256 price
    );

    // Event emitted when a transaction is completed
    event TransactionCompleted(uint256 indexed transactionId);

    /**
     * @dev Create a new energy transaction.
     * @param _seller Address of the seller.
     * @param _energyAmount Amount of energy in kWh.
     * @param _price Price per kWh in wei.
     */
    function createTransaction(
        address _seller,
        uint256 _energyAmount,
        uint256 _price
    ) external payable {
        require(_seller != address(0), "Seller address cannot be zero.");
        require(_energyAmount > 0, "Energy amount must be greater than zero.");
        require(_price > 0, "Price must be greater than zero.");
        require(
            msg.value == _energyAmount * _price,
            "Incorrect payment amount."
        );

        // Increment transaction counter
        transactionCounter++;

        // Create a new transaction
        transactions[transactionCounter] = EnergyTransaction({
            buyer: msg.sender,
            seller: _seller,
            energyAmount: _energyAmount,
            price: _price,
            completed: false
        });

        // Emit event for transaction creation
        emit TransactionCreated(
            transactionCounter,
            msg.sender,
            _seller,
            _energyAmount,
            _price
        );
    }

    /**
     * @dev Complete a transaction and transfer funds to the seller.
     * @param _transactionId ID of the transaction to complete.
     */
    function completeTransaction(uint256 _transactionId) external {
        EnergyTransaction storage transaction = transactions[_transactionId];

        require(
            transaction.seller == msg.sender,
            "Only the seller can complete the transaction."
        );
        require(!transaction.completed, "Transaction already completed.");

        // Mark the transaction as completed
        transaction.completed = true;

        // Transfer funds to the seller
        payable(transaction.seller).transfer(
            transaction.energyAmount * transaction.price
        );

        // Emit event for transaction completion
        emit TransactionCompleted(_transactionId);
    }

    /**
     * @dev Get details of a transaction.
     * @param _transactionId ID of the transaction to retrieve.
     * @return buyer Address of the buyer.
     * @return seller Address of the seller.
     * @return energyAmount Amount of energy in kWh.
     * @return price Price per kWh in wei.
     * @return completed Status of the transaction.
     */
    function getTransactionDetails(uint256 _transactionId)
        external
        view
        returns (
            address buyer,
            address seller,
            uint256 energyAmount,
            uint256 price,
            bool completed
        )
    {
        EnergyTransaction storage transaction = transactions[_transactionId];
        return (
            transaction.buyer,
            transaction.seller,
            transaction.energyAmount,
            transaction.price,
            transaction.completed
        );
    }
}
```
