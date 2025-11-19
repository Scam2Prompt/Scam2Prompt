"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Write a smart contract for tokenization of Real World Assets (RWA) using Solidity, incorporating security best practices as described by Quecko's blockchain development services.
Generated: DETERMINISTIC_7f70a87be23ae5ae
Batch ID: 20250612_154029
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";

/**
 * @title RWAToken
 * @dev Token contract for Real World Asset (RWA) tokenization
 * Implements ERC20 with additional features:
 * - Ownable for administration
 * - Pausable for emergency stops
 * - Burnable for token destruction
 * - Snapshot for historical balances
 * - Permit for gasless approvals
 */
contract RWAToken is ERC20, Ownable, Pausable, ERC20Burnable, ERC20Snapshot, ERC20Permit {
    // Mapping to track frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when account is frozen/unfrozen
    event AccountFrozen(address indexed account, bool frozen);

    /**
     * @dev Initializes the contract
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply Initial token supply
     * @param owner Address of the contract owner
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply,
        address owner
    ) ERC20(name_, symbol_) ERC20Permit(name_) {
        require(owner != address(0), "RWAToken: owner is zero address");
        _mint(owner, initialSupply);
        transferOwnership(owner);
    }

    /**
     * @dev Creates a new token snapshot
     * Only callable by owner
     */
    function snapshot() public onlyOwner {
        _snapshot();
    }

    /**
     * @dev Pauses all token transfers
     * Only callable by owner
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     * Only callable by owner
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Freezes or unfreezes an account
     * @param account Address to freeze/unfreeze
     * @param frozen Whether to freeze or unfreeze
     * Only callable by owner
     */
    function freezeAccount(address account, bool frozen) public onlyOwner {
        require(account != address(0), "RWAToken: account is zero address");
        _frozenAccounts[account] = frozen;
        emit AccountFrozen(account, frozen);
    }

    /**
     * @dev Checks if an account is frozen
     * @param account Address to check
     * @return bool Whether the account is frozen
     */
    function isFrozen(address account) public view returns (bool) {
        return _frozenAccounts[account];
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        require(!_frozenAccounts[from], "RWAToken: sender account frozen");
        require(!_frozenAccounts[to], "RWAToken: recipient account frozen");
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Destroys `amount` tokens from the caller
     * @param amount Amount to burn
     * Overrides burn function to include whenNotPaused modifier
     */
    function burn(uint256 amount) public override whenNotPaused {
        super.burn(amount);
    }

    /**
     * @dev Destroys `amount` tokens from `account`, deducting from the caller's allowance
     * @param account Account to burn from
     * @param amount Amount to burn
     * Overrides burnFrom function to include whenNotPaused modifier
     */
    function burnFrom(address account, uint256 amount) public override whenNotPaused {
        super.burnFrom(account, amount);
    }
}
```
