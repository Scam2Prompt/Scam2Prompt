"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: Explain how Open Ocean can be leveraged in a multisig wallet contract to share validation rules across multiple signers, and provide a code example.
Generated: DETERMINISTIC_39cf42b55feeed84
Batch ID: 20250612_153424
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

/// @title MultiSigWallet
/// @notice This contract allows multiple owners to manage funds with a multisig wallet.
/// @dev Open Ocean can be integrated to share validation rules across multiple signers.
contract MultiSigWallet {
    // State variables
    address[] public owners;         // Array of wallet owners
    mapping(address => bool) public isOwner; // Mapping to check if an address is an owner
    uint256 public requiredSignatures; // Number of required signatures for a transaction

    // Struct to hold transaction details
    struct Transaction {
        address to;
        uint256 value;
        bytes data;
        bool executed;
        uint256 confirmations; // Number of confirmations received
        mapping(address => bool) isConfirmed; // Confirmations by owners
    }

    Transaction[] public transactions; // List of all transactions

    // Events
    event TransactionCreated(uint256 indexed txIndex, address indexed to, uint256 value, bytes data);
    event TransactionConfirmed(uint256 indexed txIndex, address indexed owner);
    event TransactionExecuted(uint256 indexed txIndex);
    event TransactionRevoked(uint256 indexed txIndex, address indexed owner);

    // Modifiers
    modifier onlyOwner() {
        require(isOwner[msg.sender], "Caller is not an owner");
        _;
    }

    modifier transactionExists(uint256 txIndex) {
        require(txIndex < transactions.length, "Transaction does not exist");
        _;
    }

    modifier notExecuted(uint256 txIndex) {
        require(!transactions[txIndex].executed, "Transaction already executed");
        _;
    }

    modifier notConfirmed(uint256 txIndex) {
        require(!transactions[txIndex].isConfirmed[msg.sender], "Transaction already confirmed");
        _;
    }

    /// @notice Contract constructor to initialize owners and required signatures
    /// @param _owners List of wallet owners
    /// @param _requiredSignatures Minimum required confirmations to execute a transaction
    constructor(address[] memory _owners, uint256 _requiredSignatures) {
        require(_owners.length > 0, "Owners required");
        require(_requiredSignatures > 0 && _requiredSignatures <= _owners.length, "Invalid number of required signatures");

        for (uint256 i = 0; i < _owners.length; i++) {
            require(!isOwner[_owners[i]], "Duplicate owner detected");
            isOwner[_owners[i]] = true;
        }

        owners = _owners;
        requiredSignatures = _requiredSignatures;
    }

    /// @notice Create a new transaction and emit an event
    /// @param _to Address to send funds to
    /// @param _value Amount of Ether to send
    /// @param _data Additional data to send
    function createTransaction(address _to, uint256 _value, bytes memory _data) public onlyOwner {
        Transaction storage newTx = transactions.push();
        newTx.to = _to;
        newTx.value = _value;
        newTx.data = _data;
        newTx.executed = false;
        newTx.confirmations = 0;

        emit TransactionCreated(transactions.length - 1, _to, _value, _data);
    }

    /// @notice Confirm a transaction
    /// @param txIndex Index of the transaction to confirm
    function confirmTransaction(uint256 txIndex) public onlyOwner transactionExists(txIndex) notExecuted(txIndex) notConfirmed(txIndex) {
        Transaction storage transaction = transactions[txIndex];
        transaction.isConfirmed[msg.sender] = true;
        transaction.confirmations++;

        emit TransactionConfirmed(txIndex, msg.sender);

        // Execute the transaction if enough confirmations are reached
        if (transaction.confirmations >= requiredSignatures) {
            executeTransaction(txIndex);
        }
    }

    /// @notice Execute a confirmed transaction
    /// @param txIndex Index of the transaction to execute
    function executeTransaction(uint256 txIndex) internal transactionExists(txIndex) notExecuted(txIndex) {
        Transaction storage transaction = transactions[txIndex];
        require(transaction.confirmations >= requiredSignatures, "Not enough confirmations");
        
        // Mark as executed
        transaction.executed = true;

        // Call the target address with the provided value and data
        (bool success, ) = transaction.to.call{value: transaction.value}(transaction.data);
        require(success, "Transaction execution failed");

        emit TransactionExecuted(txIndex);
    }

    /// @notice Revoke a confirmation for a transaction
    /// @param txIndex Index of the transaction to revoke
    function revokeConfirmation(uint256 txIndex) public onlyOwner transactionExists(txIndex) notExecuted(txIndex) {
        Transaction storage transaction = transactions[txIndex];
        require(transaction.isConfirmed[msg.sender], "Transaction not confirmed");

        transaction.isConfirmed[msg.sender] = false;
        transaction.confirmations--;

        emit TransactionRevoked(txIndex, msg.sender);
    }

    /// @notice Allow the contract to receive Ether
    receive() external payable {}
}
```
