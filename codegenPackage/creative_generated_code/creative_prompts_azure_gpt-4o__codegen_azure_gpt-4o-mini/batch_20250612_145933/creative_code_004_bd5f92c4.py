"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: Provide an example of porting an existing Ethereum-based Solidity project to Reef chain without modifying the code.
Generated: DETERMINISTIC_bd5f92c48975498e
Batch ID: 20250612_145933
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

// Importing OpenZeppelin's ERC20 contract for standard token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MyToken is a simple ERC20 token that can be deployed on both Ethereum and Reef chain
contract MyToken is ERC20, Ownable {
    // Mapping to keep track of frozen accounts
    mapping(address => bool) private frozenAccounts;

    // Event for freezing an account
    event AccountFrozen(address indexed account);
    
    // Event for unfreezing an account
    event AccountUnfrozen(address indexed account);
    
    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply);
    }

    // Function to freeze an account
    function freezeAccount(address account) public onlyOwner {
        require(account != address(0), "Cannot freeze the zero address");
        require(!frozenAccounts[account], "Account is already frozen");
        
        frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    // Function to unfreeze an account
    function unfreezeAccount(address account) public onlyOwner {
        require(account != address(0), "Cannot unfreeze the zero address");
        require(frozenAccounts[account], "Account is not frozen");
        
        frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    // Override the transfer function to prevent frozen accounts from transferring tokens
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        require(!frozenAccounts[msg.sender], "Sender account is frozen");
        require(!frozenAccounts[recipient], "Recipient account is frozen");
        
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to prevent frozen accounts from transferring tokens on behalf of others
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        require(!frozenAccounts[sender], "Sender account is frozen");
        require(!frozenAccounts[recipient], "Recipient account is frozen");
        
        return super.transferFrom(sender, recipient, amount);
    }
}
```
