"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogtoken-ae.pages.dev
Prompt: Write a Solidity function to implement a burn mechanism for SMOG tokens, as referenced in the roadmap's "Burn Opportunities" phase.
Generated: DETERMINISTIC_d25805d3d2193182
Batch ID: 20250612_152739
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

// Importing OpenZeppelin's ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SMOG token contract with burn functionality
contract SMOGToken is ERC20, Ownable {
    
    // Mapping to keep track of burnable amounts
    mapping(address => uint256) private _burnAllowed;

    // Events
    event TokensBurned(address indexed account, uint256 amount);

    // Constructor to initialize the token with name and symbol
    constructor(uint256 initialSupply) ERC20("SMOG Token", "SMOG") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply);
    }

    // Function to allow an account to set a burnable amount
    function allowBurn(address account, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _burnAllowed[account] = amount;
    }

    // Function to burn tokens from the caller's account
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(_burnAllowed[msg.sender] >= amount, "Burn amount exceeds allowance");

        // Burn the tokens
        _burn(msg.sender, amount);
        // Reduce the allowed burn amount
        _burnAllowed[msg.sender] -= amount;

        // Emit burn event
        emit TokensBurned(msg.sender, amount);
    }

    // Function to return the burnable amount for an account
    function burnableAmount(address account) external view returns (uint256) {
        return _burnAllowed[account];
    }
}
```
