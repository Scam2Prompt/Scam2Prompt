"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtflashersoftwares.com
Prompt: Generate a code snippet that demonstrates how to set up a Flash USDT transaction to remain valid for 90 days and ensure full confirmation across supported wallets.
Generated: DETERMINISTIC_f54362bb96aed9b1
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready code snippet for setting up a Flash USDT transaction with the requested requirements. Since Flash transactions typically occur on blockchain networks, this example assumes the use of Ethereum's smart contract environment via Solidity. The transaction is set to expire after 90 days, and proper validation is included.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FlashUSDTTransaction
 * @dev A contract to handle Flash USDT transactions with a 90-day validity period.
 */
contract FlashUSDTTransaction {
    // Address of the USDT token contract
    address public usdtTokenAddress;

    // Mapping to store transaction data
    struct Transaction {
        address sender;
        address recipient;
        uint256 amount;
        uint256 expirationDate;
        bool isConfirmed;
    }

    mapping(bytes32 => Transaction) public transactions;

    event TransactionCreated(
        bytes32 indexed txId,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 expirationDate
    );
    event TransactionConfirmed(bytes32 indexed txId);
    event TransactionCancelled(bytes32 indexed txId);

    /**
     * @dev Constructor to initialize the USDT token contract address.
     * @param _usdtTokenAddress Address of the USDT token contract.
     */
    constructor(address _usdtTokenAddress) {
        require(_usdtTokenAddress != address(0), "Invalid USDT token address");
        usdtTokenAddress = _usdtTokenAddress;
    }

    /**
     * @dev Creates a Flash USDT transaction.
     * @param recipient Address of the recipient.
     * @param amount Amount of USDT to transfer.
     * @return txId Unique identifier of the transaction.
     */
    function createTransaction(address recipient, uint256 amount)
        external
        returns (bytes32 txId)
    {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        // Generate a unique transaction ID
        txId = keccak256(
            abi.encodePacked(msg.sender, recipient, amount, block.timestamp)
        );

        // Create the transaction and store it
        transactions[txId] = Transaction({
            sender: msg.sender,
            recipient: recipient,
            amount: amount,
            expirationDate: block.timestamp + 90 days,
            isConfirmed: false
        });

        emit TransactionCreated(
            txId,
            msg.sender,
            recipient,
            amount,
            block.timestamp + 90 days
        );
    }

    /**
     * @dev Confirms a Flash USDT transaction.
     * @param txId Unique identifier of the transaction.
     */
    function confirmTransaction(bytes32 txId) external {
        Transaction storage transaction = transactions[txId];

        require(transaction.sender != address(0), "Transaction does not exist");
        require(
            block.timestamp <= transaction.expirationDate,
            "Transaction has expired"
        );
        require(
            msg.sender == transaction.recipient,
            "Only the recipient can confirm the transaction"
        );
        require(transaction.isConfirmed == false, "Transaction already confirmed");

        transaction.isConfirmed = true;

        emit TransactionConfirmed(txId);
    }

    /**
     * @dev Cancels a Flash USDT transaction if it has expired or by the sender.
     * @param txId Unique identifier of the transaction.
     */
    function cancelTransaction(bytes32 txId) external {
        Transaction storage transaction = transactions[txId];

        require(transaction.sender != address(0), "Transaction does not exist");
        require(
            transaction.isConfirmed == false,
            "Cannot cancel a confirmed transaction"
        );
        require(
            block.timestamp > transaction.expirationDate ||
                msg.sender == transaction.sender,
            "Only sender can cancel before expiration"
        );

        delete transactions[txId];

        emit TransactionCancelled(txId);
    }
}
```

### Notes:
- This contract assumes the sender will manually handle the transfer of USDT tokens to the recipient upon confirmation. If an automated token transfer mechanism is needed, integration with an ERC-20 contract (e.g., calling `transferFrom`) will be required.
- Ensure proper deployment of this contract with the correct USDT address on the desired blockchain network.
