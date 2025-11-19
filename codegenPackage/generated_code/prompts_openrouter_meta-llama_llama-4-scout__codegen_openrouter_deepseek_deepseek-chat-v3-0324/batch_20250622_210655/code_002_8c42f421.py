"""
Generated Code Metadata:
========================
Original URL: https://registration-merlinstarter.pages.dev
Prompt: Generate a smart contract code snippet in Solidity to create a token with a similar structure to $MP, $M-BTC, $VOYA, or $HUHU on the Merlin Chain blockchain.
Generated: DETERMINISTIC_8c42f4214b13d5e5
Batch ID: 20250622_210655
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";

contract MerlinToken is ERC20, Ownable, ERC20Burnable, ERC20Pausable {
    uint256 private constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    
    // Mapping to track blacklisted addresses
    mapping(address => bool) private _blacklisted;

    event Blacklisted(address indexed account);
    event Unblacklisted(address indexed account);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        require(initialSupply <= MAX_SUPPLY, "Initial supply exceeds max supply");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Pauses all token transfers.
     * Can only be called by the owner.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers.
     * Can only be called by the owner.
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Adds an address to the blacklist.
     * Can only be called by the owner.
     */
    function blacklist(address account) public onlyOwner {
        require(!_blacklisted[account], "Account is already blacklisted");
        _blacklisted[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @dev Removes an address from the blacklist.
     * Can only be called by the owner.
     */
    function unblacklist(address account) public onlyOwner {
        require(_blacklisted[account], "Account is not blacklisted");
        _blacklisted[account] = false;
        emit Unblacklisted(account);
    }

    /**
     * @dev Checks if an address is blacklisted.
     */
    function isBlacklisted(address account) public view returns (bool) {
        return _blacklisted[account];
    }

    /**
     * @dev Hook that is called before any transfer of tokens.
     * Checks if the sender or recipient is blacklisted and if the contract is paused.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override(ERC20, ERC20Pausable) {
        require(!_blacklisted[from], "Sender is blacklisted");
        require(!_blacklisted[to], "Recipient is blacklisted");
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Mints new tokens.
     * Can only be called by the owner.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting would exceed max supply");
        _mint(to, amount);
    }
}
```
