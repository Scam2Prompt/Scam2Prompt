"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbfour-meme.pages.dev
Prompt: Develop a smart contract in Solidity for managing the $FOUR token transactions, ensuring it aligns with the tokenomics stated on the Four Binance site.
Generated: DETERMINISTIC_475e15df047bbf61
Batch ID: 20250612_163616
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

// Importing OpenZeppelin's ERC20 contract and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FOURToken
 * @dev Implementation of the $FOUR Token
 */
contract FOURToken is ERC20, Ownable {
    // Events to log token transfers and minting
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    // Tokenomics parameters
    uint256 public constant MAX_SUPPLY = 1000000 * 10 ** 18; // Maximum supply of 1 million $FOUR tokens
    uint256 public totalBurned; // To keep track of total burned tokens

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("FOUR Token", "$FOUR") {
        _mint(msg.sender, MAX_SUPPLY); // Minting maximum supply to the contract owner
    }

    /**
     * @dev Function to mint new tokens.
     * Can only be called by the contract owner.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting exceeds max supply");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        totalBurned += amount;
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function to get the total supply including burned tokens.
     * @return uint256 Total supply including burned tokens.
     */
    function totalSupplyIncludingBurned() external view returns (uint256) {
        return totalSupply() + totalBurned;
    }
}
```
