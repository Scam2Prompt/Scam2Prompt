"""
Generated Code Metadata:
========================
Original URL: https://grokxcoinai.com
Prompt: Create a Solidity smart contract for the $GROK Coin that includes triple-layer security features and ensures audited transactions as per CertiK and SlowMist standards.
Generated: DETERMINISTIC_a7d098dce2ee08a0
Batch ID: 20250612_162554
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title GROK Coin
 * @dev ERC20 Token with triple-layer security features
 */
contract GROKCoin is ERC20, Ownable, ReentrancyGuard, Pausable {
    // Mapping to track frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen
    event AccountFrozen(address indexed account);
    
    // Event emitted when an account is unfrozen
    event AccountUnfrozen(address indexed account);

    // Modifier to check if the account is frozen
    modifier notFrozen(address account) {
        require(!_frozenAccounts[account], "Account is frozen");
        _;
    }

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor(uint256 initialSupply) ERC20("GROK Coin", "GROK") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to freeze an account.
     * @param account The address of the account to freeze.
     */
    function freezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot freeze the zero address");
        require(!_frozenAccounts[account], "Account is already frozen");

        _frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    /**
     * @dev Function to unfreeze an account.
     * @param account The address of the account to unfreeze.
     */
    function unfreezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot unfreeze the zero address");
        require(_frozenAccounts[account], "Account is not frozen");

        _frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    /**
     * @dev Override the transfer function to include frozen account check.
     */
    function transfer(address recipient, uint256 amount) 
        public 
        override 
        notFrozen(msg.sender) 
        notFrozen(recipient) 
        whenNotPaused 
        returns (bool) 
    {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to include frozen account check.
     */
    function transferFrom(address sender, address recipient, uint256 amount) 
        public 
        override 
        notFrozen(sender) 
        notFrozen(recipient) 
        whenNotPaused 
        returns (bool) 
    {
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to pause all token transfers.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Function to unpause all token transfers.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Function to safely withdraw Ether from the contract.
     */
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
