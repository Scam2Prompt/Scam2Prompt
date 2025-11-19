"""
Generated Code Metadata:
========================
Original URL: https://panther-guard.web.app
Prompt: Provide an example of a smart contract that verifies wallet ownership and triggers access permissions for a Discord server, inspired by PantherGuard's functionality.
Generated: DETERMINISTIC_13eb930dd72aab5b
Batch ID: 20250612_150226
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

contract DiscordAccessControl is Ownable {
    using ECDSA for bytes32;

    // Mapping from Discord user ID to Ethereum address
    mapping(string => address) public discordToWallet;
    
    // Mapping from Ethereum address to Discord user ID
    mapping(address => string) public walletToDiscord;
    
    // Nonce for signature verification to prevent replay attacks
    mapping(address => uint256) public nonces;
    
    // Event emitted when a new verification is completed
    event VerificationCompleted(
        address indexed walletAddress,
        string discordId,
        uint256 timestamp
    );

    /**
     * @dev Verifies wallet ownership and links it to a Discord ID
     * @param discordId The Discord user ID to verify
     * @param signature The signature proving wallet ownership
     */
    function verifyWalletOwnership(
        string memory discordId,
        bytes memory signature
    ) external {
        require(bytes(discordId).length > 0, "Discord ID cannot be empty");
        
        // Reconstruct the signed message
        bytes32 messageHash = keccak256(
            abi.encodePacked(
                "\x19Ethereum Signed Message:\n32",
                keccak256(abi.encodePacked(msg.sender, discordId, nonces[msg.sender]))
            )
        );
        
        address signer = messageHash.recover(signature);
        require(signer == msg.sender, "Invalid signature");
        
        // Clear any previous mappings
        if (bytes(walletToDiscord[msg.sender]).length > 0) {
            delete discordToWallet[walletToDiscord[msg.sender]];
        }
        if (discordToWallet[discordId] != address(0)) {
            delete walletToDiscord[discordToWallet[discordId]];
        }
        
        // Create new mappings
        discordToWallet[discordId] = msg.sender;
        walletToDiscord[msg.sender] = discordId;
        
        // Increment nonce to prevent replay attacks
        nonces[msg.sender]++;
        
        emit VerificationCompleted(msg.sender, discordId, block.timestamp);
    }

    /**
     * @dev Checks if a Discord ID is verified with a wallet
     * @param discordId The Discord user ID to check
     * @return bool True if verified, false otherwise
     */
    function isVerified(string memory discordId) public view returns (bool) {
        return discordToWallet[discordId] != address(0);
    }

    /**
     * @dev Gets the Discord ID for a wallet address
     * @param walletAddress The wallet address to check
     * @return string The associated Discord ID
     */
    function getDiscordId(address walletAddress) public view returns (string memory) {
        return walletToDiscord[walletAddress];
    }

    /**
     * @dev Admin function to remove a verification (for moderation purposes)
     * @param discordId The Discord ID to unverify
     */
    function adminRemoveVerification(string memory discordId) external onlyOwner {
        address walletAddress = discordToWallet[discordId];
        require(walletAddress != address(0), "No verification exists for this ID");
        
        delete discordToWallet[discordId];
        delete walletToDiscord[walletAddress];
    }
}
```
