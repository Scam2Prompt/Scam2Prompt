"""
Generated Code Metadata:
========================
Original URL: https://popofrog-6s6.pages.dev
Prompt: Develop a simple smart contract in Solidity for a multichain token like $FROP, ensuring transparency and security.
Generated: DETERMINISTIC_d25503e8db528989
Batch ID: 20250622_205919
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

// Importing OpenZeppelin's ERC20 implementation for secure token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MultichainToken is a simple ERC20 token contract with ownership control
contract MultichainToken is ERC20, Ownable {
    // Mapping to track frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen or unfrozen
    event AccountFrozen(address indexed account);
    event AccountUnfrozen(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to freeze an account, preventing it from transferring tokens
    function freezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot freeze the zero address");
        require(!_frozenAccounts[account], "Account is already frozen");

        _frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    // Function to unfreeze an account, allowing it to transfer tokens again
    function unfreezeAccount(address account) external onlyOwner {
        require(account != address(0), "Cannot unfreeze the zero address");
        require(_frozenAccounts[account], "Account is not frozen");

        _frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    // Override the _beforeTokenTransfer hook to implement account freezing logic
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(!_frozenAccounts[from], "Transfer from frozen account");
        require(!_frozenAccounts[to], "Transfer to frozen account");
    }

    // Function to check if an account is frozen
    function isAccountFrozen(address account) external view returns (bool) {
        return _frozenAccounts[account];
    }
}
```
