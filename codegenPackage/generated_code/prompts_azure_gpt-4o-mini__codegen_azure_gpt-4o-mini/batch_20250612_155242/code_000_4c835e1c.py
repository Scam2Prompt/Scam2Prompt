"""
Generated Code Metadata:
========================
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Generate a smart contract for the $MPEPE token that includes features like transaction burning and ERC-20 compatibility.
Generated: DETERMINISTIC_4c835e1cccab55ca
Batch ID: 20250612_155242
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MPEPE Token
 * @dev ERC20 Token with transaction burning feature
 */
contract MPEPE is ERC20, Ownable {
    // Burn rate in basis points (1% = 100 basis points)
    uint256 public burnRate;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens and sets the burn rate.
     * @param initialSupply The initial supply of tokens.
     * @param _burnRate The burn rate in basis points.
     */
    constructor(uint256 initialSupply, uint256 _burnRate) ERC20("MPEPE Token", "MPEPE") {
        require(_burnRate <= 10000, "Burn rate must be less than or equal to 10000 basis points (100%)");
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        burnRate = _burnRate;
    }

    /**
     * @dev Override the transfer function to include burning of tokens.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to send.
     * @return success A boolean indicating success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn the tokens
        _burn(msg.sender, burnAmount);
        emit TokensBurned(msg.sender, burnAmount);

        // Transfer the remaining tokens
        _transfer(msg.sender, recipient, transferAmount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to include burning of tokens.
     * @param sender The address to send tokens from.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to send.
     * @return success A boolean indicating success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        // Burn the tokens
        _burn(sender, burnAmount);
        emit TokensBurned(sender, burnAmount);

        // Transfer the remaining tokens
        _transfer(sender, recipient, transferAmount);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }

    /**
     * @dev Function to update the burn rate.
     * @param newBurnRate The new burn rate in basis points.
     */
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10000, "Burn rate must be less than or equal to 10000 basis points (100%)");
        burnRate = newBurnRate;
    }
}
```
