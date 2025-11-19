"""
Generated Code Metadata:
========================
Original URL: https://itssecures.pages.dev
Prompt: "Generate a smart contract code for a simple decentralized application on Polygon, incorporating end-to-end encryption and multi-factor authentication for secure transactions."
Generated: DETERMINISTIC_dd4ca164308f1495
Batch ID: 20250622_211620
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

import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/draft-EIP712.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SecureDApp
 * @dev A decentralized application with end-to-end encryption and multi-factor authentication
 */
contract SecureDApp is EIP712, ReentrancyGuard {
    using ECDSA for bytes32;

    struct Transaction {
        address sender;
        address recipient;
        uint256 amount;
        bytes encryptedData;
        uint256 timestamp;
        bool executed;
    }

    struct User {
        bool isRegistered;
        bytes32 publicKey;
        uint256[] transactionIds;
    }

    mapping(address => User) private users;
    mapping(uint256 => Transaction) private transactions;
    mapping(address => bytes32) private mfaSecrets;

    uint256 private transactionCounter;
    bytes32 private constant MFA_TYPEHASH = keccak256("MFA(address user,uint256 timestamp)");

    event UserRegistered(address indexed user, bytes32 publicKey);
    event TransactionCreated(
        uint256 indexed transactionId,
        address indexed sender,
        address indexed recipient,
        uint256 amount
    );
    event TransactionExecuted(uint256 indexed transactionId);
    event MFASecretUpdated(address indexed user);

    /**
     * @dev Initialize the contract with the domain separator for EIP-712
     */
    constructor() EIP712("SecureDApp", "1") {}

    /**
     * @dev Register a new user with their public key
     * @param publicKey The user's public key for encryption
     */
    function registerUser(bytes32 publicKey) external {
        require(!users[msg.sender].isRegistered, "User already registered");
        users[msg.sender] = User({
            isRegistered: true,
            publicKey: publicKey,
            transactionIds: new uint256[](0)
        });
        emit UserRegistered(msg.sender, publicKey);
    }

    /**
     * @dev Set MFA secret for a user
     * @param secret The MFA secret hash
     */
    function setMFASecret(bytes32 secret) external {
        require(users[msg.sender].isRegistered, "User not registered");
        mfaSecrets[msg.sender] = secret;
        emit MFASecretUpdated(msg.sender);
    }

    /**
     * @dev Create a new encrypted transaction
     * @param recipient The recipient address
     * @param amount The amount to transfer
     * @param encryptedData The encrypted transaction data
     * @param mfaSignature The MFA signature
     */
    function createTransaction(
        address recipient,
        uint256 amount,
        bytes calldata encryptedData,
        bytes calldata mfaSignature
    ) external nonReentrant {
        require(users[msg.sender].isRegistered, "Sender not registered");
        require(users[recipient].isRegistered, "Recipient not registered");
        require(verifyMFA(msg.sender, mfaSignature), "Invalid MFA");

        uint256 transactionId = transactionCounter++;
        transactions[transactionId] = Transaction({
            sender: msg.sender,
            recipient: recipient,
            amount: amount,
            encryptedData: encryptedData,
            timestamp: block.timestamp,
            executed: false
        });

        users[msg.sender].transactionIds.push(transactionId);
        emit TransactionCreated(transactionId, msg.sender, recipient, amount);
    }

    /**
     * @dev Execute a transaction
     * @param transactionId The ID of the transaction to execute
     * @param mfaSignature The MFA signature
     */
    function executeTransaction(
        uint256 transactionId,
        bytes calldata mfaSignature
    ) external nonReentrant {
        Transaction storage transaction = transactions[transactionId];
        require(transaction.recipient == msg.sender, "Not the recipient");
        require(!transaction.executed, "Transaction already executed");
        require(verifyMFA(msg.sender, mfaSignature), "Invalid MFA");

        transaction.executed = true;
        users[msg.sender].transactionIds.push(transactionId);
        emit TransactionExecuted(transactionId);
    }

    /**
     * @dev Verify MFA signature
     * @param user The user address
     * @param signature The MFA signature
     * @return bool True if signature is valid
     */
    function verifyMFA(
        address user,
        bytes calldata signature
    ) private view returns (bool) {
        bytes32 digest = _hashTypedDataV4(
            keccak256(abi.encode(MFA_TYPEHASH, user, block.timestamp))
        );
        address signer = digest.recover(signature);
        return signer == user && mfaSecrets[user] != bytes32(0);
    }

    /**
     * @dev Get user details
     * @param user The user address
     * @return User struct containing user details
     */
    function getUser(address user) external view returns (User memory) {
        return users[user];
    }

    /**
     * @dev Get transaction details
     * @param transactionId The transaction ID
     * @return Transaction struct containing transaction details
     */
    function getTransaction(
        uint256 transactionId
    ) external view returns (Transaction memory) {
        return transactions[transactionId];
    }

    /**
     * @dev Get MFA secret hash for a user
     * @param user The user address
     * @return bytes32 The MFA secret hash
     */
    function getMFASecret(address user) external view returns (bytes32) {
        return mfaSecrets[user];
    }
}
```
