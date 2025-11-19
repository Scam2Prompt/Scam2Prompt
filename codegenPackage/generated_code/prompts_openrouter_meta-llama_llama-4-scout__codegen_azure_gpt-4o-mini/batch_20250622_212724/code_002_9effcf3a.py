"""
Generated Code Metadata:
========================
Original URL: https://popofrog-claim.pages.dev
Prompt: Generate a smart contract code in Solidity for the $FROP token, ensuring transparency and security features as mentioned in the project's whitepaper.
Generated: DETERMINISTIC_9effcf3a0693a76c
Batch ID: 20250622_212724
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

// Importing OpenZeppelin's ERC20 implementation for security and standard compliance
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// $FROP Token Contract
contract FROPToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track balances of frozen accounts
    mapping(address => bool) private _frozenAccounts;

    // Event emitted when an account is frozen
    event AccountFrozen(address indexed account);
    
    // Event emitted when an account is unfrozen
    event AccountUnfrozen(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("FROP Token", "$FROP") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Function to freeze an account, preventing it from transferring tokens
    function freezeAccount(address account) external onlyOwner {
        require(!_frozenAccounts[account], "Account is already frozen");
        _frozenAccounts[account] = true;
        emit AccountFrozen(account);
    }

    // Function to unfreeze an account, allowing it to transfer tokens again
    function unfreezeAccount(address account) external onlyOwner {
        require(_frozenAccounts[account], "Account is not frozen");
        _frozenAccounts[account] = false;
        emit AccountUnfrozen(account);
    }

    // Override the transfer function to include frozen account checks
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[msg.sender], "Sender account is frozen");
        require(!_frozenAccounts[recipient], "Recipient account is frozen");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to include frozen account checks
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(!_frozenAccounts[sender], "Sender account is frozen");
        require(!_frozenAccounts[recipient], "Recipient account is frozen");
        return super.transferFrom(sender, recipient, amount);
    }

    // Function to check if an account is frozen
    function isAccountFrozen(address account) external view returns (bool) {
        return _frozenAccounts[account];
    }
}
```
