"""
Generated Code Metadata:
========================
Original URL: https://getretiksale.pages.dev
Prompt: Generate a smart contract in Solidity for creating a custom token similar to RETIK, which is built upon the Ethereum mainnet and adheres to the ERC20 standard.
Generated: DETERMINISTIC_dac022d77ee6677b
Batch ID: 20250622_210348
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

// Importing the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CustomToken is an ERC20 token that follows the ERC20 standard
contract CustomToken is ERC20, Ownable {
    // Mapping to keep track of allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event emitted when tokens are minted
    event Mint(address indexed to, uint256 amount);
    
    // Event emitted when tokens are burned
    event Burn(address indexed from, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initial minting of tokens to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
        emit Mint(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    // Function to burn tokens from a specific address
    function burnFrom(address account, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(account) >= amount, "Insufficient balance");
        require(_allowances[account][msg.sender] >= amount, "Allowance exceeded");

        _allowances[account][msg.sender] -= amount;
        _burn(account, amount);
        emit Burn(account, amount);
    }

    // Override the approve function to include error handling
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");
        _approve(msg.sender, spender, amount);
        return true;
    }

    // Internal function to handle allowances
    function _approve(address owner, address spender, uint256 amount) internal virtual {
        require(owner != address(0), "Cannot approve from the zero address");
        require(spender != address(0), "Cannot approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Function to get the allowance of a spender for a specific owner
    function allowance(address owner, address spender) public view virtual override returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
