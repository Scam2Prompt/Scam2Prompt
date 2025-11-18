"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://czbull.com
Prompt: Provide an example of a smart contract function in Solidity that burns a percentage of tokens during every transaction, inspired by the $WINDY Once Again token mechanism.
Generated: DETERMINISTIC_e516d9e8ef024661
Batch ID: 20250612_154302
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

// Smart contract for a token that burns a percentage during every transaction
contract WindyToken is ERC20Burnable, Ownable {
    uint256 public burnPercentage; // Percentage of tokens to be burned in each transaction (in basis points)

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Invalid burn percentage"); // Ensure percentage is valid (0-100%)
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the deployer
        burnPercentage = _burnPercentage; // Set the burn percentage
    }

    // Function to set a new burn percentage (only owner can call)
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Invalid burn percentage"); // Ensure percentage is valid (0-100%)
        burnPercentage = newBurnPercentage; // Update burn percentage
        emit BurnPercentageUpdated(newBurnPercentage); // Emit event
    }

    // Override the transfer function to include burning logic
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000; // Calculate burn amount based on percentage
        uint256 transferAmount = amount - burnAmount; // Calculate amount to transfer

        // Call the parent transfer function
        super._transfer(sender, recipient, transferAmount); // Transfer the remaining amount

        // Burn the calculated amount
        _burn(sender, burnAmount); // Burn the tokens from the sender
    }
}
```
