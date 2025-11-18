"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marvinonbase.pages.dev
Prompt: Implement a burn mechanism in Solidity for a token, where a percentage of transaction fees is automatically sent to a burn address, inspired by Marvin's collaboration with Shiba Inu.
Generated: DETERMINISTIC_7450961304fffaed
Batch ID: 20250612_152358
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

contract BurnableToken is ERC20, Ownable {
    // Percentage of transaction fees to be burned (in basis points)
    uint256 public burnPercentage;
    // Address where burnt tokens will be sent
    address public burnAddress;

    // Events for logging
    event Burned(uint256 amount, address indexed from);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage, address _burnAddress) 
        ERC20(name, symbol) {
        require(_burnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        require(_burnAddress != address(0), "Burn address cannot be zero address");

        burnPercentage = _burnPercentage; // Set the burn percentage
        burnAddress = _burnAddress; // Set the burn address
        _mint(msg.sender, initialSupply * 10 ** decimals()); // Mint initial supply to owner
    }

    // Function to set a new burn percentage (only callable by owner)
    function setBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        burnPercentage = _burnPercentage;
    }

    // Override the _transfer function to include burn mechanism
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the burn amount
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance for transfer");

        // Transfer the amount to the recipient
        super._transfer(sender, recipient, transferAmount);
        
        // Transfer the burn amount to the burn address
        if (burnAmount > 0) {
            super._transfer(sender, burnAddress, burnAmount);
            emit Burned(burnAmount, sender);
        }
    }
}
```
