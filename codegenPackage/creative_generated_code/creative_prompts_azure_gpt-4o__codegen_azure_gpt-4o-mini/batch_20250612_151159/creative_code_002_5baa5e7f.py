"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiros.pages.dev
Prompt: Provide a Solidity contract example that could be used to create a token similar to $NEIRO, including features like no tax and a fixed supply of 1 billion tokens.
Generated: DETERMINISTIC_5baa5e7fdcae65d2
Batch ID: 20250612_151159
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

// @title NeiroToken
// This contract implements a simple ERC20 token with a fixed supply and no tax.
contract NeiroToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals(); // 1 billion tokens with decimals

    // @dev Constructor to initialize the token with the total supply
    constructor() ERC20("NeiroToken", "NEIRO") {
        _mint(msg.sender, TOTAL_SUPPLY); // Mint the total supply to the contract deployer
    }

    // @dev Function to mint new tokens. Only the owner can call this function.
    // This function is intentionally left unimplemented to maintain a fixed supply.
    function mint(address to, uint256 amount) external onlyOwner {
        require(false, "Minting is not allowed. Supply is fixed.");
    }

    // @dev Override the transfer function to prevent any tax deductions.
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    // @dev Override the transferFrom function to prevent any tax deductions.
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        
        // Decrease the allowance only if the transfer is successful
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);
        
        return true;
    }

    // @dev Override the approve function to allow setting allowances without tax deductions.
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        _approve(_msgSender(), spender, amount);
        return true;
    }

    // @dev Internal function to approve allowances.
    function _approve(address owner, address spender, uint256 amount) internal virtual {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
