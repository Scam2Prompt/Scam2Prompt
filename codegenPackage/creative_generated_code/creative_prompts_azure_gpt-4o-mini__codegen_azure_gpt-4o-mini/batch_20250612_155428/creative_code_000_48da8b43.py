"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Generate a smart contract for the $MPEPE token that includes a burn mechanism after every transaction, as described in the Mpeppe presale details.
Generated: DETERMINISTIC_48da8b431bf10095
Batch ID: 20250612_155428
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
import "@openzeppelin/contracts/utils/Context.sol";

// Defining the MPEPE token contract
contract MPEPE is Context, ERC20, Ownable {
    
    // Burn percentage to be deducted from each transaction
    uint256 public burnPercentage = 2; // 2% burn on every transaction

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("MPEPE", "MPEPE") {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to owner
    }

    // Override the _transfer function to include the burn mechanism
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "ERC20: transfer amount must be greater than zero");

        // Calculate the burn amount
        uint256 burnAmount = (amount * burnPercentage) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Call the super _transfer to execute the transfer and burn
        super._transfer(sender, recipient, transferAmount);
        
        // Burn the calculated amount
        _burn(sender, burnAmount);
        emit TokensBurned(sender, burnAmount);
    }

    // Function to update the burn percentage (only callable by the owner)
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage >= 0 && newBurnPercentage <= 100, "Burn percentage must be between 0 and 100");
        burnPercentage = newBurnPercentage;
    }
}
```
