"""
Generated Code Metadata:
========================
Original URL: https://wenwen.pages.dev
Prompt: Design a basic smart contract for a token like Wen that can be used on a blockchain platform.
Generated: DETERMINISTIC_6b5feea93c1308e3
Batch ID: 20250622_205553
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BasicToken is a simple ERC20 token contract
contract BasicToken is ERC20, Ownable {
    // Mapping to keep track of frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen or unfrozen
    event FrozenFunds(address target, bool frozen);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to freeze an account, preventing it from transferring tokens
    function freezeAccount(address target, bool freeze) external onlyOwner {
        _frozenAccounts[target] = freeze;
        emit FrozenFunds(target, freeze);
    }

    // Override the _beforeTokenTransfer function to implement freezing logic
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        require(!_frozenAccounts[from], "ERC20: account is frozen");
        super._beforeTokenTransfer(from, to, amount);
    }

    // Function to check if an account is frozen
    function isFrozen(address account) external view returns (bool) {
        return _frozenAccounts[account];
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
