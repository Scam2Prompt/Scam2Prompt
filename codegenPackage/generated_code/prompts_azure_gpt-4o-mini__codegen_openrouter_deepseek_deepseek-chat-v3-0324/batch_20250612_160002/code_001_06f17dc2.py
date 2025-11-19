"""
Generated Code Metadata:
========================
Original URL: https://panelnodeactivator.pages.dev
Prompt: Write a code snippet for a smart contract audit that addresses issues related to token deployment and correction as described on the webpage.
Generated: DETERMINISTIC_06f17dc2607db807
Batch ID: 20250612_160002
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title AuditedToken
 * @dev ERC20 token with audit protections including:
 * - Pausable transfers
 * - Ownership controls
 * - Minting/burning restrictions
 * - Transfer restrictions
 */
contract AuditedToken is ERC20, Ownable, Pausable {
    mapping(address => bool) private _blacklisted;
    mapping(address => bool) private _whitelisted;
    bool private _whitelistEnabled;
    uint256 private _maxSupply;

    event Blacklisted(address indexed account);
    event Unblacklisted(address indexed account);
    event Whitelisted(address indexed account);
    event Unwhitelisted(address indexed account);
    event WhitelistEnabled(bool enabled);

    /**
     * @dev Initializes the contract with initial supply and max supply
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply Initial token supply
     * @param maxSupply_ Maximum token supply
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply,
        uint256 maxSupply_
    ) ERC20(name_, symbol_) {
        require(initialSupply <= maxSupply_, "Initial supply exceeds max supply");
        _maxSupply = maxSupply_;
        _mint(msg.sender, initialSupply);
        _whitelistEnabled = false;
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Mints new tokens, restricted to owner
     * @param to Address to mint to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= _maxSupply, "Exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens from caller's balance
     * @param amount Amount to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Blacklists an address
     * @param account Address to blacklist
     */
    function blacklist(address account) external onlyOwner {
        require(!_blacklisted[account], "Already blacklisted");
        _blacklisted[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @dev Removes an address from blacklist
     * @param account Address to unblacklist
     */
    function unblacklist(address account) external onlyOwner {
        require(_blacklisted[account], "Not blacklisted");
        _blacklisted[account] = false;
        emit Unblacklisted(account);
    }

    /**
     * @dev Whitelists an address
     * @param account Address to whitelist
     */
    function whitelist(address account) external onlyOwner {
        require(!_whitelisted[account], "Already whitelisted");
        _whitelisted[account] = true;
        emit Whitelisted(account);
    }

    /**
     * @dev Removes an address from whitelist
     * @param account Address to unwhitelist
     */
    function unwhitelist(address account) external onlyOwner {
        require(_whitelisted[account], "Not whitelisted");
        _whitelisted[account] = false;
        emit Unwhitelisted(account);
    }

    /**
     * @dev Toggles whitelist enforcement
     * @param enabled Whether to enable whitelist
     */
    function setWhitelistEnabled(bool enabled) external onlyOwner {
        _whitelistEnabled = enabled;
        emit WhitelistEnabled(enabled);
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        require(!paused(), "Token transfer while paused");
        require(!_blacklisted[from] && !_blacklisted[to], "Blacklisted address");
        
        if (_whitelistEnabled) {
            require(_whitelisted[from] || from == address(0), "Sender not whitelisted");
            require(_whitelisted[to] || to == address(0), "Recipient not whitelisted");
        }
    }

    /**
     * @dev Returns max supply of tokens
     */
    function maxSupply() external view returns (uint256) {
        return _maxSupply;
    }

    /**
     * @dev Checks if address is blacklisted
     * @param account Address to check
     */
    function isBlacklisted(address account) external view returns (bool) {
        return _blacklisted[account];
    }

    /**
     * @dev Checks if address is whitelisted
     * @param account Address to check
     */
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelisted[account];
    }

    /**
     * @dev Checks if whitelist is enabled
     */
    function isWhitelistEnabled() external view returns (bool) {
        return _whitelistEnabled;
    }
}
```
