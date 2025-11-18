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

// Importing the OpenZeppelin Ownable contract for ownership functionalities
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with a Discord bot API (stubbed for this example)
interface IDiscordBot {
    function grantAccess(address user) external;
    function revokeAccess(address user) external;
}

// The ERC721 token that users will mint to gain access to the Discord server
contract AccessToken is Ownable {
    // Mapping to track wallet ownership of access tokens
    mapping(address => bool) public hasAccess;

    // Event emitted when access is granted
    event AccessGranted(address indexed user);
    // Event emitted when access is revoked
    event AccessRevoked(address indexed user);

    // Reference to the Discord bot for permission management
    IDiscordBot public discordBot;

    // Constructor to initialize the Discord bot address
    constructor(address _discordBotAddress) {
        discordBot = IDiscordBot(_discordBotAddress);
    }

    // Function to grant access to the Discord server
    function grantAccess(address user) external onlyOwner {
        require(!hasAccess[user], "User already has access");

        // Grant access in the smart contract
        hasAccess[user] = true;

        // Grant access through the Discord bot
        discordBot.grantAccess(user);

        emit AccessGranted(user);
    }

    // Function to revoke access to the Discord server
    function revokeAccess(address user) external onlyOwner {
        require(hasAccess[user], "User does not have access");

        // Revoke access in the smart contract
        hasAccess[user] = false;

        // Revoke access through the Discord bot
        discordBot.revokeAccess(user);

        emit AccessRevoked(user);
    }

    // Function to check if a user has access
    function checkAccess(address user) external view returns (bool) {
        return hasAccess[user];
    }
}
```
