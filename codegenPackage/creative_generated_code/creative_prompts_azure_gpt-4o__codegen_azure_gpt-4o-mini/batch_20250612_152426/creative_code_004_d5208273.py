"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotokenhub.com
Prompt: Write a smart contract for a deflationary token with burn functionality, as described in CryptoTokenHub's customizable token features.
Generated: DETERMINISTIC_d5208273ee99ff41
Batch ID: 20250612_152426
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

// Import the necessary OpenZeppelin contracts for ERC20
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeflationaryToken
 * @dev This contract implements a deflationary ERC20 token with burn functionality.
 */
contract DeflationaryToken is ERC20, Ownable {
    // Percentage of tokens to be burned on each transfer (in basis points)
    uint256 public burnRate;

    /**
     * @dev Sets the values for {name} and {symbol}, and initializes the burn rate.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens to be minted.
     * @param _burnRate The percentage of tokens to burn on each transfer (in basis points).
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnRate) 
        ERC20(name, symbol) 
    {
        require(_burnRate <= 10000, "Burn rate cannot exceed 100%");
        burnRate = _burnRate;
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    /**
     * @dev Overrides the transfer function to include the burn functionality.
     * @param recipient The address to which the tokens will be sent.
     * @param amount The amount of tokens to be transferred.
     * @return A boolean that indicates if the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 sendAmount = amount - burnAmount;

        // Ensure enough tokens are being transferred
        require(amount <= balanceOf(msg.sender), "Insufficient balance");

        // Transfer the tokens
        _transfer(msg.sender, recipient, sendAmount);
        
        // Burn the tokens
        if (burnAmount > 0) {
            _burn(msg.sender, burnAmount);
        }

        return true;
    }

    /**
     * @dev Overrides the transferFrom function to include the burn functionality.
     * @param sender The address of the token sender.
     * @param recipient The address to which the tokens will be sent.
     * @param amount The amount of tokens to be transferred.
     * @return A boolean that indicates if the operation succeeded.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 sendAmount = amount - burnAmount;

        // Ensure enough tokens are being transferred
        require(amount <= balanceOf(sender), "Insufficient balance");
        require(amount <= allowance(sender, msg.sender), "Transfer amount exceeds allowance");

        // Transfer the tokens
        _transfer(sender, recipient, sendAmount);
        
        // Burn the tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }

        // Update the allowance for the spender
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        return true;
    }

    /**
     * @dev Sets a new burn rate. Can only be called by the owner of the contract.
     * @param newBurnRate The new burn rate to be set (in basis points).
     */
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10000, "Burn rate cannot exceed 100%");
        burnRate = newBurnRate;
    }
}
```
