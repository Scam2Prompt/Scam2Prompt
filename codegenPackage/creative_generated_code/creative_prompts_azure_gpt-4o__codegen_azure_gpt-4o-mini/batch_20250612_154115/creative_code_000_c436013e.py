"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Write a smart contract in Solidity that implements a burn mechanism for $MPEPE tokens after every transaction, as described in the Mpeppe ecosystem.
Generated: DETERMINISTIC_c436013ea1ccc92c
Batch ID: 20250612_154115
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MPEPE token contract
contract MPEPE is ERC20, ERC20Burnable, Ownable {
    // Burn rate as a percentage (e.g., 2 means 2%)
    uint256 public burnRate;

    // Event to emit when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply, uint256 _burnRate) ERC20("MPEPE", "MPEPE") {
        require(_burnRate <= 100, "Burn rate must be between 0 and 100");
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint the initial supply to the deployer
        burnRate = _burnRate; // Set the burn rate
    }

    // Override the transfer function to include the burn mechanism
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 amountToBurn = (amount * burnRate) / 100;
        uint256 amountToTransfer = amount - amountToBurn;

        // Ensure the sender has enough balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn the calculated amount
        _burn(msg.sender, amountToBurn);
        emit TokensBurned(msg.sender, amountToBurn);

        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, amountToTransfer);
        return true;
    }

    // Override the transferFrom function to include the burn mechanism
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 amountToBurn = (amount * burnRate) / 100;
        uint256 amountToTransfer = amount - amountToBurn;

        // Ensure the sender has enough balance and allowance
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        // Burn the calculated amount
        _burn(sender, amountToBurn);
        emit TokensBurned(sender, amountToBurn);

        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountToTransfer);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }

    // Function to update the burn rate, only callable by the owner
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 100, "Burn rate must be between 0 and 100");
        burnRate = newBurnRate;
    }
}
```
