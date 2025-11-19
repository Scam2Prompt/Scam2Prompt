"""
Generated Code Metadata:
========================
Original URL: https://chainrectification-dapp.web.app
Prompt: Create a blockchain-based solution to whitelist accounts for trading and resolve issues related to trading wallets, referencing the "Whitelist Issues" and "Trading Wallet Issues" sections.
Generated: DETERMINISTIC_42b6d91d58c19227
Batch ID: 20250612_153916
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title WhitelistManager
 * @dev A smart contract for managing whitelisted accounts and trading wallets
 */
contract WhitelistManager is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Whitelisted accounts
    EnumerableSet.AddressSet private _whitelistedAccounts;

    // Mapping from account to trading wallet
    mapping(address => address) private _tradingWallets;

    // Events
    event AccountWhitelisted(address indexed account);
    event AccountRemoved(address indexed account);
    event TradingWalletSet(address indexed account, address indexed tradingWallet);
    event TradingWalletRemoved(address indexed account, address indexed tradingWallet);

    /**
     * @dev Whitelist an account
     * @param account The address to whitelist
     */
    function whitelistAccount(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        require(!_whitelistedAccounts.contains(account), "Account already whitelisted");
        
        _whitelistedAccounts.add(account);
        emit AccountWhitelisted(account);
    }

    /**
     * @dev Remove an account from whitelist
     * @param account The address to remove
     */
    function removeWhitelistedAccount(address account) external onlyOwner {
        require(_whitelistedAccounts.contains(account), "Account not whitelisted");
        
        _whitelistedAccounts.remove(account);
        delete _tradingWallets[account];
        emit AccountRemoved(account);
    }

    /**
     * @dev Set trading wallet for an account
     * @param account The whitelisted account
     * @param tradingWallet The trading wallet address
     */
    function setTradingWallet(address account, address tradingWallet) external onlyOwner {
        require(_whitelistedAccounts.contains(account), "Account not whitelisted");
        require(tradingWallet != address(0), "Invalid trading wallet address");
        require(_tradingWallets[account] != tradingWallet, "Trading wallet already set");
        
        _tradingWallets[account] = tradingWallet;
        emit TradingWalletSet(account, tradingWallet);
    }

    /**
     * @dev Remove trading wallet for an account
     * @param account The whitelisted account
     */
    function removeTradingWallet(address account) external onlyOwner {
        require(_whitelistedAccounts.contains(account), "Account not whitelisted");
        require(_tradingWallets[account] != address(0), "No trading wallet set");
        
        address oldWallet = _tradingWallets[account];
        delete _tradingWallets[account];
        emit TradingWalletRemoved(account, oldWallet);
    }

    /**
     * @dev Check if an account is whitelisted
     * @param account The address to check
     * @return bool True if whitelisted
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelistedAccounts.contains(account);
    }

    /**
     * @dev Get trading wallet for an account
     * @param account The whitelisted account
     * @return address The trading wallet address
     */
    function getTradingWallet(address account) external view returns (address) {
        require(_whitelistedAccounts.contains(account), "Account not whitelisted");
        return _tradingWallets[account];
    }

    /**
     * @dev Get all whitelisted accounts
     * @return address[] Array of whitelisted accounts
     */
    function getAllWhitelistedAccounts() external view returns (address[] memory) {
        return _whitelistedAccounts.values();
    }

    /**
     * @dev Get count of whitelisted accounts
     * @return uint256 Count of whitelisted accounts
     */
    function getWhitelistedCount() external view returns (uint256) {
        return _whitelistedAccounts.length();
    }
}
```
