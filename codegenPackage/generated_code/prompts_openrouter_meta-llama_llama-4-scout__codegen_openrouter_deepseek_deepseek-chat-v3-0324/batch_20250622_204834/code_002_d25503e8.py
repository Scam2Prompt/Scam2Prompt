"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Develop a simple smart contract in Solidity for a multichain token like $FROP, ensuring transparency and security.
Generated: DETERMINISTIC_d25503e8db528989
Batch ID: 20250622_204834
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
 * @title MultichainToken
 * @dev ERC20 token with multichain support, ownership control, and pausable functionality
 */
contract MultichainToken is ERC20, Ownable, Pausable {
    mapping(address => bool) private _blacklisted;
    mapping(address => bool) private _minters;

    event Blacklisted(address indexed account);
    event Unblacklisted(address indexed account);
    event MinterAdded(address indexed account);
    event MinterRemoved(address indexed account);

    /**
     * @dev Constructor that initializes the token with initial supply
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param owner Address of the contract owner
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address owner
    ) ERC20(name, symbol) {
        _transferOwnership(owner);
        _mint(owner, initialSupply);
    }

    /**
     * @dev Modifier to check if caller is a minter
     */
    modifier onlyMinter() {
        require(_minters[_msgSender()], "MultichainToken: caller is not a minter");
        _;
    }

    /**
     * @dev Mint new tokens (only by minter)
     * @param to Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyMinter whenNotPaused {
        _mint(to, amount);
    }

    /**
     * @dev Add a minter address
     * @param account Address to be added as minter
     */
    function addMinter(address account) external onlyOwner {
        require(!_minters[account], "MultichainToken: account is already minter");
        _minters[account] = true;
        emit MinterAdded(account);
    }

    /**
     * @dev Remove a minter address
     * @param account Address to be removed from minters
     */
    function removeMinter(address account) external onlyOwner {
        require(_minters[account], "MultichainToken: account is not minter");
        _minters[account] = false;
        emit MinterRemoved(account);
    }

    /**
     * @dev Check if address is minter
     * @param account Address to check
     * @return bool True if address is minter
     */
    function isMinter(address account) external view returns (bool) {
        return _minters[account];
    }

    /**
     * @dev Blacklist an address
     * @param account Address to blacklist
     */
    function blacklist(address account) external onlyOwner {
        require(!_blacklisted[account], "MultichainToken: account is already blacklisted");
        _blacklisted[account] = true;
        emit Blacklisted(account);
    }

    /**
     * @dev Remove address from blacklist
     * @param account Address to unblacklist
     */
    function unblacklist(address account) external onlyOwner {
        require(_blacklisted[account], "MultichainToken: account is not blacklisted");
        _blacklisted[account] = false;
        emit Unblacklisted(account);
    }

    /**
     * @dev Check if address is blacklisted
     * @param account Address to check
     * @return bool True if address is blacklisted
     */
    function isBlacklisted(address account) external view returns (bool) {
        return _blacklisted[account];
    }

    /**
     * @dev Pause token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
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

        require(!_blacklisted[from], "MultichainToken: sender is blacklisted");
        require(!_blacklisted[to], "MultichainToken: recipient is blacklisted");
        require(!paused(), "MultichainToken: token transfer while paused");
    }
}
```
