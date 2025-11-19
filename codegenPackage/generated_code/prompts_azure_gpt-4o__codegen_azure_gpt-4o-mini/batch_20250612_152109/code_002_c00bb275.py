"""
Generated Code Metadata:
========================
Original URL: https://beef-meme.pages.dev
Prompt: Provide a Solidity example for a smart contract that burns a percentage of BEEF tokens during every transaction to maintain deflationary tokenomics, similar to the model described on the BEEF Coin website.
Generated: DETERMINISTIC_c00bb27527d835a3
Batch ID: 20250612_152109
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BEEFToken is an ERC20 token with deflationary mechanics
contract BEEFToken is ERC20Burnable, Ownable {
    // Percentage of tokens to burn during each transaction (in basis points)
    uint256 public burnPercentage; // e.g., 100 means 1%

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    // Constructor to initialize the token with a name, symbol, and initial supply
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage must be <= 100%");
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the deployer
        burnPercentage = _burnPercentage; // Set the burn percentage
    }

    // Override the transfer function to include burn logic
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than zero");

        // Burn the calculated amount
        _burn(msg.sender, burnAmount);

        // Call the parent transfer function
        return super.transfer(recipient, transferAmount);
    }

    // Override the transferFrom function to include burn logic
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than zero");

        // Burn the calculated amount
        _burn(sender, burnAmount);

        // Call the parent transferFrom function
        _transfer(sender, recipient, transferAmount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    // Function to update the burn percentage, only callable by the owner
    function updateBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = newBurnPercentage;
        emit BurnPercentageUpdated(newBurnPercentage);
    }
}
```
