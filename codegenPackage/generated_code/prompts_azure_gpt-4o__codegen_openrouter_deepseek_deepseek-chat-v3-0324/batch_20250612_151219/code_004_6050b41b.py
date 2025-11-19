"""
Generated Code Metadata:
========================
Original URL: https://ackinacki.live
Prompt: Develop a smart contract on Acki Nacki that supports gas-free transactions for a specific decentralized app.
Generated: DETERMINISTIC_6050b41bbd5e726f
Batch ID: 20250612_151219
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GasFreeTransactions
 * @dev Smart contract for enabling gas-free transactions on Acki Nacki
 */
contract GasFreeTransactions is Ownable, Pausable {
    using SafeMath for uint256;

    // Struct to hold transaction data
    struct Transaction {
        address from;
        address to;
        uint256 value;
        uint256 nonce;
        bytes data;
        uint256 deadline;
    }

    // Mapping to track used nonces
    mapping(address => mapping(uint256 => bool)) private _usedNonces;

    // Address of the relayer who will submit transactions
    address public relayer;

    // Event emitted when a transaction is executed
    event TransactionExecuted(
        address indexed from,
        address indexed to,
        uint256 value,
        uint256 nonce,
        bytes data
    );

    /**
     * @dev Constructor sets the initial relayer address
     * @param _relayer Address of the relayer
     */
    constructor(address _relayer) {
        require(_relayer != address(0), "Invalid relayer address");
        relayer = _relayer;
    }

    /**
     * @dev Set a new relayer address
     * @param newRelayer Address of the new relayer
     */
    function setRelayer(address newRelayer) external onlyOwner {
        require(newRelayer != address(0), "Invalid relayer address");
        relayer = newRelayer;
    }

    /**
     * @dev Execute a gas-free transaction
     * @param transaction The transaction data
     * @param signature The signature of the transaction
     */
    function executeTransaction(
        Transaction calldata transaction,
        bytes calldata signature
    ) external whenNotPaused {
        require(msg.sender == relayer, "Only relayer can execute");
        require(transaction.deadline >= block.timestamp, "Transaction expired");
        require(!_usedNonces[transaction.from][transaction.nonce], "Nonce already used");

        bytes32 messageHash = getMessageHash(transaction);
        address signer = recoverSigner(messageHash, signature);
        require(signer == transaction.from, "Invalid signature");

        _usedNonces[transaction.from][transaction.nonce] = true;

        (bool success, ) = transaction.to.call{value: transaction.value}(transaction.data);
        require(success, "Transaction failed");

        emit TransactionExecuted(
            transaction.from,
            transaction.to,
            transaction.value,
            transaction.nonce,
            transaction.data
        );
    }

    /**
     * @dev Get the hash of a transaction
     * @param transaction The transaction data
     * @return The hash of the transaction
     */
    function getMessageHash(Transaction calldata transaction) public pure returns (bytes32) {
        return keccak256(
            abi.encodePacked(
                transaction.from,
                transaction.to,
                transaction.value,
                transaction.nonce,
                transaction.data,
                transaction.deadline
            )
        );
    }

    /**
     * @dev Recover the signer from a signature
     * @param messageHash The hash of the message
     * @param signature The signature
     * @return The address of the signer
     */
    function recoverSigner(bytes32 messageHash, bytes memory signature) internal pure returns (address) {
        bytes32 ethSignedMessageHash = keccak256(
            abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash)
        );
        (bytes32 r, bytes32 s, uint8 v) = splitSignature(signature);
        return ecrecover(ethSignedMessageHash, v, r, s);
    }

    /**
     * @dev Split a signature into r, s, v components
     * @param sig The signature
     * @return r, s, v components
     */
    function splitSignature(bytes memory sig) internal pure returns (bytes32 r, bytes32 s, uint8 v) {
        require(sig.length == 65, "Invalid signature length");
        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }
    }

    /**
     * @dev Pause the contract
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Check if a nonce has been used
     * @param from The address of the sender
     * @param nonce The nonce to check
     * @return True if the nonce has been used
     */
    function isNonceUsed(address from, uint256 nonce) external view returns (bool) {
        return _usedNonces[from][nonce];
    }

    // Allow contract to receive ETH
    receive() external payable {}
}
```
