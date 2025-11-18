"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga-hat.fund
Prompt: Develop a smart contract snippet for a meme token similar to $MAGA, ensuring it has 0% tax and is community-driven.
Generated: DETERMINISTIC_909ae23f1221e952
Batch ID: 20250612_151158
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple ERC20 token contract for a community-driven meme token
contract MemeToken is ERC20, Ownable {
    // Events for logging token transfers
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Meme Token", "MTK") {
        // Mint an initial supply of tokens to the owner's address
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to mint new tokens, restricted to the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(to, amount);
        emit Mint(to, amount);
    }

    // Function to burn tokens, reducing the total supply
    function burn(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    // Override the transfer function to ensure there is no tax on transfers
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    // Override the transferFrom function to ensure there is no tax on transfers
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "Transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);
        return true;
    }
}
```
