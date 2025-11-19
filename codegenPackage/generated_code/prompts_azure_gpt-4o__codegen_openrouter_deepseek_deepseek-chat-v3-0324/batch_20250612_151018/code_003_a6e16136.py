"""
Generated Code Metadata:
========================
Original URL: https://epep-flip.vercel.app
Prompt: Create a smart contract that enables transaction-free gameplay for users who confirm their wallets, inspired by the EPEP platform.
Generated: DETERMINISTIC_a6e16136d8451ab2
Batch ID: 20250612_151018
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract TransactionFreeGameplay is Ownable {
    using ECDSA for bytes32;

    // Mapping to track confirmed wallets
    mapping(address => bool) public confirmedWallets;

    // Mapping to track used nonces to prevent replay attacks
    mapping(address => mapping(uint256 => bool)) public usedNonces;

    // Event emitted when a wallet is confirmed
    event WalletConfirmed(address indexed user);

    // Event emitted when a game action is performed
    event GameActionPerformed(
        address indexed user,
        string action,
        uint256 nonce
    );

    /**
     * @dev Confirms a wallet by verifying the signature
     * @param signature The signature proving wallet ownership
     */
    function confirmWallet(bytes calldata signature) external {
        require(!confirmedWallets[msg.sender], "Wallet already confirmed");
        
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender));
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        
        address recoveredAddress = ethSignedMessageHash.recover(signature);
        require(recoveredAddress == msg.sender, "Invalid signature");
        
        confirmedWallets[msg.sender] = true;
        emit WalletConfirmed(msg.sender);
    }

    /**
     * @dev Performs a game action without a transaction
     * @param user The address of the user performing the action
     * @param action The game action being performed
     * @param nonce A unique number to prevent replay attacks
     * @param signature The signature authorizing the action
     */
    function performGameAction(
        address user,
        string calldata action,
        uint256 nonce,
        bytes calldata signature
    ) external {
        require(confirmedWallets[user], "Wallet not confirmed");
        require(!usedNonces[user][nonce], "Nonce already used");

        bytes32 messageHash = keccak256(
            abi.encodePacked(user, action, nonce)
        );
        bytes32 ethSignedMessageHash = messageHash.toEthSignedMessageHash();
        
        address recoveredAddress = ethSignedMessageHash.recover(signature);
        require(recoveredAddress == user, "Invalid signature");

        usedNonces[user][nonce] = true;
        emit GameActionPerformed(user, action, nonce);
    }

    /**
     * @dev Allows owner to revoke a confirmed wallet
     * @param user The address to revoke confirmation for
     */
    function revokeConfirmation(address user) external onlyOwner {
        require(confirmedWallets[user], "Wallet not confirmed");
        confirmedWallets[user] = false;
    }
}
```
