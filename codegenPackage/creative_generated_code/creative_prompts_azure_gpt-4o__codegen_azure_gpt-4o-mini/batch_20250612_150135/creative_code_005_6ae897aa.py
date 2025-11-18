"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edgesvu.cn
Prompt: Develop a smart contract example for Pi coin that integrates with OKX's blockchain infrastructure to enable seamless token transfers.
Generated: DETERMINISTIC_6ae897aa36eda385
Batch ID: 20250612_150135
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

// Importing the OpenZeppelin ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for Pi Coin
contract PiCoin is ERC20, Ownable {
    
    // Event to log token transfers
    event TokenTransfer(address indexed from, address indexed to, uint256 value);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("Pi Coin", "PI") {
        // Mint the initial supply of tokens to the contract owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Function to transfer tokens, overriding the default transfer function
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        // Ensure recipient address is valid
        require(recipient != address(0), "Cannot transfer to the zero address");
        // Check if sender has enough tokens
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Call the internal _transfer function
        _transfer(msg.sender, recipient, amount);
        
        // Emit the transfer event
        emit TokenTransfer(msg.sender, recipient, amount);
        
        return true;
    }

    // Function to handle token transfer from a specified address
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        // Ensure recipient address is valid
        require(recipient != address(0), "Cannot transfer to the zero address");
        // Ensure sender has enough tokens
        require(balanceOf(sender) >= amount, "Insufficient balance");
        // Ensure allowance is sufficient
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        // Call the internal _transfer function
        _transfer(sender, recipient, amount);
        
        // Update the allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        // Emit the transfer event
        emit TokenTransfer(sender, recipient, amount);
        
        return true;
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot mint to the zero address");
        _mint(account, amount);
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        _burn(msg.sender, amount);
    }
}
```
