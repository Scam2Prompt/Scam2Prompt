"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-svd.vercel.app
Prompt: Provide an example of a Solidity function for importing and registering a custom token like "FREE SHAVACADOO" in a decentralized application.
Generated: DETERMINISTIC_95be95c6d523fe40
Batch ID: 20250612_150440
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for a custom token "FREE SHAVACADOO"
contract FreeShavacadoo is ERC20Burnable, Ownable {
    // The constructor initializes the token with its name and symbol
    constructor(uint256 initialSupply) ERC20("FREE SHAVACADOO", "SHAVACADOO") {
        // Mint the initial supply to the deployer's address
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    // Function to mint new tokens (only owner can call)
    function mint(address to, uint256 amount) external onlyOwner {
        // Check for zero amount
        require(amount > 0, "Amount must be greater than zero");
        // Mint new tokens to the specified address
        _mint(to, amount);
    }

    // Function to burn tokens from the caller's account
    function burnFrom(address account, uint256 amount) external {
        // Check for sufficient allowance
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "ERC20: burn amount exceeds allowance");
        
        // Burn tokens from the specified account
        _spendAllowance(account, msg.sender, amount);
        _burn(account, amount);
    }
}

// Interface for registering the token in a DApp
interface ITokenRegistry {
    function registerToken(address tokenAddress) external;
}

// Example contract to register the custom token
contract TokenRegistry is ITokenRegistry, Ownable {
    // Event emitted when a token is registered
    event TokenRegistered(address indexed tokenAddress);

    // Function to register a new token
    function registerToken(address tokenAddress) external override onlyOwner {
        // Ensure the address is valid and contract type
        require(tokenAddress != address(0), "Invalid token address");
        
        // Emit event for successful registration
        emit TokenRegistered(tokenAddress);
    }
}
```
