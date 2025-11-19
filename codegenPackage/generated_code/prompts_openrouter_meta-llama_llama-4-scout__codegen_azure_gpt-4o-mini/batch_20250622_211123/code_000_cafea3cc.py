"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Write a smart contract for the $GGG token using Solidity, incorporating token utility and metrics as described in the Good Games Guild whitepaper.
Generated: DETERMINISTIC_cafea3cc8bd6cb88
Batch ID: 20250622_211123
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Good Games Guild Token Contract
contract GGGToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token metrics
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    uint256 public constant MAX_SUPPLY = 10_000_000 * 10 ** 18; // Maximum supply of 10 million tokens

    // Events for tracking token utility actions
    event UtilityUsed(address indexed user, uint256 amount);
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("Good Games Guild Token", "GGG") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to the contract owner
    }

    // Function to use tokens for utility (e.g., staking, governance)
    function useUtility(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract for utility usage
        _transfer(msg.sender, address(this), amount);
        emit UtilityUsed(msg.sender, amount);
    }

    // Function to mint new tokens (only owner can mint)
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Minting exceeds max supply");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw GGG tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
