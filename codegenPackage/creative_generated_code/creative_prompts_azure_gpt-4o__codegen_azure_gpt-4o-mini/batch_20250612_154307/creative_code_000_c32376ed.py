"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Write a smart contract in Solidity for a token inspired by "Crypto Burger," incorporating features such as zero tax and a fixed total supply of 692 billion tokens.
Generated: DETERMINISTIC_c32376ed08358592
Batch ID: 20250612_154307
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

// Import the ERC20 token interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title CryptoBurgerToken
// @dev A simple ERC20 token with zero tax and a fixed supply
contract CryptoBurgerToken is ERC20, Ownable {
    // Total supply of 692 billion tokens
    uint256 public constant TOTAL_SUPPLY = 692_000_000_000 * 10 ** decimals();

    // @dev Constructor that initializes the token with a name and symbol
    constructor() ERC20("Crypto Burger", "BURGER") {
        // Mint the total supply to the contract deployer (owner)
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // @dev Disable transfer tax by overriding the _transfer function from ERC20
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        // Ensure the sender has enough tokens to transfer
        require(balanceOf(sender) >= amount, "Insufficient balance for transfer");

        // Call the parent _transfer function to execute the transfer
        super._transfer(sender, recipient, amount);
    }

    // @dev Allows the owner to mint new tokens (only if necessary)
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= TOTAL_SUPPLY, "Cannot exceed total supply");
        _mint(to, amount);
    }

    // @dev Allows the owner to burn tokens (to reduce total supply if needed)
    function burn(uint256 amount) external onlyOwner {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        _burn(msg.sender, amount);
    }
}
```
