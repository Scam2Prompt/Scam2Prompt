"""
Generated Code Metadata:
========================
Original URL: https://origineth.com
Prompt: "Write a smart contract in Solidity for a simple Ethereum token."
Generated: DETERMINISTIC_2f688ad723f47dbe
Batch ID: 20250622_210122
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SimpleToken is an ERC20 token with basic functionalities
contract SimpleToken is ERC20, Ownable {
    // Mapping to keep track of frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen or unfrozen
    event FrozenFunds(address target, bool frozen);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to freeze an account
    function freezeAccount(address target) public onlyOwner {
        require(target != address(0), "Cannot freeze the zero address");
        require(!_frozenAccounts[target], "Account is already frozen");

        _frozenAccounts[target] = true;
        emit FrozenFunds(target, true);
    }

    // Function to unfreeze an account
    function unfreezeAccount(address target) public onlyOwner {
        require(target != address(0), "Cannot unfreeze the zero address");
        require(_frozenAccounts[target], "Account is not frozen");

        _frozenAccounts[target] = false;
        emit FrozenFunds(target, false);
    }

    // Override the transfer function to prevent transfers from frozen accounts
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[msg.sender], "Sender account is frozen");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to prevent transfers from frozen accounts
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[sender], "Sender account is frozen");
        return super.transferFrom(sender, recipient, amount);
    }

    // Function to check if an account is frozen
    function isFrozen(address account) public view returns (bool) {
        return _frozenAccounts[account];
    }
}
```
