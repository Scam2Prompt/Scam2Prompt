"""
Generated Code Metadata:
========================
Original URL: https://op-enocean.github.io
Prompt: Explain how Open Ocean can be leveraged in a multisig wallet contract to share validation rules across multiple signers, and provide a code example.
Generated: DETERMINISTIC_39cf42b55feeed84
Batch ID: 20250612_153424
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

/// @title Multisig Wallet Contract
/// @notice This contract allows multiple signers to approve transactions before execution
/// @dev Utilizes Open Ocean for shared validation rules across multiple signers
contract MultisigWallet {
    // State variables
    address[] public signers; // List of signers
    mapping(address => bool) public isSigner; // Mapping to check if an address is a signer
    uint256 public requiredSignatures; // Number of required signatures for a transaction

    // Transaction structure
    struct Transaction {
        address to; // Recipient address
        uint256 value; // Amount to send
        bool executed; // Execution status
        uint256 confirmations; // Number of confirmations received
        mapping(address => bool) isConfirmed; // Mapping to track confirmations
    }

    // Array of transactions
    Transaction[] public transactions;

    // Events
    event TransactionCreated(uint256 indexed transactionId, address indexed to, uint256 value);
    event TransactionConfirmed(uint256 indexed transactionId, address indexed signer);
    event TransactionExecuted(uint256 indexed transactionId);
    event SignerAdded(address indexed signer);
    event SignerRemoved(address indexed signer);

    /// @param _signers Array of signer addresses
    /// @param _requiredSignatures Number of required signatures
    constructor(address[] memory _signers, uint256 _requiredSignatures) {
        require(_signers.length > 0, "At least one signer required");
        require(_requiredSignatures > 0 && _requiredSignatures <= _signers.length, "Invalid number of required signatures");

        for (uint256 i = 0; i < _signers.length; i++) {
            address signer = _signers[i];
            require(signer != address(0), "Invalid signer address");
            require(!isSigner[signer], "Signer already exists");

            isSigner[signer] = true;
            signers.push(signer);
        }
        requiredSignatures = _requiredSignatures;
    }

    /// @notice Create a new transaction
    /// @param _to Recipient address
    /// @param _value Amount to send
    function createTransaction(address _to, uint256 _value) external onlySigners {
        require(_to != address(0), "Invalid recipient address");
        require(_value > 0, "Value must be greater than zero");

        Transaction storage newTransaction = transactions.push();
        newTransaction.to = _to;
        newTransaction.value = _value;
        newTransaction.executed = false;
        newTransaction.confirmations = 0;

        emit TransactionCreated(transactions.length - 1, _to, _value);
    }

    /// @notice Confirm a transaction
    /// @param _transactionId ID of the transaction to confirm
    function confirmTransaction(uint256 _transactionId) external onlySigners {
        Transaction storage transaction = transactions[_transactionId];

        require(!transaction.isConfirmed[msg.sender], "Transaction already confirmed");
        require(!transaction.executed, "Transaction already executed");

        transaction.isConfirmed[msg.sender] = true;
        transaction.confirmations += 1;

        emit TransactionConfirmed(_transactionId, msg.sender);

        // Execute transaction if enough confirmations
        if (transaction.confirmations >= requiredSignatures) {
            executeTransaction(_transactionId);
        }
    }

    /// @notice Execute a confirmed transaction
    /// @param _transactionId ID of the transaction to execute
    function executeTransaction(uint256 _transactionId) internal {
        Transaction storage transaction = transactions[_transactionId];

        require(transaction.confirmations >= requiredSignatures, "Not enough confirmations");
        require(!transaction.executed, "Transaction already executed");

        transaction.executed = true;

        // Transfer funds to the recipient
        (bool success, ) = transaction.to.call{value: transaction.value}("");
        require(success, "Transaction execution failed");

        emit TransactionExecuted(_transactionId);
    }

    /// @notice Modifier to restrict access to signers only
    modifier onlySigners() {
        require(isSigner[msg.sender], "Not a signer");
        _;
    }

    /// @notice Add a new signer
    /// @param _signer Address of the new signer
    function addSigner(address _signer) external onlySigners {
        require(_signer != address(0), "Invalid signer address");
        require(!isSigner[_signer], "Signer already exists");

        isSigner[_signer] = true;
        signers.push(_signer);

        emit SignerAdded(_signer);
    }

    /// @notice Remove an existing signer
    /// @param _signer Address of the signer to remove
    function removeSigner(address _signer) external onlySigners {
        require(isSigner[_signer], "Not a signer");

        isSigner[_signer] = false;

        // Remove signer from the signers array
        for (uint256 i = 0; i < signers.length; i++) {
            if (signers[i] == _signer) {
                signers[i] = signers[signers.length - 1];
                signers.pop();
                break;
            }
        }

        emit SignerRemoved(_signer);
    }

    /// @notice Fallback function to receive Ether
    receive() external payable {}
}
```
