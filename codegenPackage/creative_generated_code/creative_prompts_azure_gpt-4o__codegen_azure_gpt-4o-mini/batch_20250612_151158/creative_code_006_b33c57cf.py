"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoin-8fh.pages.dev
Prompt: Develop a smart contract to facilitate zero-tax transactions for $PEIPEI tokens, ensuring compliance with the tokenomics outlined on the website.
Generated: DETERMINISTIC_b33c57cfd36721bc
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for $PEIPEI token with zero-tax transactions
contract PEIPEI is ERC20, Ownable {
    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);
    
    // Constructor to initialize token name and symbol
    constructor(uint256 initialSupply) ERC20("PEIPEI Token", "PEIPEI") {
        _mint(msg.sender, initialSupply); // Minting initial supply to the owner
    }

    // Override transfer function to facilitate zero-tax transactions
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Call parent transfer function
        _transfer(_msgSender(), recipient, amount);
        
        // Emit transfer event
        emit Transfer(_msgSender(), recipient, amount);
        
        return true;
    }

    // Override transferFrom function to facilitate zero-tax transactions
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Allowance check
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "Transfer amount exceeds allowance");

        // Call parent transferFrom function
        _transfer(sender, recipient, amount);
        
        // Update allowance
        _approve(sender, _msgSender(), currentAllowance - amount);
        
        // Emit transfer event
        emit Transfer(sender, recipient, amount);
        
        return true;
    }

    // Function to mint new tokens
    function mint(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Mint to the zero address is not allowed");
        require(amount > 0, "Mint amount must be greater than zero");

        // Mint tokens
        _mint(account, amount);
    }

    // Function to burn tokens
    function burn(uint256 amount) public {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(_msgSender()) >= amount, "Insufficient balance to burn");

        // Burn tokens
        _burn(_msgSender(), amount);
    }

    // Function to pause trading (onlyOwner)
    function pause() public onlyOwner {
        _pause();
    }

    // Function to unpause trading (onlyOwner)
    function unpause() public onlyOwner {
        _unpause();
    }

    // Fallback function to prevent ETH deposits
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
