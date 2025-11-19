"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbdfinancialsmig.pages.dev
Prompt: Create an example of a smart contract for managing transactions in the MBD Boulevard phygital marketplace, ensuring compliance with Web3 standards.
Generated: DETERMINISTIC_9866462a16da03ab
Batch ID: 20250612_163742
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
 * @title MBD Boulevard Marketplace Smart Contract
 * @dev This contract handles transactions in the phygital marketplace, ensuring Web3 compliance.
 */
contract MBDMarketplace {
    // Owner of the smart contract (platform admin)
    address public owner;

    // Struct to represent a transaction
    struct Transaction {
        uint256 id;
        address buyer;
        address seller;
        uint256 amount;
        bool completed;
    }

    // Mapping to store all transactions by ID
    mapping(uint256 => Transaction) public transactions;

    // Counter for transaction IDs
    uint256 private transactionCounter;

    // Event emitted when a transaction is created
    event TransactionCreated(
        uint256 indexed id,
        address indexed buyer,
        address indexed seller,
        uint256 amount
    );

    // Event emitted when a transaction is completed
    event TransactionCompleted(uint256 indexed id);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new transaction between buyer and seller.
     * @param _buyer Address of the buyer.
     * @param _seller Address of the seller.
     * @param _amount Amount involved in the transaction.
     * @return Transaction ID.
     */
    function createTransaction(
        address _buyer,
        address _seller,
        uint256 _amount
    ) external onlyOwner returns (uint256) {
        require(_buyer != address(0), "Buyer address cannot be zero");
        require(_seller != address(0), "Seller address cannot be zero");
        require(_amount > 0, "Transaction amount must be greater than zero");

        transactionCounter++;

        transactions[transactionCounter] = Transaction({
            id: transactionCounter,
            buyer: _buyer,
            seller: _seller,
            amount: _amount,
            completed: false
        });

        emit TransactionCreated(transactionCounter, _buyer, _seller, _amount);

        return transactionCounter;
    }

    /**
     * @dev Complete a transaction.
     * @param _transactionId ID of the transaction to be completed.
     */
    function completeTransaction(uint256 _transactionId) external {
        Transaction storage transaction = transactions[_transactionId];

        require(!transaction.completed, "Transaction is already completed");
        require(
            msg.sender == transaction.buyer || msg.sender == transaction.seller,
            "Only buyer or seller can complete the transaction"
        );

        transaction.completed = true;

        emit TransactionCompleted(_transactionId);
    }

    /**
     * @dev Retrieve details of a transaction.
     * @param _transactionId ID of the transaction.
     * @return Transaction details (id, buyer, seller, amount, completed).
     */
    function getTransactionDetails(
        uint256 _transactionId
    )
        external
        view
        returns (
            uint256,
            address,
            address,
            uint256,
            bool
        )
    {
        Transaction memory transaction = transactions[_transactionId];
        return (
            transaction.id,
            transaction.buyer,
            transaction.seller,
            transaction.amount,
            transaction.completed
        );
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether transfers are not accepted");
    }

    /**
     * @dev Receive function to handle direct Ether transfers (not used here).
     */
    receive() external payable {
        revert("Ether transfers are not accepted");
    }
}
```
