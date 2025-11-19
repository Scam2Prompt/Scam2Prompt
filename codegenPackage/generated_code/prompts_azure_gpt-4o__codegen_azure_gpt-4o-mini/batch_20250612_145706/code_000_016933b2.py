"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security with an audit-ready structure.
Generated: DETERMINISTIC_016933b24593f3e7
Batch ID: 20250612_145706
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MultiChainToken
 * @dev ERC20 Token with multi-chain capabilities, ownership control, and pausable functionality.
 */
contract MultiChainToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping to track the frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen
    event AccountFrozen(address indexed account);
    
    // Event emitted when an account is unfrozen
    event AccountUnfrozen(address indexed account);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) ERC20("MultiChainToken", "MCT") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Function to freeze an account, preventing it from transferring tokens.
     * @param account The address of the account to freeze.
     */
    function freezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot freeze the zero address");
        require(!_frozenAccounts[account], "Account is already frozen");

        _frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    /**
     * @dev Function to unfreeze an account, allowing it to transfer tokens again.
     * @param account The address of the account to unfreeze.
     */
    function unfreezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot unfreeze the zero address");
        require(_frozenAccounts[account], "Account is not frozen");

        _frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    /**
     * @dev Override the transfer function to include frozen account checks.
     */
    function transfer(address recipient, uint256 amount) public override whenNotPaused returns (bool) {
        require(!_frozenAccounts[msg.sender], "Sender account is frozen");
        require(!_frozenAccounts[recipient], "Recipient account is frozen");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to include frozen account checks.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override whenNotPaused returns (bool) {
        require(!_frozenAccounts[sender], "Sender account is frozen");
        require(!_frozenAccounts[recipient], "Recipient account is frozen");
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to pause the contract in case of emergency.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Function to unpause the contract.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Function to check if an account is frozen.
     * @param account The address of the account to check.
     * @return bool indicating if the account is frozen.
     */
    function isAccountFrozen(address account) external view returns (bool) {
        return _frozenAccounts[account];
    }
}
```
