"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentrailzedprotocoll.pages.dev
Prompt: Develop a tool to whitelist wallets for trading coins/tokens using the Decentralized Dapp Loading protocol. Ensure the account is marked as a trusted payment source.
Generated: DETERMINISTIC_c5afb2b71adfe8af
Batch ID: 20250612_154016
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

// A contract to manage whitelisting of wallets for trading tokens
contract WalletWhitelister is Ownable {
    // Mapping to track whitelisted wallets
    mapping(address => bool) private whitelistedWallets;

    // Event emitted when a wallet is whitelisted
    event WalletWhitelisted(address indexed wallet);
    
    // Event emitted when a wallet is removed from the whitelist
    event WalletRemoved(address indexed wallet);

    /**
     * @dev Modifier to check if the wallet is whitelisted
     */
    modifier onlyWhitelisted() {
        require(whitelistedWallets[msg.sender], "Wallet is not whitelisted");
        _;
    }

    /**
     * @dev Function to whitelist a wallet
     * @param wallet The address of the wallet to whitelist
     */
    function whitelistWallet(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address");
        require(!whitelistedWallets[wallet], "Wallet already whitelisted");

        whitelistedWallets[wallet] = true;
        emit WalletWhitelisted(wallet);
    }

    /**
     * @dev Function to remove a wallet from the whitelist
     * @param wallet The address of the wallet to remove
     */
    function removeWallet(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address");
        require(whitelistedWallets[wallet], "Wallet not whitelisted");

        delete whitelistedWallets[wallet];
        emit WalletRemoved(wallet);
    }

    /**
     * @dev Function to check if a wallet is whitelisted
     * @param wallet The address of the wallet to check
     * @return bool indicating whether the wallet is whitelisted
     */
    function isWhitelisted(address wallet) external view returns (bool) {
        return whitelistedWallets[wallet];
    }

    /**
     * @dev Function to get the owner of the contract
     * @return address of the contract owner
     */
    function getOwner() external view returns (address) {
        return owner();
    }
}
```
