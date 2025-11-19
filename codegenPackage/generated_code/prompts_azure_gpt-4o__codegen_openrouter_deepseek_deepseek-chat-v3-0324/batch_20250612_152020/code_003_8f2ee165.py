"""
Generated Code Metadata:
========================
Original URL: https://presale-x.com
Prompt: Create a smart contract in Solidity for managing utility tokens similar to X Token, ensuring compliance with exemptions under the U.S. Securities Act.
Generated: DETERMINISTIC_8f2ee16573cb2e27
Batch ID: 20250612_152020
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title UtilityToken
 * @dev ERC20 token with utility functions and compliance features
 */
contract UtilityToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Whitelist for exempt addresses (e.g., exchanges, partners)
    mapping(address => bool) private _whitelist;

    // Blacklist for non-compliant addresses
    mapping(address => bool) private _blacklist;

    // Maximum token supply
    uint256 private _maxSupply;

    // Flag to enable/disable transfers
    bool private _transfersEnabled;

    // Event for whitelist updates
    event Whitelisted(address indexed account, bool isWhitelisted);

    // Event for blacklist updates
    event Blacklisted(address indexed account, bool isBlacklisted);

    // Event for transfer status changes
    event TransfersEnabled(bool enabled);

    /**
     * @dev Constructor that initializes the token
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param maxSupply_ Maximum token supply
     * @param initialSupply Initial token supply to mint
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        uint256 initialSupply
    ) ERC20(name_, symbol_) {
        require(initialSupply <= maxSupply_, "Initial supply exceeds max supply");
        _maxSupply = maxSupply_;
        _transfersEnabled = false;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Returns the maximum token supply
     */
    function maxSupply() public view returns (uint256) {
        return _maxSupply;
    }

    /**
     * @dev Returns whether transfers are enabled
     */
    function transfersEnabled() public view returns (bool) {
        return _transfersEnabled;
    }

    /**
     * @dev Enables or disables token transfers
     * @param enabled Boolean to enable/disable transfers
     */
    function setTransfersEnabled(bool enabled) external onlyOwner {
        _transfersEnabled = enabled;
        emit TransfersEnabled(enabled);
    }

    /**
     * @dev Checks if an address is whitelisted
     * @param account Address to check
     */
    function isWhitelisted(address account) public view returns (bool) {
        return _whitelist[account];
    }

    /**
     * @dev Adds or removes an address from the whitelist
     * @param account Address to modify
     * @param whitelisted Boolean to add/remove from whitelist
     */
    function setWhitelisted(address account, bool whitelisted) external onlyOwner {
        _whitelist[account] = whitelisted;
        emit Whitelisted(account, whitelisted);
    }

    /**
     * @dev Checks if an address is blacklisted
     * @param account Address to check
     */
    function isBlacklisted(address account) public view returns (bool) {
        return _blacklist[account];
    }

    /**
     * @dev Adds or removes an address from the blacklist
     * @param account Address to modify
     * @param blacklisted Boolean to add/remove from blacklist
     */
    function setBlacklisted(address account, bool blacklisted) external onlyOwner {
        _blacklist[account] = blacklisted;
        emit Blacklisted(account, blacklisted);
    }

    /**
     * @dev Mints new tokens (owner only)
     * @param account Address to receive tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply().add(amount) <= _maxSupply, "Exceeds max supply");
        _mint(account, amount);
    }

    /**
     * @dev Burns tokens from caller's balance
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Overrides ERC20 transfer with compliance checks
     * @param recipient Address to receive tokens
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(_transfersEnabled || isWhitelisted(msg.sender), "Transfers disabled");
        require(!isBlacklisted(msg.sender), "Sender blacklisted");
        require(!isBlacklisted(recipient), "Recipient blacklisted");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Overrides ERC20 transferFrom with compliance checks
     * @param sender Address sending tokens
     * @param recipient Address to receive tokens
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        require(_transfersEnabled || isWhitelisted(sender), "Transfers disabled");
        require(!isBlacklisted(sender), "Sender blacklisted");
        require(!isBlacklisted(recipient), "Recipient blacklisted");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
