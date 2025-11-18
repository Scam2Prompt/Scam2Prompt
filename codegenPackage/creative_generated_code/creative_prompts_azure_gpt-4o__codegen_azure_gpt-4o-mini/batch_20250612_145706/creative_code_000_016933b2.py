"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security with an audit-ready structure.
Generated: DETERMINISTIC_016933b24593f3e7
Batch ID: 20250612_145706
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

// Importing OpenZeppelin Contracts for ERC20 standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title MultiChainToken
 * @dev Implementation of a multi-chain ERC20 token with transparency and security features
 */
contract MultiChainToken is ERC20, Ownable, Pausable {
    // Mapping to track frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen
    event FrozenAccount(address indexed target, bool frozen);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens of a specified initial supply
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Function to pause contract operations in case of emergency
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Function to unpause contract operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Function to freeze an account, preventing it from transferring tokens
     * @param target The address of the account to freeze
     * @param freeze true to freeze, false to unfreeze
     */
    function freezeAccount(address target, bool freeze) external onlyOwner {
        _frozenAccounts[target] = freeze;
        emit FrozenAccount(target, freeze);
    }

    /**
     * @dev Override _beforeTokenTransfer to prevent transfers to or from frozen accounts
     * @param from The address sending the tokens
     * @param to The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal whenNotPaused override {
        require(!_frozenAccounts[from], "Sender account is frozen");
        require(!_frozenAccounts[to], "Recipient account is frozen");
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Function to retrieve the frozen status of an account
     * @param account The address of the account to check
     * @return bool indicating whether the account is frozen
     */
    function isFrozen(address account) external view returns (bool) {
        return _frozenAccounts[account];
    }
}
```
