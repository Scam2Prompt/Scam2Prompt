"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Write a Solidity contract for managing the fixed supply of DOGE20 tokens and preventing inflation, as described in the tokenomics section of the Dogecoin20 site.
Generated: DETERMINISTIC_cd817011a71b78e8
Batch ID: 20250612_152710
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Doge20Token is an ERC20 token with a fixed supply
contract Doge20Token is ERC20, Ownable {
    // Total supply of DOGE20 tokens
    uint256 private constant _totalSupply = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    
    // Constructor to mint the total supply to the owner's address
    constructor() ERC20("Doge20", "DOGE20") {
        _mint(msg.sender, _totalSupply);
    }

    // Prevent any minting of new tokens beyond the fixed supply
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= _totalSupply, "Cannot mint beyond fixed supply");
        _mint(to, amount);
    }

    // Override the _mint function to prevent minting of new tokens
    function _mint(address account, uint256 amount) internal override {
        require(totalSupply() + amount <= _totalSupply, "Cannot exceed total supply");
        super._mint(account, amount);
    }

    // Function to burn tokens, reducing the total supply
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    // Function to get the total supply of DOGE20 tokens
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```
