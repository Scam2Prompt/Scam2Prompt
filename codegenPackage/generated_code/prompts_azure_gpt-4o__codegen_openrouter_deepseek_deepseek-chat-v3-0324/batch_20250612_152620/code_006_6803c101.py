"""
Generated Code Metadata:
========================
Original URL: https://mimicguard.web.app
Prompt: Write a smart contract that verifies wallet ownership and integrates with a web app for Discord access control, inspired by MimicGuard.
Generated: DETERMINISTIC_6803c10195a4b005
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/utils/cryptography/draft-EIP712.sol";

contract DiscordAccessControl is Ownable, EIP712 {
    using ECDSA for bytes32;

    // Domain separator for EIP-712
    string private constant SIGNING_DOMAIN = "DiscordAccessControl";
    string private constant SIGNATURE_VERSION = "1";

    // Mapping from Discord ID to Ethereum address
    mapping(string => address) public discordToAddress;
    
    // Mapping from Ethereum address to Discord ID
    mapping(address => string) public addressToDiscord;

    // Nonce for each address to prevent replay attacks
    mapping(address => uint256) public nonces;

    // Events
    event WalletLinked(string discordId, address walletAddress);
    event WalletUnlinked(string discordId, address walletAddress);

    constructor() EIP712(SIGNING_DOMAIN, SIGNATURE_VERSION) {}

    /**
     * @dev Links a Discord ID to an Ethereum address
     * @param discordId The Discord ID to link
     * @param signature The signature proving wallet ownership
     */
    function linkWallet(string memory discordId, bytes memory signature) external {
        require(bytes(discordId).length > 0, "Invalid Discord ID");
        require(discordToAddress[discordId] == address(0), "Discord ID already linked");

        // Recover the signer from the signature
        bytes32 digest = _hashTypedDataV4(
            keccak256(abi.encode(
                keccak256("LinkWallet(string discordId,uint256 nonce)"),
                keccak256(bytes(discordId)),
                nonces[msg.sender]
            ))
        );
        address signer = digest.recover(signature);
        require(signer == msg.sender, "Invalid signature");

        // Update mappings
        discordToAddress[discordId] = msg.sender;
        addressToDiscord[msg.sender] = discordId;
        nonces[msg.sender]++;

        emit WalletLinked(discordId, msg.sender);
    }

    /**
     * @dev Unlinks a Discord ID from an Ethereum address
     * @param discordId The Discord ID to unlink
     */
    function unlinkWallet(string memory discordId) external {
        require(discordToAddress[discordId] == msg.sender, "Not the linked wallet");

        // Clear mappings
        delete addressToDiscord[msg.sender];
        delete discordToAddress[discordId];

        emit WalletUnlinked(discordId, msg.sender);
    }

    /**
     * @dev Verifies if a Discord ID is linked to a specific address
     * @param discordId The Discord ID to verify
     * @param walletAddress The address to verify against
     * @return bool True if linked, false otherwise
     */
    function verifyWallet(string memory discordId, address walletAddress) external view returns (bool) {
        return discordToAddress[discordId] == walletAddress;
    }

    /**
     * @dev Returns the Discord ID linked to a wallet address
     * @param walletAddress The address to query
     * @return string The linked Discord ID
     */
    function getDiscordId(address walletAddress) external view returns (string memory) {
        return addressToDiscord[walletAddress];
    }

    /**
     * @dev Returns the wallet address linked to a Discord ID
     * @param discordId The Discord ID to query
     * @return address The linked wallet address
     */
    function getWalletAddress(string memory discordId) external view returns (address) {
        return discordToAddress[discordId];
    }

    /**
     * @dev Admin function to force unlink a Discord ID
     * @param discordId The Discord ID to unlink
     */
    function adminUnlinkWallet(string memory discordId) external onlyOwner {
        address walletAddress = discordToAddress[discordId];
        require(walletAddress != address(0), "Discord ID not linked");

        delete addressToDiscord[walletAddress];
        delete discordToAddress[discordId];

        emit WalletUnlinked(discordId, walletAddress);
    }
}
```
