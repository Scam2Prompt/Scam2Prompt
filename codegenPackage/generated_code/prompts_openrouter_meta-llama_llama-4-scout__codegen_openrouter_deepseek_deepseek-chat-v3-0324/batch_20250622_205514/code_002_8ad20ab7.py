"""
Generated Code Metadata:
========================
Original URL: https://pepe2coin.site
Prompt: Generate a Solidity smart contract for creating and managing Pepe2Coin tokens on the Ethereum blockchain.
Generated: DETERMINISTIC_8ad20ab7c315a7ce
Batch ID: 20250622_205514
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract Pepe2Coin is ERC20, Ownable, ERC20Burnable, ERC20Snapshot, Pausable {
    // Token details
    string private constant _NAME = "Pepe2Coin";
    string private constant _SYMBOL = "PEPE2";
    uint256 private constant _INITIAL_SUPPLY = 1000000 * 10**18; // 1 million tokens with 18 decimals

    // Mapping to track blacklisted addresses
    mapping(address => bool) private _blacklisted;

    // Events
    event Blacklisted(address indexed account);
    event Unblacklisted(address indexed account);

    constructor() ERC20(_NAME, _SYMBOL) {
        _mint(msg.sender, _INITIAL_SUPPLY);
    }

    /**
     * @dev Creates a new snapshot ID
     */
    function snapshot() public onlyOwner {
        _snapshot();
    }

    /**
     * @dev Pauses all token transfers
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Blacklists an address, preventing it from sending/receiving tokens
     * @param account The address to blacklist
     */
    function blacklist(address account) public onlyOwner {
        require(!_blacklisted[account], "Pepe2Coin: Address already blacklisted");
        _blacklisted[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @dev Removes an address from the blacklist
     * @param account The address to unblacklist
     */
    function unblacklist(address account) public onlyOwner {
        require(_blacklisted[account], "Pepe2Coin: Address not blacklisted");
        _blacklisted[account] = false;
        emit Unblacklisted(account);
    }

    /**
     * @dev Checks if an address is blacklisted
     * @param account The address to check
     * @return bool True if blacklisted, false otherwise
     */
    function isBlacklisted(address account) public view returns (bool) {
        return _blacklisted[account];
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        require(!_blacklisted[from], "Pepe2Coin: Sender is blacklisted");
        require(!_blacklisted[to], "Pepe2Coin: Recipient is blacklisted");
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Mints new tokens (only owner can call)
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
```
