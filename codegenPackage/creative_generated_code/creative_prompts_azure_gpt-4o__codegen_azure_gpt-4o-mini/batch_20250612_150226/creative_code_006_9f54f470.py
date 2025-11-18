"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://islamic-guard.web.app
Prompt: Create a smart contract in Solidity that verifies wallet ownership and triggers access permissions for a Discord server, similar to IslamicGuard's use case.
Generated: DETERMINISTIC_9f54f4708d2d76ec
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

import "@openzeppelin/contracts/access/Ownable.sol";

contract DiscordAccessManager is Ownable {
    // Mapping of wallet addresses to their access status
    mapping(address => bool) private _accessGranted;

    // Event emitted when access is granted or revoked
    event AccessUpdated(address indexed wallet, bool access);

    /**
     * @dev Grants access to the specified wallet address.
     * @param wallet The address of the wallet to grant access.
     */
    function grantAccess(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address: zero address");
        require(!_accessGranted[wallet], "Access already granted");

        _accessGranted[wallet] = true;
        emit AccessUpdated(wallet, true);
    }

    /**
     * @dev Revokes access from the specified wallet address.
     * @param wallet The address of the wallet to revoke access.
     */
    function revokeAccess(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address: zero address");
        require(_accessGranted[wallet], "Access not granted");

        _accessGranted[wallet] = false;
        emit AccessUpdated(wallet, false);
    }

    /**
     * @dev Checks if a wallet address has access.
     * @param wallet The address of the wallet to check.
     * @return True if the wallet has access, false otherwise.
     */
    function hasAccess(address wallet) external view returns (bool) {
        require(wallet != address(0), "Invalid address: zero address");
        return _accessGranted[wallet];
    }

    /**
     * @dev Withdraws any Ether in the contract to the owner's address.
     */
    function withdraw() external onlyOwner {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
