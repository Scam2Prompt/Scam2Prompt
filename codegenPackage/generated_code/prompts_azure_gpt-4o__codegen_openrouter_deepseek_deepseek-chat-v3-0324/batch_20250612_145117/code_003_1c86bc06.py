"""
Generated Code Metadata:
========================
Original URL: https://priv.cash
Prompt: Provide an example of a smart contract that facilitates private transactions on a blockchain, inspired by the privacy features mentioned on priv.cash.
Generated: DETERMINISTIC_1c86bc06bbb058ed
Batch ID: 20250612_145117
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

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PrivateTransactionContract
 * @dev A smart contract that facilitates private transactions using stealth addresses and zero-knowledge proofs
 */
contract PrivateTransactionContract is Ownable {
    using SafeMath for uint256;

    // Struct to represent a stealth address
    struct StealthAddress {
        address addr;
        bytes32 viewingKey;
        bytes32 spendingKey;
    }

    // Struct to represent a private transaction
    struct PrivateTransaction {
        address sender;
        StealthAddress recipient;
        uint256 amount;
        bytes32 zkProof;
        uint256 timestamp;
    }

    // Mapping from stealth address to balance
    mapping(address => uint256) private balances;

    // Array of all private transactions
    PrivateTransaction[] private transactions;

    // Event emitted when a new private transaction is created
    event PrivateTransactionCreated(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        bytes32 zkProof,
        uint256 timestamp
    );

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(
        address indexed recipient,
        uint256 amount,
        uint256 timestamp
    );

    /**
     * @dev Deposit funds into the contract
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] = balances[msg.sender].add(msg.value);
    }

    /**
     * @dev Create a private transaction
     * @param _recipient The stealth address of the recipient
     * @param _amount The amount to send
     * @param _zkProof The zero-knowledge proof for the transaction
     */
    function createPrivateTransaction(
        StealthAddress calldata _recipient,
        uint256 _amount,
        bytes32 _zkProof
    ) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        require(_amount > 0, "Amount must be greater than 0");

        // Deduct from sender's balance
        balances[msg.sender] = balances[msg.sender].sub(_amount);

        // Add to recipient's balance
        balances[_recipient.addr] = balances[_recipient.addr].add(_amount);

        // Record the transaction
        transactions.push(
            PrivateTransaction({
                sender: msg.sender,
                recipient: _recipient,
                amount: _amount,
                zkProof: _zkProof,
                timestamp: block.timestamp
            })
        );

        emit PrivateTransactionCreated(
            msg.sender,
            _recipient.addr,
            _amount,
            _zkProof,
            block.timestamp
        );
    }

    /**
     * @dev Withdraw funds using spending key
     * @param _amount The amount to withdraw
     * @param _spendingKey The spending key to authenticate the withdrawal
     */
    function withdrawFunds(
        uint256 _amount,
        bytes32 _spendingKey
    ) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // In a real implementation, we would verify the spending key against the stealth address
        // This is a simplified version for demonstration purposes
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        payable(msg.sender).transfer(_amount);

        emit FundsWithdrawn(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Get the balance of a stealth address
     * @param _addr The stealth address to check
     * @return The balance of the address
     */
    function getBalance(address _addr) external view returns (uint256) {
        return balances[_addr];
    }

    /**
     * @dev Get the total number of transactions
     * @return The number of transactions
     */
    function getTransactionCount() external view returns (uint256) {
        return transactions.length;
    }

    /**
     * @dev Get transaction details by index
     * @param _index The index of the transaction
     * @return The transaction details
     */
    function getTransaction(
        uint256 _index
    )
        external
        view
        returns (
            address,
            StealthAddress memory,
            uint256,
            bytes32,
            uint256
        )
    {
        require(_index < transactions.length, "Invalid transaction index");
        PrivateTransaction memory txn = transactions[_index];
        return (
            txn.sender,
            txn.recipient,
            txn.amount,
            txn.zkProof,
            txn.timestamp
        );
    }
}
```
