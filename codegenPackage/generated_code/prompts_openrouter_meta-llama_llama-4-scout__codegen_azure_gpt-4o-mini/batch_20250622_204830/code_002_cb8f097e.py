"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a code snippet in Solidity to implement a similar token burning mechanism as described in the BTCETF roadmap, where a percentage of tokens is burned with each transaction.
Generated: DETERMINISTIC_cb8f097e78ede158
Batch ID: 20250622_204830
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BurnableToken
 * @dev ERC20 Token that burns a percentage of tokens with each transaction.
 */
contract BurnableToken is ERC20, Ownable {
    // Percentage of tokens to burn (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage;
    
    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Sets the values for {name} and {symbol}, and initializes the burn percentage.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param _burnPercentage The percentage of tokens to burn per transaction (in basis points).
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = _burnPercentage;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides the transfer function to include the burning mechanism.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return bool indicating success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
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
     * @dev Overrides the transferFrom function to include the burning mechanism.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return bool indicating success of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        // Burn the tokens
        _burn(sender, burnAmount);
        emit TokensBurned(sender, burnAmount);

        // Transfer the remaining tokens
        _transfer(sender, recipient, transferAmount);
        
        // Update the allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }

    /**
     * @dev Allows the owner to update the burn percentage.
     * @param newBurnPercentage The new burn percentage (in basis points).
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = newBurnPercentage;
    }
}
```
