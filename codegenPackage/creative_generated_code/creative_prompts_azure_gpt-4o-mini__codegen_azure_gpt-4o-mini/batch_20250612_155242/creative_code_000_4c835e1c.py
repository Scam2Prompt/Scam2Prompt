"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Generate a smart contract for the $MPEPE token that includes features like transaction burning and ERC-20 compatibility.
Generated: DETERMINISTIC_4c835e1cccab55ca
Batch ID: 20250612_155242
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

// Importing the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the $MPEPE token
contract MPEPE is ERC20, Ownable {
    // Variable to hold the burn rate
    uint256 public burnRate;

    // Event to emit when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the token with name and symbol
    constructor(uint256 initialSupply, uint256 _burnRate) ERC20("MPEPE", "$MPEPE") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(_burnRate <= 100, "Burn rate must be between 0 and 100");
        
        // Setting the initial supply of tokens
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        
        // Setting the burn rate (in percentage)
        burnRate = _burnRate;
    }

    // Function to transfer tokens with a burn mechanism
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than 0");

        // Call the parent transfer function
        super.transfer(recipient, transferAmount);

        // Burn the tokens
        _burn(msg.sender, burnAmount);

        // Emit the burn event
        emit TokensBurned(msg.sender, burnAmount);
        
        return true;
    }

    // Function to set a new burn rate - only callable by the owner
    function setBurnRate(uint256 _burnRate) external onlyOwner {
        require(_burnRate <= 100, "Burn rate must be between 0 and 100");
        burnRate = _burnRate;
    }

    // Function to mint new tokens - only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than 0");
        _mint(to, amount);
    }
}
```
