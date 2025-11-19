"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Generate a Solidity smart contract that tracks and displays recent transactions, including deposits, reinvestments, and redistributions, similar to the transaction table on BibbyDivs.com.
Generated: DETERMINISTIC_6c23a5f72555d4a3
Batch ID: 20250612_150316
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

contract TransactionTracker {
    // Struct to represent a transaction
    struct Transaction {
        address user;
        uint256 amount;
        uint256 timestamp;
        string transactionType; // "DEPOSIT", "REINVEST", "REDISTRIBUTION"
    }

    // Array to store all transactions
    Transaction[] public transactions;

    // Event emitted when a new transaction is recorded
    event TransactionRecorded(
        address indexed user,
        uint256 amount,
        uint256 timestamp,
        string transactionType
    );

    // Modifier to check for zero address
    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    // Modifier to check for zero amount
    modifier validAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Record a new transaction
     * @param _user Address of the user involved in the transaction
     * @param _amount Amount of the transaction
     * @param _transactionType Type of transaction ("DEPOSIT", "REINVEST", "REDISTRIBUTION")
     */
    function recordTransaction(
        address _user,
        uint256 _amount,
        string memory _transactionType
    ) external validAddress(_user) validAmount(_amount) {
        // Validate transaction type
        require(
            keccak256(abi.encodePacked(_transactionType)) == keccak256(abi.encodePacked("DEPOSIT")) ||
            keccak256(abi.encodePacked(_transactionType)) == keccak256(abi.encodePacked("REINVEST")) ||
            keccak256(abi.encodePacked(_transactionType)) == keccak256(abi.encodePacked("REDISTRIBUTION")),
            "Invalid transaction type"
        );

        transactions.push(Transaction({
            user: _user,
            amount: _amount,
            timestamp: block.timestamp,
            transactionType: _transactionType
        }));

        emit TransactionRecorded(_user, _amount, block.timestamp, _transactionType);
    }

    /**
     * @dev Get the total number of transactions
     * @return uint256 Count of transactions
     */
    function getTransactionCount() external view returns (uint256) {
        return transactions.length;
    }

    /**
     * @dev Get paginated transactions
     * @param _page Page number (1-based)
     * @param _perPage Number of items per page
     * @return Transaction[] Array of transactions for the requested page
     */
    function getPaginatedTransactions(
        uint256 _page,
        uint256 _perPage
    ) external view returns (Transaction[] memory) {
        require(_page > 0, "Page must be greater than 0");
        require(_perPage > 0, "Items per page must be greater than 0");

        uint256 start = (_page - 1) * _perPage;
        uint256 end = start + _perPage;

        // Adjust end if it exceeds array length
        if (end > transactions.length) {
            end = transactions.length;
        }

        // Return empty array if start is beyond array length
        if (start >= transactions.length) {
            return new Transaction[](0);
        }

        Transaction[] memory pageTransactions = new Transaction[](end - start);
        
        for (uint256 i = start; i < end; i++) {
            pageTransactions[i - start] = transactions[i];
        }

        return pageTransactions;
    }

    /**
     * @dev Get latest transactions
     * @param _count Number of latest transactions to return
     * @return Transaction[] Array of latest transactions
     */
    function getLatestTransactions(
        uint256 _count
    ) external view returns (Transaction[] memory) {
        require(_count > 0, "Count must be greater than 0");

        uint256 start = transactions.length > _count ? transactions.length - _count : 0;
        uint256 resultCount = transactions.length > _count ? _count : transactions.length;

        Transaction[] memory latestTransactions = new Transaction[](resultCount);
        
        for (uint256 i = 0; i < resultCount; i++) {
            latestTransactions[i] = transactions[start + i];
        }

        return latestTransactions;
    }
}
```
