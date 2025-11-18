"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.de
Prompt: Generate a Solidity smart contract example optimized for deployment on the Arbitrum layer-2 network.
Generated: DETERMINISTIC_1e213df794757f88
Batch ID: 20250612_150342
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

// Importing OpenZeppelin's ERC20 contract for creating a token.
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple ERC20 token contract
contract MyToken is ERC20, Ownable {
    // Mapping to keep track of frozen accounts
    mapping(address => bool) private frozenAccounts;

    // Event to log freezing of accounts
    event AccountFrozen(address indexed target);
    // Event to log unfreezing of accounts
    event AccountUnfrozen(address indexed target);

    // Constructor to set the name and symbol of the token
    constructor() ERC20("MyToken", "MTK") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Modifier to restrict functions to non-frozen accounts
    modifier notFrozen(address account) {
        require(!frozenAccounts[account], "Account is frozen");
        _;
    }

    // Function to freeze an account, callable only by the owner
    function freezeAccount(address target) external onlyOwner {
        require(target != address(0), "Cannot freeze zero address");
        require(!frozenAccounts[target], "Account already frozen");

        frozenAccounts[target] = true;
        emit AccountFrozen(target);
    }

    // Function to unfreeze an account, callable only by the owner
    function unfreezeAccount(address target) external onlyOwner {
        require(frozenAccounts[target], "Account is not frozen");

        frozenAccounts[target] = false;
        emit AccountUnfrozen(target);
    }

    // Override the transfer function to include frozen account check
    function transfer(address recipient, uint256 amount) 
        public 
        override 
        notFrozen(msg.sender) 
        notFrozen(recipient) 
        returns (bool) 
    {
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to include frozen account check
    function transferFrom(address sender, address recipient, uint256 amount) 
        public 
        override 
        notFrozen(sender) 
        notFrozen(recipient) 
        returns (bool) 
    {
        return super.transferFrom(sender, recipient, amount);
    }

    // Additional safe minting function, callable only by the owner
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot mint to zero address");
        _mint(account, amount);
    }

    // Function to burn tokens, callable by token holders
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```
