"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abc-shield.web.app
Prompt: Create a smart contract that verifies wallet ownership and integrates with a backend system to provide Discord access, inspired by the ABC Guard platform.
Generated: DETERMINISTIC_06af3c0de73aed5c
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code for a smart contract and backend integration. The smart contract is written in Solidity, and the backend system is implemented in Node.js (using Express). The contract verifies wallet ownership, while the backend provides Discord access upon verification.

### Solidity Smart Contract

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title WalletOwnershipVerifier
/// @notice This contract allows users to verify ownership of their wallet address.
/// @dev The contract emits an event upon successful signature verification.
contract WalletOwnershipVerifier {
    // Event emitted when a wallet is verified successfully
    event WalletVerified(address indexed walletOwner, string discordId);

    /// @notice Verifies wallet ownership using the provided signature
    /// @param discordId The user's Discord ID
    /// @param signature The signed message proving wallet ownership
    function verifyWalletOwnership(string memory discordId, bytes memory signature) external {
        // Recover the signer from the signature and require it matches msg.sender
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender, discordId));
        bytes32 signedHash = _getEthSignedMessageHash(messageHash);
        address signer = _recoverSigner(signedHash, signature);

        require(signer == msg.sender, "Wallet verification failed: Invalid signer");

        // Emit the event upon successful verification
        emit WalletVerified(msg.sender, discordId);
    }

    /// @dev Generates an Ethereum signed message hash
    /// @param messageHash The original hash
    /// @return The generated hash
    function _getEthSignedMessageHash(bytes32 messageHash) private pure returns (bytes32) {
        return keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash));
    }

    /// @dev Recovers the signer address from a signed hash
    /// @param signedHash The Ethereum signed message hash
    /// @param signature The provided signature
    /// @return The recovered address
    function _recoverSigner(bytes32 signedHash, bytes memory signature) private pure returns (address) {
        (bytes32 r, bytes32 s, uint8 v) = _splitSignature(signature);
        return ecrecover(signedHash, v, r, s);
    }

    /// @dev Splits a signature into its r, s, and v components
    /// @param signature The provided signature
    /// @return r, s, v
    function _splitSignature(bytes memory signature) private pure returns (bytes32 r, bytes32 s, uint8 v) {
        require(signature.length == 65, "Invalid signature length");

        assembly {
            r := mload(add(signature, 32))
            s := mload(add(signature, 64))
            v := byte(0, mload(add(signature, 96)))
        }
    }
}
```

---

### Node.js Backend System

```javascript
const express = require('express');
const Web3 = require('web3');
const bodyParser = require('body-parser');
const { Client } = require('discord.js');

// Initialize Express and Discord client
const app = express();
const discordClient = new Client({ intents: [] });
const web3 = new Web3();

// Middleware for parsing JSON requests
app.use(bodyParser.json());

// Configuration
const DISCORD_BOT_TOKEN = 'your_discord_bot_token';
const DISCORD_ROLE_ID = 'your_discord_role_id';
const DISCORD_SERVER_ID = 'your_discord_server_id';

// Connect Discord bot
discordClient.login(DISCORD_BOT_TOKEN);

discordClient.on('ready', () => {
    console.log(`Discord bot logged in as ${discordClient.user.tag}`);
});

// Endpoint to verify wallet and grant Discord access
app.post('/verify-wallet', async (req, res) => {
    try {
        const { walletAddress, discordId, signature } = req.body;

        if (!walletAddress || !discordId || !signature) {
            return res.status(400).json({ error: 'Missing required fields' });
        }

        // Recreate the signed message
        const message = web3.utils.soliditySha3(walletAddress, discordId);
        const signedMessage = web3.eth.accounts.hashMessage(message);

        // Recover the address from the signature
        const recoveredAddress = web3.eth.accounts.recover(signedMessage, signature);

        if (recoveredAddress !== walletAddress) {
            return res.status(401).json({ error: 'Invalid signature' });
        }

        // Add the user to the Discord role
        const guild = discordClient.guilds.cache.get(DISCORD_SERVER_ID);
        const member = await guild.members.fetch(discordId);

        await member.roles.add(DISCORD_ROLE_ID);

        return res.status(200).json({ message: 'Wallet verified and Discord access granted' });
    } catch (error) {
        console.error('Error processing request:', error);
        return res.status(500).json({ error: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

---

### Notes
- Replace `your_discord_bot_token`, `your_discord_role_id`, and `your_discord_server_id` with real values.
- The smart contract validates wallet ownership using Ethereum's `ecrecover` function.
- The backend integrates with Discord via the Discord.js library to assign roles to verified users.
- Both the smart contract and backend include error handling for invalid inputs.
