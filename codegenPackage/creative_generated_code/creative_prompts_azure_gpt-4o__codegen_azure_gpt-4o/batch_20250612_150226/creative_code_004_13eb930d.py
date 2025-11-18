"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-guard.web.app
Prompt: Provide an example of a smart contract that verifies wallet ownership and triggers access permissions for a Discord server, inspired by PantherGuard's functionality.
Generated: DETERMINISTIC_13eb930dd72aab5b
Batch ID: 20250612_150226
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
 * @title WalletVerifier
 * @dev A smart contract that verifies wallet ownership and triggers access permissions for a Discord server.
 */
contract WalletVerifier {
    // Event emitted when access is granted
    event AccessGranted(address indexed walletAddress, string discordId);

    // Mapping to store verified wallets and their associated Discord IDs
    mapping(address => string) public verifiedWallets;

    /**
     * @dev Verifies wallet ownership and grants Discord server access.
     * @param discordId The Discord ID associated with the wallet owner.
     */
    function verifyWallet(string memory discordId) external {
        // Ensure the Discord ID is not empty
        require(bytes(discordId).length > 0, "Discord ID cannot be empty");

        // Ensure the wallet has not already been verified
        require(bytes(verifiedWallets[msg.sender]).length == 0, "Wallet already verified");

        // Associate the wallet with the Discord ID
        verifiedWallets[msg.sender] = discordId;

        // Emit the access granted event
        emit AccessGranted(msg.sender, discordId);
    }

    /**
     * @dev Checks if a wallet is verified and returns the associated Discord ID.
     * @param walletAddress The wallet address to check.
     * @return discordId The Discord ID associated with the wallet.
     */
    function getVerifiedWallet(address walletAddress) external view returns (string memory discordId) {
        // Check if the wallet is verified
        require(bytes(verifiedWallets[walletAddress]).length > 0, "Wallet not verified");

        // Return the associated Discord ID
        return verifiedWallets[walletAddress];
    }

    /**
     * @dev Revokes access for a verified wallet. Can only be called by the wallet owner.
     */
    function revokeAccess() external {
        // Ensure the wallet is verified
        require(bytes(verifiedWallets[msg.sender]).length > 0, "Wallet not verified");

        // Remove the wallet from the verification mapping
        delete verifiedWallets[msg.sender];
    }
}
```
